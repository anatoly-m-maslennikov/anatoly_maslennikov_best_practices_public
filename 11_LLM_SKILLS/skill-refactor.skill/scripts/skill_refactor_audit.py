#!/usr/bin/env python3
"""Read-only audit helper for portable agent skill folders."""
from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Any

LOCAL_PATTERNS = (".local.",)
CACHE_NAMES = {"__pycache__", ".DS_Store"}
RESOURCE_DIRS = ("agents", "scripts", "references", "assets")
SKIP_DIRS = {".git", ".hg", ".svn", "node_modules", ".venv", "venv"}
SETTINGS_PREFIXES = ("settings.", "config.")
ACTION_LOG_NAMES = {"action_log.local.ndjson", "action-log.local.ndjson"}


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return {}, text
    end_index = next((index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---"), None)
    if end_index is None:
        return {}, text
    raw = "".join(lines[1:end_index])
    body = "".join(lines[end_index + 1 :])
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"\'')
    return data, body


def iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [name for name in dirnames if name not in SKIP_DIRS]
        for filename in filenames:
            files.append(Path(dirpath) / filename)
    return sorted(files)


def line_count(path: Path) -> int:
    try:
        return len(path.read_text(encoding="utf-8", errors="replace").splitlines())
    except OSError:
        return 0


def detect_code_fences(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            lang = stripped[3:].strip() or "plain"
            counts[lang] = counts.get(lang, 0) + 1
    return counts


def format_command(parts: list[str]) -> str:
    """Format an argument list for the current operating system."""
    if os.name == "nt":
        return subprocess.list2cmdline(parts)
    return shlex.join(parts)


def classify_state_files(rel_files: list[str]) -> tuple[list[str], list[str]]:
    settings_files: list[str] = []
    action_log_files: list[str] = []
    for rel_file in rel_files:
        path = Path(rel_file)
        name = path.name.lower()
        if name.startswith(SETTINGS_PREFIXES):
            settings_files.append(rel_file)
        if name in ACTION_LOG_NAMES or path.suffix.lower() == ".log" or "logs" in {part.lower() for part in path.parts[:-1]}:
            action_log_files.append(rel_file)
    return settings_files, action_log_files


def state_review(settings_files: list[str], action_log_files: list[str], local_state: list[str]) -> list[str]:
    checks: list[str] = []
    if settings_files:
        checks.append("Confirm settings contain no secrets and document defaults, precedence, types, and unknown-key handling.")
    if action_log_files:
        checks.append("Confirm action logs are append-only, redacted, size-limited, and excluded from publication.")
    if local_state:
        checks.append("Confirm every local-state file is ignored by version control and packaging.")
    if not settings_files and not action_log_files:
        checks.append("No settings or action-log files detected; score both needs before adding runtime state.")
    return checks


def suggested_checks(root: Path, scripts: list[Path]) -> list[str]:
    checks: list[str] = []
    py_files = [path for path in scripts if path.suffix.lower() == ".py"]
    if py_files:
        checks.append(format_command([sys.executable, "-m", "py_compile", *(str(path) for path in py_files)]))
    checks.append(f"Run the active platform's native skill validator against {root} when available.")
    checks.append(f"Review the version-control diff and whitespace for {root} when it is tracked.")
    return checks


def audit(target: Path) -> dict[str, Any]:
    target = target.expanduser().resolve()
    skill_file = target if target.name == "SKILL.md" else target / "SKILL.md"
    root = skill_file.parent
    result: dict[str, Any] = {
        "target": str(target),
        "root": str(root),
        "skill_file": str(skill_file),
        "exists": skill_file.exists(),
    }
    if not skill_file.exists():
        return result

    text = skill_file.read_text(encoding="utf-8", errors="replace")
    frontmatter, body = parse_frontmatter(text)
    files = iter_files(root)
    rel_files = [str(path.relative_to(root)) for path in files]
    local_state = [
        path
        for path in rel_files
        if any(part in CACHE_NAMES for part in Path(path).parts) or any(pattern in path for pattern in LOCAL_PATTERNS)
    ]
    markdown_files = [path for path in files if path.suffix.lower() == ".md"]
    scripts = [path for path in files if path.suffix.lower() in {".py", ".sh", ".mjs", ".js", ".ts"}]
    settings_files, action_log_files = classify_state_files(rel_files)

    result.update(
        {
            "frontmatter": frontmatter,
            "skill_md_lines": len(text.splitlines()),
            "body_lines": len(body.splitlines()),
            "body_chars": len(body),
            "code_fences": detect_code_fences(text),
            "resource_dirs": {name: (root / name).is_dir() for name in RESOURCE_DIRS},
            "file_count": len(files),
            "files": rel_files,
            "local_state_candidates": local_state,
            "settings_files": settings_files,
            "action_log_files": action_log_files,
            "state_review": state_review(settings_files, action_log_files, local_state),
            "large_markdown_files": [
                {"path": str(path.relative_to(root)), "lines": line_count(path)}
                for path in markdown_files
                if line_count(path) >= 120
            ],
            "script_files": [str(path.relative_to(root)) for path in scripts],
            "suggested_checks": suggested_checks(root, scripts),
        }
    )
    return result


def to_markdown(data: dict[str, Any]) -> str:
    if not data.get("exists"):
        return f"# Skill refactor audit\n\nMissing SKILL.md: `{data['skill_file']}`\n"
    frontmatter = data.get("frontmatter", {})
    lines = [
        "# Skill refactor audit",
        "",
        f"- Root: `{data['root']}`",
        f"- Name: `{frontmatter.get('name', '')}`",
        f"- Description present: {'yes' if frontmatter.get('description') else 'no'}",
        f"- SKILL.md lines: {data['skill_md_lines']}",
        f"- Files: {data['file_count']}",
        f"- Scripts: {', '.join(data['script_files']) if data['script_files'] else 'none'}",
        f"- Local-state candidates: {', '.join(data['local_state_candidates']) if data['local_state_candidates'] else 'none'}",
        f"- Settings files: {', '.join(data['settings_files']) if data['settings_files'] else 'none'}",
        f"- Action-log files: {', '.join(data['action_log_files']) if data['action_log_files'] else 'none'}",
        "",
        "## Resource dirs",
    ]
    for name, exists in data["resource_dirs"].items():
        lines.append(f"- `{name}/`: {'yes' if exists else 'no'}")
    if data["large_markdown_files"]:
        lines.extend(["", "## Large Markdown files"])
        for item in data["large_markdown_files"]:
            lines.append(f"- `{item['path']}` — {item['lines']} lines")
    if data["code_fences"]:
        lines.extend(["", "## Code fences"])
        for language, count in sorted(data["code_fences"].items()):
            lines.append(f"- `{language}`: {count}")
    lines.extend(["", "## Settings and action-log review"])
    for check in data["state_review"]:
        lines.append(f"- {check}")
    lines.extend(["", "## Suggested checks"])
    for check in data["suggested_checks"]:
        lines.append(f"- `{check}`")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only audit for a skill folder before refactoring.")
    parser.add_argument("target", help="Skill folder or SKILL.md path")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    args = parser.parse_args()

    data = audit(Path(args.target))
    if args.format == "json":
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(to_markdown(data), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
