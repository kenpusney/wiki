#!/usr/bin/env python3
"""Convert Zhihu backup files from <qid>-<aid>.md to <question title>.md with HTML→Markdown body."""

from __future__ import annotations

import re
import shutil
import urllib.parse
from pathlib import Path
from typing import Optional

from bs4 import BeautifulSoup

SRC_DIR = Path("content/collect/zhihu")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
TITLE_RE = re.compile(r"^title:\s*(.+)$", re.MULTILINE)
ORIGIN_RE = re.compile(r"^origin:\s*(.+)$", re.MULTILINE)
DATE_RE = re.compile(r"^date:\s*(.+)$", re.MULTILINE)
HEADING_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
ZHIHU_LINK_RE = re.compile(r"^\[知乎链接\]\((.+)\)$", re.MULTILINE)
SEPARATOR_RE = re.compile(r"^-{3,}\s*$", re.MULTILINE)
RICHTEXT_RE = re.compile(r'<span class="RichText ztext CopyrightRichText-richText" itemprop="text">', re.DOTALL)

# Tags whose content should be treated as plain text rather than recursed into.
TEXT_ONLY_TAGS = {"script", "style", "noscript", "figure"}


def safe_filename(title: str) -> str:
    title = title.strip()
    title = title.replace("/", "-").replace("\\", "-")
    # Keep most punctuation including ?!.、；：…
    return title + ".md"


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


def extract_title_from_body(text: str) -> Optional[str]:
    m = HEADING_RE.search(text)
    if m:
        return m.group(1).strip()
    return None


def extract_html(text: str) -> Optional[str]:
    soup = BeautifulSoup(text, "html.parser")
    span = soup.find("span", class_="RichText", attrs={"itemprop": "text"})
    if span:
        return span.decode_contents()
    return None


def convert_node(node) -> str:
    if isinstance(node, str):
        return node

    if getattr(node, "name", None) in TEXT_ONLY_TAGS:
        return node.get_text()

    if not hasattr(node, "name") or node.name is None:
        return node.get_text() if hasattr(node, "get_text") else ""

    tag = node.name.lower()

    if tag == "br":
        return "\n"

    if tag in {"b", "strong"}:
        inner = "".join(convert_node(c) for c in node.children)
        return f"**{inner}**" if inner else ""

    if tag in {"i", "em"}:
        inner = "".join(convert_node(c) for c in node.children)
        return f"*{inner}*" if inner else ""

    if tag == "u":
        inner = "".join(convert_node(c) for c in node.children)
        return f"<u>{inner}</u>" if inner else ""

    if tag == "p":
        parts = [convert_node(c) for c in node.children]
        text = "".join(parts).strip()
        return f"{text}\n\n" if text else ""

    if tag in {"ul", "ol"}:
        items = []
        for li in node.find_all("li", recursive=False):
            items.append(_list_item_to_md(li, ordered=(tag == "ol")))
        return "".join(items)

    if tag == "blockquote":
        inner = _normalize_inline(node).strip()
        quoted = "\n".join(f"> {line}" if line else ">" for line in inner.splitlines())
        return f"{quoted}\n\n"

    if tag == "a":
        href = node.get("href", "")
        href = _fix_zhihu_link(href)
        text = "".join(convert_node(c) for c in node.children).strip()
        if not text:
            text = href
        if href:
            return f"[{text}]({href})"
        return text

    if tag == "img":
        src = node.get("src", "")
        raw_alt = node.get("alt", "") or node.get("data-actualsrc", "") or ""
        if not src:
            return ""
        fixed_src = _fix_zhihu_image(src)
        if fixed_src != src:
            return f"{fixed_src}\n"
        alt = re.sub(r"^\[|]$", "", raw_alt).strip()
        return f"![{alt}]({fixed_src})\n"

    if tag in {"pre"}:
        code = node.find("code")
        if code:
            lang = (code.get("class") or [""])[0].replace("language-", "")
            text = code.get_text()
            return f"```{lang}\n{text}\n```\n\n"
        return f"```\n{node.get_text()}\n```\n\n"

    if tag == "code" and node.parent and node.parent.name != "pre":
        text = node.get_text()
        return f"`{text}`"

    if tag == "div":
        return "".join(convert_node(c) for c in node.children)

    if tag == "span":
        inner = "".join(convert_node(c) for c in node.children)
        # Preserve the visual @user mention text only.
        cls = " ".join(node.get("class", []))
        if "UserLink" in cls and not inner.strip():
            return ""
        return inner

    if tag == "figure":
        # Extract image text if present, otherwise ignore wrapper.
        img = node.find("img")
        if img:
            return convert_node(img)
        return ""

    if tag == "noscript":
        return ""

    if tag == "html" or tag == "body":
        return "".join(convert_node(c) for c in node.children)

    # Default: recurse children.
    return "".join(convert_node(c) for c in node.children)


