# Source Record Contract

Use this after reading the live `81_REFERENCES` authoring rules. This file carries static templates and checks; the live rule notes are authoritative when they differ.

## Reference title

Use this exact title/file stem pattern unless the user overrides it:

`author(s) - title (source domain, published)`

Example:

`Юрий Е. - Человек рабочего продукта (systemsworld.club, 2025-08-29)`

Rules:

- Use the human-visible author name(s), not usernames, when available. For repositories, use the profile/display name when available; otherwise use the owner/login.
- Use the source domain without `www.`.
- Use `published` as `YYYY-MM-DD` when known. For repositories, use the repo creation date when no publication/release date is more appropriate. For books, use the original publication date/year when known.
- If the date is unknown, ask only when the date is important; otherwise use `unknown-date` when the user wants to proceed.
- Use the same string for the filename stem, frontmatter `title`, and H1.
- Sanitize filename-forbidden characters only when necessary.

## Frontmatter

Default minimal frontmatter for article/web references:

```yaml
type: source
subtype: article
title: Author - Title (domain, YYYY-MM-DD)
authors:
  - Author
year: YYYY
published: YYYY-MM-DD
source: https://example.com/path
topics:
  - topic-in-english
date: YYYY-MM-DD
authorship: external
```

For repositories, use `subtype: repo` and add `local_copy` only after the clone/download exists:

```yaml
local_copy: /Users/am/Documents/Repos/owner/repo
```

For books or book files, use `subtype: book` and add `gdrive_path` only after the Drive file/folder exists:

```yaml
gdrive_path: /path/to/Google Drive/books/file.pdf
```

Topics in `81_REFERENCES/` must be in English. Prefer specific retrieval terms over container repeats.

Do not add these fields by default:

- `status`
- `local_copy` unless a repo/local artifact actually exists
- `gdrive_path` unless a Google Drive artifact actually exists
- `yandex_disk` for new references unless the user explicitly asks for an older Yandex Disk path to be recorded

## Body shape

For article/web references, store the full accessible copy in the note:

```markdown
# Author - Title (domain, YYYY-MM-DD)

Source: https://example.com/path

Saved for personal use on YYYY-MM-DD.

## Original text

Cleaned Markdown copy of the accessible article/post text, with meaningful images embedded as `![[82_ASSETS/51_attachments/descriptive-filename.ext]]`.
```

For repositories, keep the note as a pointer to the source plus local clone/download:

```markdown
# Author - Title (github.com, YYYY-MM-DD)

Source repo: https://github.com/owner/repo

Local copy: /Users/am/Documents/Repos/owner/repo
```

For books, keep the note as a bibliographic/source pointer plus Drive location when available:

```markdown
# Author - Title (domain, YYYY-MM-DD)

Source/book page: https://example.com/book

Google Drive copy: /path/to/Google Drive/books/file.pdf
```

Do not retell, summarize, or add interpretation unless the user asks.

## Completion check

Before replying, verify:

- File path is under the correct flat area folder in `81_REFERENCES/`, or at the `81_REFERENCES/` root only when intentionally unclassified.
- `title` and H1 match the filename stem.
- `source` contains the original URL.
- `authorship: external` is present.
- `topics` are in English and follow the live `81_REFERENCES` authoring rules.
- For articles/web posts, the note contains the full accessible text or explicitly states why only partial text/metadata was saved.
- For article/site imports, a Python scraper was used through `51_DEV/10_PROD/obsidian_vault_python`, or the note/report states why a scraper was unnecessary or unavailable.
- For multi-page site imports, a dry-run/manifest verified page scope, groups/folders, counts, duplicates, and skipped unrelated links before final writes.
- For article/web images, meaningful images are downloaded into `82_ASSETS/51_attachments/`, embedded locally in the note, and verified to exist; irrelevant/decorative images are skipped.
- For repos, the local repo/download path exists and `local_copy` matches it.
- For books, `gdrive_path` is present only when the Google Drive file/folder exists; otherwise the note/body and final reply state that the Drive copy is pending.
- `status` and `yandex_disk` are absent unless explicitly requested.
- `local_copy` and `gdrive_path` are absent unless their corresponding artifacts exist.
- No stale nested reference paths such as `81_REFERENCES/...`, `81_REFERENCES/32_LEARNING/...`, or `81_REFERENCES/53_RESEARCH/...` were introduced.
