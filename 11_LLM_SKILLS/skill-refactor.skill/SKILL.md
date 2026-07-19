---
name: skill-refactor
description: Create or refactor portable Codex, Claude, OpenCode, and similar agent skill packages while preserving behavior and safety. Use when the user asks to create, update, refactor, trim, clean up, slim down, make token-cheap, modernize, scriptify, validate, mirror, or reorganize a `SKILL.md` or skill package.
---

# Skill Refactor

Use this skill to create or improve an agent skill package without weakening its contract. This is usually refactoring, not redesign: preserve what the skill does, remove non-load-bearing weight, move deterministic work into scripts, and make the result work on Linux, macOS, and Windows.

The package is self-contained. Its runtime contract is this `SKILL.md` plus `scripts/skill_refactor_audit.py`; it must not depend on private notes, repository-specific methodology files, or machine-local paths.

## Target discovery

1. Resolve the target from the user request, current working context, or an explicit path.
2. Read the target `SKILL.md` and adjacent files before proposing edits.
3. Identify the target shape:
   - standalone skill folder: `<name>.skill/`;
   - package-owned skill: `<package>/skill/`;
   - repository-local skill: the repository's documented agent or skill directory;
   - installed skill: the active platform's configured skill directory.
4. If an installed skill has a canonical source elsewhere, edit the canonical source and use the platform's documented install or synchronization method. Do not assume symlinks are available.
5. Do not edit generated caches, dependency folders, action logs, or machine-local settings unless the user explicitly asks.

## Built-in naming methodology

Use lowercase, action-last names that reveal what a skill serves and does.

Default shape:

```text
<domain>-<entity>-<action>
```

- `domain` identifies the owning or served area;
- `entity` identifies the object being handled;
- `action` identifies the operation and comes last.

Use the shorter `<domain>-<action>` form when the domain already identifies the object and an entity would add no useful information. For example, `skill-refactor` means “refactor a skill”; a separate entity would be redundant.

Use established abbreviations only when they remain recognizable. Keep names in lowercase kebab-case and within the active platform's length limit.

Apply this convention to new skills and deliberate renames; do not bulk-rename stable skills without checking dependencies. When renaming, update together:

1. the source folder and the `name` field in `SKILL.md`;
2. agent metadata, display names, and explicit triggers;
3. registries, indexes, navigation, and current documentation;
4. installed or packaged copies managed by the active platform;
5. tests, validation commands, and live configuration references.

Preserve historical logs, completed task records, and archived evidence unless they function as live configuration.

## Cross-platform contract

Every skill created or updated by this workflow must be usable on Linux, macOS, and Windows unless the user explicitly declares it OS-specific.

- Prefer portable Python helpers using the standard library: `pathlib`, `subprocess` with argument lists, `shutil`, `tempfile`, `json`, and explicit UTF-8 reads and writes.
- Do not require Bash, zsh, PowerShell, GNU-only tools, executable permission bits, symlinks, a specific home directory, or platform-specific path syntax in the core workflow.
- Use placeholders such as `<python>`, `<skill-root>`, `<target>`, and `<workspace-root>` instead of fixed paths. Resolve `<python>` to an available Python 3 launcher, such as `py -3` or `python` on Windows and `python3` or `python` on Linux/macOS.
- If shell commands are examples, label them by operating system or provide a platform-neutral Python alternative.
- If OS-specific behavior is necessary, isolate it behind platform detection and document the supported paths or fallbacks.
- Do not rely on symlinks as the only install strategy. The skill must also work when copied as a real folder.
- Keep bundled scripts dependency-light. If third-party packages are unavoidable, state the requirements and fail with a clear installation message.
- Review path handling, quoting, case sensitivity, CRLF/LF behavior, and permission assumptions before declaring the result portable.

## Refactor workflow

1. **Audit first.** Run the bundled read-only helper when useful:

```text
<python> <skill-refactor-root>/scripts/skill_refactor_audit.py <target> --format markdown
```

2. **Inventory load-bearing behavior.** Record triggers, required inputs, outputs, side effects, safety gates, scripts, templates, references, validation commands, and installation rules. Score the need for settings and action logs using the heuristics below.
3. **Delete only non-load-bearing weight.** Remove duplicated prose, stale paths, contradicted rules, repeated checklists, obsolete examples, and explanations that do not change execution. Ask before deleting anything that might remove behavior.
4. **Move mechanics out of `SKILL.md`.** Prefer scripts for deterministic parsing, hashing, frontmatter handling, table generation, diffs, renames, and filesystem inventories. Default to portable Python for reusable helpers.
5. **Move static bulk to resources.** Long templates, examples, schemas, prompts, and reference material belong in `references/`, `assets/`, or script templates loaded only when needed.
6. **Smooth the happy path.** Make the common path one clear command or ordered sequence. Prefer read-only or dry-run defaults and require an explicit apply flag or approval for risky writes.
7. **Preserve host conventions without hardcoding one host.** Follow the target repository's link, metadata, formatting, and navigation conventions, but keep reusable instructions free of private locations and machine-specific assumptions.
8. **Preserve behavior.** Do not weaken overwrite protection, dirty-file gates, validation, provenance, or other safety rules. Document intentional behavior changes separately from refactoring.