def _list_item_to_md(li, ordered: bool, prefix: str = "") -> str:
    if li.find("ul", recursive=False) or li.find("ol", recursive=False):
        lines = []
        for child in li.children:
            if getattr(child, "name", None) == "ul":
                for sub in child.find_all("li", recursive=False):
                    lines.append(_list_item_to_md(sub, ordered=False, prefix=prefix + "  "))
            elif getattr(child, "name", None) == "ol":
                idx = 1
                for sub in child.find_all("li", recursive=False):
                    lines.append(_list_item_to_md(sub, ordered=True, prefix=f"{prefix}{idx}. "))
                    idx += 1
            elif getattr(child, "name", None) == "li":
                lines.append(_list_item_to_md(child, ordered=ordered, prefix=prefix))
        return "".join(lines)

    inner = _normalize_inline(li).strip()
    bullet = "- " if not ordered else "1. "
    return f"{prefix}{bullet}{inner}\n\n"


def _normalize_inline(node) -> str:
    parts = []
    for child in node.children:
        if getattr(child, "name", None) == "br":
            parts.append("\n")
        else:
            parts.append(convert_node(child))
    text = "".join(parts)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def normalize_whitespace(text: str) -> str:
    # Zhihu uses <br><br> for paragraph gaps; collapse excessive blank lines.
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n"


def _fix_zhihu_link(href: str) -> str:
    if not href:
        return href
    try:
        parsed = urllib.parse.urlparse(href)
    except Exception:
        return href

    # Convert protocol-relative URLs like //www.zhihu.com/... to https://...
    if parsed.scheme == "" and href.startswith("//"):
        return "https:" + href

    # Unwrap Zhihu external-link redirects.
    if parsed.netloc == "link.zhihu.com" and parsed.path == "/":
        qs = urllib.parse.parse_qs(parsed.query)
        target = qs.get("target", [None])[0]
        if target:
            return target
    return href


def _fix_zhihu_image(src: str) -> str:
    if not src:
        return src
    if "equation?tex=" in src:
        try:
            parsed = urllib.parse.urlparse(src)
            qs = urllib.parse.parse_qs(parsed.query)
            tex = qs.get("tex", [None])[0]
            if tex:
                latex = urllib.parse.unquote(tex)
                return f"$${latex}$$"
        except Exception:
            pass
    return src


def convert_file(path: Path, dry_run: bool = False, backup: bool = True) -> Optional[Path]:
    raw = path.read_text(encoding="utf-8")
    frontmatter, body = extract_frontmatter(raw)
    title = frontmatter.get("title") or extract_title_from_body(body) or path.stem
    origin = frontmatter.get("origin", "")
    date = frontmatter.get("date", "")

    html = extract_html(body)
    if html is None:
        return None

    soup = BeautifulSoup(html, "html.parser")
    markdown_body = convert_node(soup)
    markdown_body = normalize_whitespace(markdown_body)

    out_text = "---\n"
    out_text += f"title: {title}\n"
    if date:
        out_text += f"date: {date}\n"
    if origin:
        out_text += f"origin: {origin}\n"
    out_text += "---\n"
    out_text += f"# {title}\n\n"
    out_text += f"[知乎链接]({origin})\n\n"
    out_text += "---------\n\n"
    out_text += markdown_body

    new_name = safe_filename(title)
    dest = path.with_name(new_name)

    if dry_run:
        print(f"[dry-run] {path.name} -> {dest.name}")
        return dest

    if dest.exists() and dest != path:
        dest_text = dest.read_text(encoding="utf-8")
        # If destination is already in converted format, skip.
        if RICHTEXT_RE.search(dest_text) is None:
            return dest
        raise FileExistsError(f"Target already exists: {dest}")

    # Write converted content first.
    dest.write_text(out_text, encoding="utf-8")

    # Remove the original file if we renamed.
    if dest != path:
        path.unlink()

    return dest


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Convert Zhihu backup answers to title-based Markdown.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing files")
    parser.add_argument("--no-backup", action="store_true", help="Overwrite files in place instead of renaming")
    args = parser.parse_args()

    files = sorted(SRC_DIR.glob("*.md"))
    if not files:
        print(f"No markdown files found in {SRC_DIR}")
        return

    converted = 0
    skipped = 0
    errors = 0
    for path in files:
        if not path.is_file():
            continue
        try:
            dest = convert_file(path, dry_run=args.dry_run, backup=not args.no_backup)
        except Exception as exc:  # pragma: no cover
            print(f"[error] {path.name}: {exc}")
            errors += 1
            continue

        if dest is None:
            skipped += 1
        elif args.dry_run:
            converted += 1
        else:
            converted += 1
            print(f"[ok] {path.name} -> {dest.name}")

    print(f"\nConverted: {converted}, Skipped: {skipped}, Errors: {errors}")
    if args.dry_run:
        print("Dry run only. Remove --dry-run to apply.")


if __name__ == "__main__":
    main()
