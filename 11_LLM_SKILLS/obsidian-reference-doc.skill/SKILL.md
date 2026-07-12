---
name: obsidian-reference-doc
description: Create or update Obsidian source/reference records for third-party material. Use when saving articles, web posts, site/page collections, and docs pages into 81_REFERENCES as full personal-use local copies with meaningful images downloaded into 82_ASSETS/51_attachments; for websites use a deterministic Python scraper through 51_DEV/10_PROD/obsidian_vault_python. Also use for cloning/downloading repository references into /Users/am/Documents/Repos, placing book/PDF/EPUB references in Google Drive, creating source notes, following `00_META/40_Operations/10_81_REFERENCES authoring rules/00_81_REFERENCES authoring rules HUB.md`, using the reference-title format "author(s) - title (source domain, published)", or cleaning reference-note metadata/templates.
---

# Obsidian Reference Doc

## Mission

Create or update one canonical Markdown source record under `81_REFERENCES/` for external/not-mine material, then route the durable local copy by source type. Do not retell, summarize, or add interpretation unless the user asks. Do not paste full third-party text in chat; save accessible copies in vault files only.

## Load order

1. Read the live rules first:
   - `00_META/40_Operations/10_81_REFERENCES authoring rules/00_81_REFERENCES authoring rules HUB.md`
   - the child rule notes in the same folder: `01_Placement.md`, `02_Naming.md`, `03_Frontmatter.md`, `04_Topics.md`, `05_Source-type routing.md`, `06_Web source import workflow.md`, and `07_Verification checklist.md`
2. When creating/updating a reference note, load `references/source-record-contract.md` for the concrete title, frontmatter, body, and completion-check details that used to live in this file.
3. For article/web/site imports, copy and customize `scripts/reference_web_scraper_template.py` rather than relying on manual copy/paste or LLM-only extraction.

Live vault rule notes win over this skill and its reference file when they drift. Use `00_META/00_Vault structure/00_Vault structure HUB.md`, `00_META/20_Writing workflows/00_Writing workflows HUB.md`, `00_META/10_Property schema/00_Property schema HUB.md`, and `82_ASSETS/53_templates/Reference - web post (template).md` only when placement, workflow, property, or Templater context is needed.

## Source-type routing

- Article, web post, forum post, docs page, or site/page collection: save the full accessible main text in the `81_REFERENCES/` note for Anatoly's personal use. Download meaningful in-content images into `82_ASSETS/51_attachments/` and replace external image URLs with Obsidian embeds. Skip decorative, tracking, avatar, logo, ad, share-button, and unrelated images. Keep the original source URL and metadata. Do not bypass paywalls, logins, DRM, or other access controls; if full text or images are unavailable, save what is accessible and state the limitation.
- Repository or code template: ensure a local copy exists under `/Users/am/Documents/Repos/`. First scan for an existing clone or name collision. If absent, clone or download the repo there using current directory conventions; for GitHub repos prefer `/Users/am/Documents/Repos/<owner>/<repo>` unless the live folder structure suggests another established convention. Create/update the `81_REFERENCES/` note as a source record pointing to both the URL and the local path.
- Book, PDF, EPUB, paper, dataset, or book pointer: keep the actual file in Google Drive, not in the vault. Discover the current Google Drive root and books folder from live filesystem/vault docs before writing. If only a source page is available and no legitimate file is supplied or downloadable, create the reference note with the source URL and report that the file still needs to be added to Drive. Record `gdrive_path` only when the file/folder exists.
- Video, talk, podcast, or media page: create a source record with URL, metadata, and pointer text only unless a transcript is explicitly supplied or created by another workflow.

## Web/site scraping

Default to a deterministic Python scraper for article, docs, web post, or site/page-collection imports.

