# SyntraVariga-Care: Go/No-Go vor einem öffentlichen Website- oder Produktstart

Stand 12.11.2026. Dieses Dokument ist eine **Arbeits- und Prüfliste, keine rechtliche Freigabe**. GitHub als öffentliches Code-Repository ist nicht gleichbedeutend mit einer freigegebenen GitHub-Pages-Website oder einer einsatzbereiten App.

## Technischer Preview-Check

- [ ] `python3 -m unittest discover -s tests -v` erfolgreich; Negativfälle demonstriert.
- [ ] `python3 tools/care_release_guard.py --preview` erfolgreich; statische Landing-Page ohne aktive Skripte, fremde Ressourcen oder Formulare.
- [ ] GitHub Actions mit `contents: read` erfolgreich; keine fremden Caches, keine dynamischen Befehle aus Issues/PRs.
- [ ] GitHub Branch-/Ruleset-Einstellungen verlangen Pull Request, erfolgreiche Checks und Review durch Code Owner. Eine CODEOWNERS-Datei allein erzwingt keine Prüfung.

## Vor öffentlicher Website / Produktfreigabe

- [ ] **Lizenz ausdrücklich entscheiden** (MIT/Apache-2.0/andere/keine); Rechte an betroffenen Bestandteilen und Beiträgen klären. Keine Lizenz ohne ausdrückliche Entscheidung hinzufügen.
- [ ] **Echtes Impressum:** verantwortlichen Anbieter, gegebenenfalls ladungsfähige Anschrift und erforderliche Kontaktdaten prüfen und erst mit ausdrücklicher Veröffentlichungsfreigabe einstellen. Kein Platzhalter als „fertig“ darstellen.
- [ ] **Datenschutzhinweise:** tatsächlichen Hosting-Betrieb, Cookies, Logs, Aufbewahrung, Empfänger, lokale Datenspeicherung und etwaige Zahlungs-/Drittdienste bestimmen. Keine pauschale Zusage „100 % offline“ ohne Verifikation.
- [ ] **Zweckbestimmung / Medizinprodukterecht:** tatsächliche Produktfunktionen, beworbene Verwendung und Nutzerfluss fachlich prüfen. Der Satz „Kein Medizinprodukt“ allein entscheidet keine MDR-Einstufung.
- [ ] **AI-Act-Prüfung:** zutreffende Pflichten nach tatsächlichem KI-Einsatz (etwa direkte KI-Interaktion und generierte Inhalte) prüfen. Keine menschliche Einzelprüfung behaupten, die nicht stattgefunden hat.
- [ ] **Sicherheitsmeldungen:** Private Vulnerability Reporting bei GitHub aktivieren und **aus externer Perspektive** verifizieren; vorher keine private Melderoute behaupten.
- [ ] **Sicherheits- und Barrierefreiheitstests:** reale Gerätetests und passende fachliche Abnahme dokumentieren; keine Notruf-/Diagnosefunktion behaupten.
- [ ] **Deployment-Kopplung:** GitHub Pages deaktiviert lassen, solange die Rechtsangaben fehlen. Bei späterer Veröffentlichung muss der Deployment-Workflow den Release-Guard zwingend als Vorbedingung ausführen; geschütztes `github-pages`-Environment einrichten.
- [ ] `python3 tools/care_release_guard.py --release` erfolgreich **und** die oben genannten menschlichen Prüfungen belegt.

## Grenzen des technischen Guards

Die statische Prüfung erkennt definierte Text- und Ressourcenmuster und prüft die Existenz bestimmter Dokumente. Sie ist **kein vollständiger Security-, DSGVO- oder MDR-Nachweis**. Neue JavaScript-Funktionalität erfordert eine überprüfte, bewusst geänderte Sicherheitsarchitektur und neue Tests.

Offizielle Informationen:
- § 5 DDG: https://www.gesetze-im-internet.de/ddg/__5.html
- BfArM Medizinprodukt-Zweckbestimmung: https://www.bfarm.de/DE/Medizinprodukte/Aufgaben/Feststellung-rechtlicher-Status-und-Klassifizierung/_node.html
- AI Act Artikel 50: https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act
- Private Vulnerability Reporting: https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository
- CODEOWNERS: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
