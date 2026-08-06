import glob
import re

from typing import Optional

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
TITLE_RE = re.compile(r"^title:\s*(.+)$", re.MULTILINE)
ORIGIN_RE = re.compile(r"^origin:\s*(.+)$", re.MULTILINE)
DATE_RE = re.compile(r"^date:\s*(.+)$", re.MULTILINE)

def extract_frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    body = text[m.end() :]
    fm = m.group(1)
    return {
        "title": _group(TITLE_RE.search(fm)),
        "date": _group(DATE_RE.search(fm)),
        "origin": _group(ORIGIN_RE.search(fm)),
    }, body

def _group(m: Optional[re.Match]) -> str:
    return m.group(1).strip() if m else ""

def format(title: "", date: "", origin: ""):
    return f'- [{title}]({origin}) **{date}**\n'

def to_list_item(f):
    with open(f, 'r') as file:
        s = file.read()
        meta, body = extract_frontmatter(s)
        return meta

files = glob.glob("content/collect/zhihu/*.md")
filtered_files = list(filter(lambda s: '知乎答案备份' not in s, files))

metas = [to_list_item(item) for item in filtered_files]

with open('list.md', 'w+') as listfile:
    for meta in sorted(metas, key=lambda m: m['date']):
        listfile.write(format(**meta))
