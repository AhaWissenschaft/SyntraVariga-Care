import tempfile
import unittest
from pathlib import Path
from tools.care_guard import REQUIRED, check


class CareGuardTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in REQUIRED:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("doc", encoding="utf-8")
        self.good = (
            '<!doctype html><html><head><style>body{color:#fff}</style></head>'
            '<body><p>noch keine öffentlich freigegebene</p>'
            '<p>kein Notrufdienst</p><p>keine zugelassene Digitale Pflegeanwendung</p>'
            '<p>Vor öffentlichem Website-Betrieb</p>'
            '<a href="https://github.com/example/test">Source</a></body></html>'
        )
        (self.root / "index.html").write_text(self.good, encoding="utf-8")

    def test_clean_static_page(self):
        self.assertEqual([], check(self.root))

    def test_external_resource_single_quotes(self):
        self.assertTrue(self.bad("<img src='https://example.org/tracker.png'>"))

    def test_protocol_relative_resource(self):
        self.assertTrue(self.bad('<link rel="stylesheet" href="//cdn.example.org/x.css">'))

    def test_multiline_resource(self):
        self.assertTrue(self.bad('<img\n src="https://example.org/x.png">'))

    def test_css_external_url(self):
        self.assertTrue(self.bad('<style>body{background:url(https://example.org/x.png)}</style>'))

    def test_inline_scripts(self):
        self.assertTrue(self.bad("<script>fetch('/data')</script>"))

    def test_iframe(self):
        self.assertTrue(self.bad('<iframe src="/embed"></iframe>'))

    def test_inline_event_handler(self):
        self.assertTrue(self.bad('<button onclick="sendData()">Send</button>'))

    def test_missing_status_notice(self):
        p = self.root / "index.html"
        p.write_text(self.good.replace("kein Notrufdienst", "Notruf"), encoding="utf-8")
        self.assertTrue(check(self.root))

    def test_missing_required_file(self):
        (self.root / "SECURITY.md").unlink()
        self.assertTrue(check(self.root))

    def test_missing_local_link(self):
        self.assertTrue(self.bad('<a href="missing.html">missing</a>'))

    def test_valid_external_hyperlink_allowed(self):
        self.assertEqual([], check(self.root))

    def bad(self, snippet):
        p = self.root / "index.html"
        p.write_text(self.good.replace("</body>", snippet + "</body>"), encoding="utf-8")
        return check(self.root)


if __name__ == "__main__":
    unittest.main()
