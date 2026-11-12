# QA – Zeit-Ticket in großer Schrift (statischer Nachweis)

**Prüfzeit:** 2026-11-12T23:11:50Z = 2026-11-13 00:11:50 Europe/Berlin.  
**Branch / Ausgangscommit:** `main`, [71851cc5857e7a705c1448f474eaee1a9c319554](https://github.com/AhaWissenschaft/SyntraVariga-Care/commit/71851cc5857e7a705c1448f474eaee1a9c319554).  
**Prüfobjekt:** [KAMPAGNE/ZEIT_TICKET_GROSSE_SCHRIFT.html](ZEIT_TICKET_GROSSE_SCHRIFT.html), Git-Blob `78f66a8a0980b7061facff302ca463d08170f561`.

## Tatsächliche Prüfmethode

GitHub-Datei über verbundenen Repository-Lesezugriff abgerufen; anschließend acht **statische JavaScript-Regulärausdrucks-/String-Prüfungen** gegen den vollständigen HTML-Quelltext ausgeführt. Keine Browser-, Drucker-, PDF- oder Screenreader-Ausführung. Die Suche nach externen Ressourcen und APIs ist eine Negativprüfung für bekannte Muster, **keine** umfassende Sicherheitszertifizierung.

| ID | Prüfgegenstand / Muster | Ergebnis |
|---|---|---|
| 1 | `@page {size:A4; margin:14mm}` | BESTANDEN – Druckformat im CSS definiert |
| 2 | `@media print` und `break-inside:avoid` | BESTANDEN – Druckregeln vorhanden, Umbruch nicht visuell geprüft |
| 3 | Keine `script`, `iframe`, `img`, `link`, `form`, `input`, CSS-`@import` oder `url(` | BESTANDEN – keine erkannten eingebetteten Fremdressourcen |
| 4 | Keine `fetch(`, `XMLHttpRequest`, `sendBeacon`, `localStorage`, `sessionStorage`, `document.cookie` | BESTANDEN – keine erkannten Netzwerk-/Speicher-APIs |
| 5 | `Entwicklungsprojekt` und `keine fertige App` | BESTANDEN – Prototyp klar abgegrenzt |
| 6 | `window.print()` und Hinweis `Browsermenü` | BESTANDEN – Schaltfläche plus alternativer Weg vorhanden |
| 7 | Sichtbare Labels `Für:`, `Von:`, `Unser Termin:` und exakt drei `class="blank" aria-hidden="true"` | BESTANDEN – handschriftliche Leerfelder als dekorativ verborgen, keine digitalen Eingaben |
| 8 | Keine bekannten Tracking-Strings `google-analytics`, `gtag(`, `facebook.net`, `pixel.`, `analytics.js` | BESTANDEN – keine erkannten Tracker-Muster |

**Statischer Umfang:** 8/8 = **100 % der hier definierten acht Quelltextkriterien**. Keine Aussage zur vollständigen WCAG-Konformität oder realen Druckqualität.

## Status / Freigabe

- **BESTANDEN:** 8 statische Kriterien am angegebenen Blob.
- **FEHLGESCHLAGEN:** keine der acht statischen Prüfungen.
- **NICHT GEPRÜFT:** echte A4-Druckvorschau und Seitenzahl, Abschneidungen, 200-%-Zoom, Tastatur- und Screenreader-Bedienung, menschliche Lesbarkeitstests, externe Linkverfügbarkeit.
- **BLOCKIERT:** Praktische Accessibility-/Druckfreigabe und Gesamtprodukt-/Website-Freigabe bleiben offen. Keine medizinische Beratung oder Notrufleistung zugesagt.

**Primärquellen und Geltungsbereich (nicht live neu geprüft):** [W3C, WCAG 2.2, Reflow 1.4.10](https://www.w3.org/TR/WCAG22/#reflow) und [W3C, WCAG 2.2, Contrast (Minimum) 1.4.3](https://www.w3.org/TR/WCAG22/#contrast-minimum). Diese Normtexte dienen als Kriterienreferenz; ein statischer CSS-Test belegt **keine** vollständige Normerfüllung. Eigentliche technische Quelle ist der oben genannte öffentliche HTML-Blob.

**Nächster vorhandener Unterauftrag:** CARE-009 (Builder) soll die praktische Druckvorschau und reale Bedienbarkeit beider Ticket-Varianten dokumentieren. Kein neuer Queue-Auftrag, keine zusätzlichen Automationen, keine Ausgaben, keine Änderung am Produkt.
