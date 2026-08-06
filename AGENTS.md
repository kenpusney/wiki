# AGENTS.md

> Follow `.agents/document-guide.md` for all agent-facing documents in this repo.
> Follow `.agents/obsidian-rules.md` for Obsidian-specific conventions.

## Repo

- Obsidian Vault: `content/`
- Site generator: Material for MkDocs
- Published site: https://wiki.kimleo.net
- Entry: `content/index.md`
- Nav root: `content/站点目录.md`

## Repo Structure

```
content/          # Published content (Material for MkDocs)
00.inbox/         # Inbound staging for publishable / WIP content
01.index/         # MOC for working items
02.domain/        # Areas (topics / domains)
03.projects/      # Projects (time-bounded, outcome-driven)
04.resources/     # Resources (references, collections)
05.journals/      # Dated notes / journals
10.meta/          # Metadata, base files, templates
99.archive/       # Archive
```

## Content Structure

| Path | Purpose | Status |
|------|---------|--------|
| `articles/` | Original articles | Active |
| `articles/opinion/` | Opinion shorts | Sparse |
| `notes/` | Study notes | Active |
| `notes/tech/` | Technical notes | Active |
| `notes/controversial-words/` | Word distinctions | Sparse |
| `projects/` | Project descriptions | Needs update |
| `publications/` | Published works | Active |
| `collect/` | External collections | Large |
| `collect/zhihu/selected/` | Curated Zhihu Q&A | Large |
| `meta/` | Wiki meta docs | Small |

## Workflow Loop

1. **Discover** - Source content from external inputs.
2. **Explore** - Read, understand, and extract key information.
3. **Organize** - Structure and place into `content/` or PARA working directories.
4. **Learn** - Internalize via notes, summaries, reviews.
5. **Produce** - Create original articles, tutorials, projects.

## 00.inbox Protocol

`00.inbox/` is the unified entry point for publishable or in-progress content.

- All new content enters `00.inbox/` first.
- Naming:
  - `YYYYMMDD-topic-slug.md` for time-sensitive content
  - `Draft-topic.md` for incomplete drafts
  - `Collect-source-topic.md` for external collections
- Ready-to-publish content must be complete; in-progress content may be incomplete.
- When organizing, start from `00.inbox/` and move files to target directories.
- After moving, update `content/站点目录.md`, `01.index/index.md`, or relevant index pages.

## Writing Conventions

- Language: Chinese; technical terms in English.
- Format: Obsidian Markdown (`[[wikilinks]]`, Callouts, Frontmatter).
- Frontmatter: `title`, `date` (YYYY-MM-DD), optional `tags`, `aliases`.
- Links: Internal `[[file]]` or `[[text|file]]`; external standard Markdown.
- Images: Relative paths under `content/static/` or article directories.
- Drafts: Mark incomplete content with `> [!warning] 草稿`.

## Site Directory

`content/站点目录.md` is the navigation root. Update it when the structure changes.

Current nav:
```
主页 [[content/index]]

## 创作
- [[projects/README|项目列表]]
- [[笔记列表|笔记列表]]
- [[出版作品|出版作品]]

## 收藏
- [[收藏夹|收藏夹]]

## 关于站点
- [[Meta wiki]]
- [[Code Of Conduct 行为守则]]
- [[测试页面]]
- [[关于我]]
- [[FAQ 常见问题]]
```

## Agent Rules

- Do not modify build config outside `content/` unless explicitly requested.
- Do not delete unarchived `content/collect/` files.
- When moving files, check all Wikilinks and update references.
- If `00.inbox/` is empty, re-enter content from `content/` into the workflow loop.
- After organizing content, update the status column in the structure table.
- Preserve Obsidian Vault compatibility: filenames, directories, and links must work in Obsidian.
