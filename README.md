# anatoly-m-playbooks

Public playbooks, prompts, and Codex-style skills that I use or have used as reusable operating patterns.

This README is the repo HUB: use it to jump to framework docs, skill packages, source-sync context, and the license.

## Main areas

| Area | What it contains |
|---|---|
| [Industrial vibe coding framework](01_INDUSTRIAL_VIBE_CODING_FRAMEWORK/) | Public methodology/playbook docs exported from vault source files. |
| [LLM skills](11_LLM_SKILLS/) | Codex-style skill packages with prompt references and examples. |

## Industrial vibe coding framework

| Playbook | Source role |
|---|---|
| [Tool Development Playbook](01_INDUSTRIAL_VIBE_CODING_FRAMEWORK/00_Tool%20Development%20Playbook.md) | methodology source |
| [Spec Authoring Patterns — Service Spec Conventions](01_INDUSTRIAL_VIBE_CODING_FRAMEWORK/01_Spec%20Authoring%20Patterns%20%E2%80%94%20Service%20Spec%20Conventions.md) | methodology source |
| [Eval and Test Plan Patterns — Test Plan Authoring Conventions](01_INDUSTRIAL_VIBE_CODING_FRAMEWORK/02_Eval%20and%20Test%20Plan%20Patterns%20%E2%80%94%20Test%20Plan%20Authoring%20Conventions.md) | methodology source |
| [Implementation Plan Patterns — Service Build Conventions](01_INDUSTRIAL_VIBE_CODING_FRAMEWORK/03_Implementation%20Plan%20Patterns%20%E2%80%94%20Service%20Build%20Conventions.md) | methodology source |
| [General Build Rules — Tool Code Conventions](01_INDUSTRIAL_VIBE_CODING_FRAMEWORK/04_General%20Build%20Rules%20%E2%80%94%20Tool%20Code%20Conventions.md) | methodology source |
| [Layered Build Standard — DDD, TDD, Small Functions, Typed Gates](01_INDUSTRIAL_VIBE_CODING_FRAMEWORK/05_Layered%20Build%20Standard%20%E2%80%94%20DDD%2C%20TDD%2C%20Small%20Functions%2C%20Typed%20Gates.md) | methodology source |
| [External Grounding — LLM Power-User Practice](01_INDUSTRIAL_VIBE_CODING_FRAMEWORK/06_External%20Grounding%20%E2%80%94%20LLM%20Power-User%20Practice.md) | methodology source |

## LLM skills

| Skill | What it does | Folder |
|---|---|---|
| [CNG Podcast to Post](11_LLM_SKILLS/cng-podcast-to-post.skill/) | Transform raw Russian Colleagues, not guys podcast transcripts into publishable first-person Obsidian Markdown post drafts in Anatoly/CNG voice. | `11_LLM_SKILLS/cng-podcast-to-post.skill/` |
| [CNG Post Packaging](11_LLM_SKILLS/cng-post-to-title-subtitle-promo.skill/) | Generate CNG-style title variants, subtitle variants, and short promo texts from a finished Colleagues, not guys post. | `11_LLM_SKILLS/cng-post-to-title-subtitle-promo.skill/` |
| [General Answer Prompt](11_LLM_SKILLS/general-answer-system-prompt.skill/) | Apply or adapt a general-purpose answer system prompt that emphasizes role selection, explicit task interpretation, concise task-type playbooks, real citations, and final validation. | `11_LLM_SKILLS/general-answer-system-prompt.skill/` |
| [HH CV to Good Resume](11_LLM_SKILLS/hh-cv-to-good-resume.skill/) | Convert Russian HeadHunter or hh.ru resume/CV exports into concise professional resume drafts for a target role. | `11_LLM_SKILLS/hh-cv-to-good-resume.skill/` |
| [Refine Article Prompt](11_LLM_SKILLS/refine-article-prompt-from-redacted-example.skill/) | Rewrite an article-generation prompt by comparing source material, an original prompt, and a redacted target article. | `11_LLM_SKILLS/refine-article-prompt-from-redacted-example.skill/` |
| [System Prompt Generator](11_LLM_SKILLS/system-prompt-generator.skill/) | Generate a production-ready system prompt for a specified LLM role, goal, audience, context, task type, output format, browsing/citation policy, and quality bar. | `11_LLM_SKILLS/system-prompt-generator.skill/` |

## License

This project is licensed under the Creative Commons Attribution–NonCommercial 4.0 International License. See the [LICENSE](LICENSE.txt) file for details.