- Run scrapers with the canonical vault Python environment: `uv --project 51_DEV/10_PROD/obsidian_vault_python run python <script.py>`.
- Prefer the stack already available there: `requests`, `beautifulsoup4`, `markdownify`, `lxml`, and `pyyaml`. If a needed package is missing, add it with `uv --project 51_DEV/10_PROD/obsidian_vault_python add <package>` only after the user approves any required network/dependency write.
- For one-off single-page imports, a scratch-directory scraper is acceptable. For repeatable, brittle, or multi-page site imports, save a descriptive script under `51_DEV/10_PROD/obsidian_vault_python/scripts/`. Use `scripts/reference_web_scraper_template.py` as the starting template for single-page article/web imports; copy it first, customize selectors/metadata, and run `--dry-run` before writing.
- For multi-page site imports, do a dry-run or manifest first: source URL, discovered target URLs, grouping/folders, intended note paths, page counts, skipped URL patterns, and duplicate checks. Do not start broad crawling without a bounded manifest.
- Extract main article/body content only. Exclude navigation, sidebar, footer, comments, author bio, email/signup forms, booking CTAs, ads, share widgets, and unrelated promo blocks unless the user explicitly wants them.
- Download meaningful in-article images through the scraper into `82_ASSETS/51_attachments/` with deterministic descriptive filenames. Replace image HTML/URLs with local Obsidian embeds.
- When using `markdownify`, verify it did not escape Obsidian embed paths such as `82\_ASSETS`; normalize them back to `Obsidian image embed syntax for 82_ASSETS/51_attachments/file.ext` and keep embeds separated from adjacent prose/headings.
- Keep scraper logs and final chat reports path/count focused; do not print full copied article text in chat or logs.

## Workflow

1. Identify source type first: article/web text, repository/code template, book/file, media page, or generic source pointer.
2. Read the live `81_REFERENCES` authoring rules and `references/source-record-contract.md`, then identify source URL, author(s), title, published/created date, domain, subtype, English topics, and the correct flat `81_REFERENCES/` area folder from user input, selected text, current note, repository metadata, book metadata, or the live web page.
3. Fetch/verify live metadata when the user gave a URL and the current content matters. For current web/GitHub/book pages, prefer live verification over memory.
4. For article/web text, use the web/site scraping rule: extract the full accessible main text, convert it to clean Markdown, download meaningful images into `82_ASSETS/51_attachments/`, and create/update the `81_REFERENCES/` note with `## Original text` plus local `Obsidian image embed syntax` image embeds where the images belong. Use descriptive image filenames based on the reference title/source; avoid overwriting existing attachments.
5. For repositories, scan `/Users/am/Documents/Repos/` for an existing copy, clone/download if needed, then record the local path in `local_copy` and the body. Ask for approval when required for network or writes outside the vault.
6. For books and other large files, discover the current Google Drive/book storage path before moving/downloading. Put the file there only when it is supplied or legitimately downloadable, then record the path in `gdrive_path` and the body. Ask/report if no file is available.
7. Build the title using `author(s) - title (source domain, published)` unless the user or live rules require an established override.
8. Create or update the note under the correct flat area folder in `81_REFERENCES/`. Leave notes at `81_REFERENCES/` root only when intentionally unclassified. Prefer Obsidian CLI for vault-aware moves/renames; if it aborts, use a filesystem fallback only after checking the destination does not already exist.
9. Keep Markdown prose unwrapped; do not insert manual prose line wraps.
10. Verify the final note and any off-vault artifact paths using the live `07_Verification checklist.md` plus `references/source-record-contract.md`.

## Safety gates

- Do not add `status`, `local_copy`, `gdrive_path`, or `yandex_disk` by default; use artifact pointer fields only when the corresponding artifact exists or the user explicitly requests the legacy field.
- Do not introduce stale nested mirror paths such as `81_REFERENCES/...`, `81_REFERENCES/32_LEARNING/...`, or `81_REFERENCES/53_RESEARCH/...`.
- Do not overwrite existing notes, attachments, repo clones, or Drive files without checking for collisions and getting approval when needed.
- Do not use root-level symlink homes for source repositories. If a repo must be visible inside the vault, follow the live rule note for optional area-folder symlinks.
