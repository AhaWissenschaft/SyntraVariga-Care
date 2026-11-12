"""Negative tests for the deterministic public-preview gate. No third-party packages."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.care_release_guard import (
    PREVIEW_FILES, check_preview, check_release,
)

SAFE_PAGE = """<!doctype html><html lang="de"><head>
<meta charset="utf-8">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'none'; connect-src 'none'; style-src 'unsafe-inline'; form-action 'none'">
<style>body { color: #fff; }</style></head>
<body><p>kein Notrufdienst; keine zugelassene Digitale Pflegeanwendung.</p>
<p>Es ist noch keine öffentlich freigegebene App verfügbar.</p>
<a href="https://github.com/AhaWissenschaft/SyntraVariga-Care">Repository</a>
</body></html>"""


class ReleaseGuardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in PREVIEW_FILES:
            file = self.root / name
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text("present\n", encoding="utf-8")
        (self.root / "index.html").write_text(SAFE_PAGE, encoding="utf-8")

    def write_page(self, extra: str) -> None:
        (self.root / "index.html").write_text(
            SAFE_PAGE.replace("</body>", extra + "</body>"), encoding="utf-8"
        )

    def test_clean_public_preview(self) -> None:
        self.assertEqual(check_preview(self.root), [])

    def test_missing_csp_is_rejected(self) -> None:
        page = (self.root / "index.html").read_text(encoding="utf-8")
        page = page.replace('http-equiv="Content-Security-Policy"', 'name="deleted-policy"')
        (self.root / "index.html").write_text(page, encoding="utf-8")
        self.assertTrue(check_preview(self.root))

    def test_single_quoted_external_script_is_rejected(self) -> None:
        self.write_page("<script src='https://tracker.example/x.js'></script>")
        self.assertTrue(check_preview(self.root))

    def test_inline_script_is_rejected(self) -> None:
        self.write_page("<script>fetch('https://tracker.example')</script>")
        self.assertTrue(check_preview(self.root))

    def test_css_import_is_rejected(self) -> None:
        self.write_page("<style>@import url(https://tracker.example/a.css);</style>")
        self.assertTrue(check_preview(self.root))

    def test_inline_handlers_are_rejected(self) -> None:
        self.write_page("<img src='x' onerror='alert(1)'>")
        self.assertTrue(check_preview(self.root))

    def test_meta_redirect_is_rejected(self) -> None:
        self.write_page('<meta http-equiv="refresh" content="0;url=https://x.example">')
        self.assertTrue(check_preview(self.root))

    def test_missing_warning_is_rejected(self) -> None:
        self.write_page("")
        (self.root / "index.html").write_text("<html>Preview</html>", encoding="utf-8")
        self.assertTrue(check_preview(self.root))

    def test_release_cannot_pass_without_legal_artifacts(self) -> None:
        problems = check_release(self.root)
        self.assertTrue(any("LICENSE" in p for p in problems))
        self.assertTrue(any("impressum.html" in p for p in problems))
        self.assertTrue(any("datenschutz.html" in p for p in problems))
        self.assertTrue(any("RELEASE_APPROVAL.md" in p for p in problems))

    def test_structural_release_requires_flag_and_links(self) -> None:
        for name in ("LICENSE", "impressum.html", "datenschutz.html"):
            (self.root / name).write_text("NOT A REAL LEGAL DOCUMENT", encoding="utf-8")
        (self.root / "RELEASE_APPROVAL.md").write_text("UNAPPROVED", encoding="utf-8")
        self.assertTrue(check_release(self.root))
        self.write_page('<a href="./impressum.html">Impressum</a>'
                        '<a href="./datenschutz.html">Datenschutz</a>')
        (self.root / "RELEASE_APPROVAL.md").write_text(
            "APPROVED_FOR_PUBLIC_RELEASE: YES", encoding="utf-8"
        )
        # Only structural checks; this test does not claim the fake documents are legal.
        self.assertEqual(check_release(self.root), [])


if __name__ == "__main__":
    unittest.main()
