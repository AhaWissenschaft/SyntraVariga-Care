#!/usr/bin/env python3
"""Deterministic checks for the static Care preview. No dependencies or network I/O.

This is a narrow risk-reduction measure, not legal clearance or a runtime security audit.
"""
from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re

PREVIEW_FILES = (
    "README.md", "index.html", "SICHERHEIT.md", "MITMACHEN.md",
    "RECHTLICHES_VOR_LIVEGANG.md", "SECURITY.md", "CONTRIBUTING.md",
    ".github/CODEOWNERS", ".github/ISSUE_TEMPLATE/config.yml",
    "docs/LAUNCH_GATES.md",
)
RELEASE_FILES = ("LICENSE", "impressum.html", "datenschutz.html", "RELEASE_APPROVAL.md")
FORBIDDEN_TAGS = {"script", "iframe", "object", "embed", "form", "base"}
REMOTE_URL = re.compile(r"(?i)(?:https?:)?//")
CSS_RESOURCE = re.compile(r"(?i)@import\b|url\s*\(")


class StaticPreviewParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.errors: list[str] = []
        self.in_style = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        if tag in FORBIDDEN_TAGS:
            self.errors.append(f"Forbidden HTML tag: <{tag}>")
        if tag == "style":
            self.in_style = True
        if tag == "meta" and a.get("http-equiv", "").lower() == "refresh":
            self.errors.append("Meta refresh is not permitted")
        for key, value in attrs:
            val = value or ""
            if key.startswith("on"):
                self.errors.append(f"Inline event handler prohibited: {key}")
            if re.search(r"(?i)javascript\s*:", val):
                self.errors.append(f"JavaScript URL prohibited in {key}")
            if key == "style" and CSS_RESOURCE.search(val):
                self.errors.append("CSS url() or @import not permitted in style attributes")
            if key in {"src", "srcset", "poster", "data", "action", "formaction"}:
                self.errors.append(f"Dynamic/resource attribute prohibited: {key}")
            if key == "href" and tag != "a":
                self.errors.append(f"Resource reference prohibited: <{tag} href>")
            if key != "href" and REMOTE_URL.search(val):
                self.errors.append(f"Remote URL prohibited in {key}")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        if tag == "style":
            self.in_style = False

    def handle_data(self, data: str) -> None:
        if self.in_style and CSS_RESOURCE.search(data):
            self.errors.append("CSS url() or @import not permitted in <style>")


def check_preview(root: Path) -> list[str]:
    errors = [f"Missing/empty: {p}" for p in PREVIEW_FILES
              if not (root / p).is_file() or (root / p).stat().st_size == 0]
    page = root / "index.html"
    if not page.is_file():
        return errors
    text = page.read_text(encoding="utf-8")
    parser = StaticPreviewParser()
    parser.feed(text)
    parser.close()
    errors.extend(parser.errors)

    # Protect the existing non-medical, non-emergency positioning.
    for pattern, label in (
        (r"kein\s+Notrufdienst", "no-emergency-service warning"),
        (r"keine\s+zugelassene\s+Digitale\s+Pflegeanwendung", "no-approved-DiPA warning"),
        (r"keine\s+öffentlich\s+freigegebene", "preview-only notice"),
    ):
        if not re.search(pattern, text, re.IGNORECASE):
            errors.append(f"Mandatory preview wording missing: {label}")
    return errors


def check_release(root: Path) -> list[str]:
    errors = check_preview(root)
    errors.extend(f"Release blocked: missing/empty {p}" for p in RELEASE_FILES
                  if not (root / p).is_file() or (root / p).stat().st_size == 0)
    page = root / "index.html"
    if page.is_file():
        text = page.read_text(encoding="utf-8")
        for name in ("impressum.html", "datenschutz.html"):
            if not re.search(r'href\s*=\s*["\'](?:\./)?' + re.escape(name) + r'["\']',
                             text, re.IGNORECASE):
                errors.append(f"Release blocked: missing visible link to {name}")
    approval = root / "RELEASE_APPROVAL.md"
    if approval.is_file() and "APPROVED_FOR_PUBLIC_RELEASE: YES" not in approval.read_text(encoding="utf-8"):
        errors.append("Release blocked: explicit human approval flag missing")
    return errors


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--preview", action="store_true")
    group.add_argument("--release", action="store_true")
    p.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = p.parse_args()
    errors = check_release(args.root) if args.release else check_preview(args.root)
    if errors:
        for problem in errors:
            print(f"FAIL: {problem}")
        return 1
    print("PASS: deterministic preview checks" if args.preview
          else "PASS: structural release checks (NOT legal clearance)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
