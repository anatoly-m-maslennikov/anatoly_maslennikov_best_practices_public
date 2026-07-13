# anatoly-m-playbooks

Public prompts and Codex-style skills that I use or have used as reusable operating patterns.

This README is the repo HUB: use it to jump to skill packages, source-sync context, the moved methodology, and the license.

## Main areas

| Area | What it contains |
|---|---|
| [DSET Loops Framework](https://github.com/anatoly-m-maslennikov/dset-loops-framework) | Methodology moved to a separate public repo. |
| [Old methodology location](01_INDUSTRIAL_VIBE_CODING_TOOL_DEVELOPMENT_PLAYBOOK/README.md) | Redirect file kept for old `anatoly-m-playbooks` links. |
| [LLM skills](11_LLM_SKILLS/) | Codex-style skill packages with prompt references and examples. |

## DSET Loops Framework

The methodology moved to a separate repository: [DSET Loops Framework](https://github.com/anatoly-m-maslennikov/dset-loops-framework).

## LLM skills

| Skill | What it does | Folder |
|---|---|---|
| [CNG Create Episode Images](11_LLM_SKILLS/cng-create-ep-images.skill/) | Create persistent Obsidian image asset sets for Colleagues, not guys posts. | `11_LLM_SKILLS/cng-create-ep-images.skill/` |
| [CNG Podcast to Post](11_LLM_SKILLS/cng-podcast-to-post.skill/) | Transform raw Russian Colleagues, not guys podcast transcripts into publishable first-person Obsidian Markdown post drafts in Anatoly/CNG voice. | `11_LLM_SKILLS/cng-podcast-to-post.skill/` |
| [CNG Post Packaging](11_LLM_SKILLS/cng-post-to-title-subtitle-promo.skill/) | Generate CNG-style title variants, subtitle variants, and short promo texts from a finished Colleagues, not guys post. | `11_LLM_SKILLS/cng-post-to-title-subtitle-promo.skill/` |
| [Codex Skill Mirror](11_LLM_SKILLS/codex-skill-mirror.skill/) | Maintain Codex custom skill sources in the Obsidian vault and keep per-skill entries under `~/.codex/skills` as symlinks to those vault sources. | `11_LLM_SKILLS/codex-skill-mirror.skill/` |
| [General Answer Prompt](11_LLM_SKILLS/general-answer-system-prompt.skill/) | Apply or adapt a general-purpose answer system prompt that emphasizes role selection, explicit task interpretation, concise task-type playbooks, real citations, and final validation. | `11_LLM_SKILLS/general-answer-system-prompt.skill/` |
| [HH CV to Good Resume](11_LLM_SKILLS/hh-cv-to-good-resume.skill/) | Convert Russian HeadHunter or hh.ru resume/CV exports into concise professional resume drafts for a target role. | `11_LLM_SKILLS/hh-cv-to-good-resume.skill/` |
| [Obsidian Reference Doc](11_LLM_SKILLS/obsidian-reference-doc.skill/) | Create or update Obsidian source/reference records for third-party material. | `11_LLM_SKILLS/obsidian-reference-doc.skill/` |
| [Refactor Skills](11_LLM_SKILLS/refactor-skills.skill/) | Create or refactor Codex, Claude, OpenCode, and Obsidian-vault skill packages to be lean, token-cheap, script-backed where useful, and portable across Linux, macOS, and Windows without changing their behavior. | `11_LLM_SKILLS/refactor-skills.skill/` |
| [Refine Article Prompt](11_LLM_SKILLS/refine-article-prompt-from-redacted-example.skill/) | Rewrite an article-generation prompt by comparing source material, an original prompt, and a redacted target article. | `11_LLM_SKILLS/refine-article-prompt-from-redacted-example.skill/` |
| [System Prompt Generator](11_LLM_SKILLS/system-prompt-generator.skill/) | Generate a production-ready system prompt for a specified LLM role, goal, audience, context, task type, output format, browsing/citation policy, and quality bar. | `11_LLM_SKILLS/system-prompt-generator.skill/` |

## License

This project is licensed under the Creative Commons Attribution–NonCommercial 4.0 International License. See the [LICENSE](LICENSE.txt) file for details.