## Settings and action-log methodology

Do not add settings or logs to every skill. Decide independently for each target and record the rationale in the final report.

### When to add settings

Count one settings signal for each true condition:

- the skill has at least two operator-tunable, non-secret values;
- values vary by user, machine, workspace, provider, or environment;
- the same values must persist across repeated runs;
- multiple scripts need the same values;
- users need discoverable defaults, types, or validation rules.

Add a settings surface when the score is **2 or more**. Add one with a lower score only when a hardcoded value would break portability or safe reuse. Do not count credentials as a settings signal; secrets belong in environment variables or a platform secret store.

When settings are justified:

- version `settings.example.toml` with documented, non-secret defaults;
- keep operator overrides in `settings.local.toml`, ignored by version control and publication;
- create the local file only when missing and never overwrite operator edits;
- use precedence `built-in defaults < project settings < local settings < environment or CLI overrides`;
- validate types and unknown keys, resolve relative paths from the settings file, and use portable path handling;
- avoid settings for a single stable value that belongs in the skill contract.

### When to add an action log

Count one logging signal for each true condition:

- the skill writes, deletes, renames, moves, publishes, or otherwise changes durable state;
- one run can affect multiple targets;
- the skill changes an external system or calls a mutating API;
- retry, resume, rollback, or duplicate prevention needs prior-run evidence;
- failures are expensive or difficult to reconstruct;
- auditability or explicit user review is part of the contract.

Add an action log when the score is **2 or more**. Treat it as mandatory for destructive or irreversible operations unless the user explicitly declines after the risk is explained. Do not add persistent logs to read-only inspection, deterministic validation, or low-cost idempotent generation with no external side effects.

When logging is justified:

- use append-only `action_log.local.ndjson` unless the host project has an established equivalent;
- write one JSON object per event with UTC timestamp, run ID, action, non-sensitive target identifier, outcome, dry-run flag, tool version, and concise error data when relevant;
- record hashes or identifiers instead of full private content;
- never log secrets, access tokens, credentials, or unnecessary personal data;
- keep logs ignored and unpublished, document retention or size limits, and make logging failure non-fatal unless compliance requires otherwise.

### Implementation rules

- If local settings or logs are introduced, add precise ignore rules without replacing an existing ignore file.
- Keep loaders and log writers dependency-light and shared rather than duplicating them across scripts.
- Make settings validation fail clearly before side effects begin.
- Make log writes append-only and safe across normal interruptions; use file locking or a per-run file when concurrent writers are possible.
- Do not rely on private assistant memory or unavailable external documents for runtime behavior. Put required rules in `SKILL.md`, bundled resources, or versioned example settings.
- The bundled audit helper remains settings-free and log-free because it is read-only and has no persistent operator-tunable state.

## Ask before changing

Ask the user before proceeding when:

- the target package or bundle scope is unclear;
- a deletion might remove real behavior;
- there are multiple plausible homes for shared code or resources;
- an installed package must be overwritten, relinked, or backed up;
- validation requires network access, dependency installation, or destructive writes;
- the request is redesign rather than refactoring.

State the best current interpretation and the safest proposed path; avoid a long menu unless requested.

## Verification

Before replying, run the smallest useful checks for the changed files.

```text
<python> <skill-refactor-root>/scripts/skill_refactor_audit.py <target> --format markdown
<python> -m py_compile <changed-python-files>
```

Also:

- run the active agent platform's native skill validator when one is available;
- run the repository's diff and whitespace checks when the target is version-controlled;
- exercise read-only or dry-run modes against realistic target data before applying writes;
- compare the before/after `SKILL.md` line count and confirm the trigger description still covers the intended requests;
- statically review all bundled instructions and scripts for Linux, macOS, and Windows portability;
- report any OS-specific behavior that could not be tested directly.

## Final report

Report compactly:

- target skill;
- files changed;
- before/after `SKILL.md` line count;
- what was removed, moved, or preserved;
- validation commands and results;
- the settings and action-log decision, scores, and rationale;
- remaining uncertainty or required installation follow-up.
