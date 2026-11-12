"""Deterministic checks for a static, non-released project presentation.

This is NOT a privacy audit, medical-device assessment, or legal approval.
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

REQUIRED = (
    "README.md", "SECURITY.md", "SICHERHEIT.md", "CONTRIBUTING.md",
    "MITMACHEN.md", "RECHTLICHES_VOR_LIVEGANG.md",
    "AGENTENVERBUND.md", "agent_coordination/QUEUE.md", "index.html",
    "RELEASE_STATUS.md", ".github/CODEOWNERS",
)
REQUIRED_PHRASES = (
    "noch keine öffentlich freigegebene", "kein Notrufdienst",
    "keine zugelassene Digitale Pflegeanwendung",
    "Vor öffentlichem Website-Betrieb",
)
PROHIBITED_TAGS = {"script", "iframe", "object", "embed", "form"}
RESOURCE_ATTRS = {
    "img": ("src", "srcset"), "link": ("href",),
    "audio": ("src",), "video": ("src", "poster"),
    "source": ("src", "srcset"), "track": ("src",),
}
EXTERNAL = re.compile(r"(?i)^\s*(?:https?:|wss?:)?//")
CSS_EXTERNAL = re.compile(r"(?is)@import\s+|url\(\s*['\"]?\s*(?:https?:)?//")
PLACEHOLDERS = re.compile(r"\b(?:Max Mustermann|Musterstra(?:ss|ß)e|platzhalter@)\b", re.I)


class StaticSiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.errors: list[str] = []
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_map = dict(attrs)
        if tag in PROHIBITED_TAGS:
            self.errors.append(f"Prohibited active tag <{tag}>")
        if tag == "meta" and attrs_map.get("http-equiv", "").lower() == "refresh":
            self.errors.append("Meta refresh is not allowed")
        for key, value in attrs:
            if key.startswith("on"):
                self.errors.append(f"Inline event handler {key} not allowed")
            if key == "style" and value and CSS_EXTERNAL.search(value):
                self.errors.append("CSS @import or external URL in inline style")
        if tag in RESOURCE_ATTRS:
            for key in RESOURCE_ATTRS[tag]:
                value = attrs_map.get(key, "") or ""
                if EXTERNAL.match(value) or "javascript:" in value.lower():
                    self.errors.append(f"External/active resource <{tag} {key}> not allowed")
        if tag == "a":
            href = attrs_map.get("href", "") or ""
            if href.lower().startswith("javascript:"):
                self.errors.append("javascript: link not allowed")
            elif href and not (href.startswith("#") or href.startswith("/") or urlsplit(href).scheme):
                self.links.append(href.split("#")[0].split("?")[0])


def check(root: Path) -> list[str]:
    errors: list[str] = []
    for name in REQUIRED:
        target = root / name
        if not target.is_file() or target.stat().st_size == 0:
            errors.append(f"Missing or empty required file: {name}")
    index = root / "index.html"
    if not index.is_file():
        return errors
    text = index.read_text(encoding="utf-8")
    parser = StaticSiteParser()
    parser.feed(text)
    parser.close()
    errors.extend(parser.errors)
    if CSS_EXTERNAL.search(text):
        errors.append("CSS @import or potentially external url() found")
    if PLACEHOLDERS.search(text):
        errors.append("Fake example identity found in index.html")
    for phrase in REQUIRED_PHRASES:
        if phrase.casefold() not in text.casefold():
            errors.append(f"Missing project-status phrase in index.html: {phrase}")
    for link in parser.links:
        if link.startswith(".") or link.endswith((".html", ".md")):
            if not (root / link).resolve().is_relative_to(root.resolve()):
                errors.append("Link escapes repository root")
            elif not (root / link).is_file():
                errors.append(f"Broken local link in index.html: {link}")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = check(root)
    for msg in errors:
        print(f"::error::{msg}")
    if errors:
        print(f"FAIL: {len(errors)} deterministic check(s) failed. No legal conclusions.")
        return 1
    print("PASS: Static project-page checks only. NOT a live-release approval.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
