# Care-Agentenqueue

Nur öffentliche, für die Projektkommunikation geeignete Aufgaben hier erfassen. Keine privaten Ideen oder personenbezogenen Daten.

| ID | Rolle | Ziel | Abnahmekriterium | Status |
|---|---|---|---|---|
| CARE-001 | QA | Prüfe bestehende öffentliche Aussagen auf veraltete oder unbelegte Funktionsversprechen. | Fundstellen und Korrekturvorschläge mit Quellen. | OPEN |
| CARE-002 | Outreach | Entwerfe eine neutrale, zweisprachige Kooperationseinladung für Barrierefreiheits-/Seniorenorganisationen. | [DE/EN-Text veröffentlicht](../KAMPAGNE/KOOPERATIONSEINLADUNG_DE_EN.md), ohne Spenden- oder Heilversprechen; keine externe Kontaktaufnahme. | DONE |
| CARE-003 | Builder | Ergänze eine nachvollziehbare, kurze Projekt-Einstiegsnavigation für Nutzertester. | [Einstiegsanleitung](../TESTEN_EINSTIEG.md) und README-Schnellzugriff veröffentlicht; ausdrücklich kein öffentlicher App-Test. | DONE |
| CARE-004 | QA | Prüfe, welche rechtlichen Pflichtinformationen vor GitHub Pages tatsächlich fehlen. | Prüfliste mit offiziellen Links, keine fingierten Angaben. | OPEN |

| CARE-005 | QA | GitHub-Actions-Fehler vor Merge klären. | Run [43295723127](https://github.com/AhaWissenschaft/SyntraVariga-Care/actions/runs/43295723127): API meldet Job `static-verification` (ID `131453418420`) mit `failure`, aber `steps: null`; Logabruf liefert `404 BlobNotFound`. Ursache damit **nicht nachgewiesen**. Workflow ist read-only, Checkout auf Commit gepinnt, führt `tools/care_guard.py` und Unittests aus. Nächster QA-Schritt: GitHub-UI/Run-Retry auf Job-Startfehler prüfen, anschließend erst PR [#1](https://github.com/AhaWissenschaft/SyntraVariga-Care/pull/1) vergleichen; keinen Blindfix oder Merge. | BLOCKED: LOG UNAVAILABLE |

| CARE-006 | Outreach | Erstelle eine zielgruppenspezifische, kurze organische Bekanntmachung für Senioren- und Angehörigentests, ohne Gesundheitsversprechen. | Veröffentlichungsfertiger Entwurf plus CTA und Quellen-/Prototyp-Hinweis, im Veröffentlichungslog als Entwurf/nicht gesendet gekennzeichnet. | OPEN |

Die Agenten dürfen höchstens zwei neue Unteraufträge pro Lauf eintragen und sollen keine weiteren Automationen erzeugen.
