# CARE-008 – QA des Goldenen Zeit-Tickets (12.11.2026)

**Gegenstand:** [GOLDENES_ZEIT_TICKET.html](GOLDENES_ZEIT_TICKET.html), bei Prüfung Blob-SHA `1c086e966c969ab32849f8ce48211ae0155c6eb5`.

**Prüfart:** ausschließlich statische Quelltextprüfung der öffentlichen GitHub-Datei. **7/7 statische Prüfkriterien bestanden. Kein visueller Browsertest, keine echte PDF-Druckprobe, kein Screenreader- oder Nutzertest.** Der Container konnte die öffentliche Raw-Datei wegen fehlender DNS-Auflösung nicht herunterladen; daher kein belastbarer visueller Ausdrucktest. Ein statischer CSS-Nachweis ist kein Nachweis der Druckbarkeit.

## Reproduzierbare Prüfkriterien und Befunde

| ID | Statische Prüfmethode | Ergebnis |
|---|---|---|
| S1 | Suche nach `<html lang="de">`, Viewport-Meta-Tag und `<title>` | PASS |
| S2 | Suche nach `@page{size:A4; margin:12mm}`, `@media print` und `break-inside:avoid` | PASS: Druck-CSS vorhanden; visuelle Qualität ungeprüft |
| S3 | Suche nach aktiven externen Ressourcen: `<script`, `<img`, `<iframe`, `<link`, CSS `@import` und `url(` | PASS: keine eingebetteten Drittressourcen |
| S4 | Suche nach `<form`, `<input`, `fetch(`, `XMLHttpRequest`, `sendBeacon`, `localStorage`, `document.cookie` | PASS: keine erkannten Formulare oder Datenübertragungen; keine vollständige Datenschutz-Zertifizierung |
| S5 | Exakte Negativabgrenzung `keine App oder Gesundheitsleistung verschenkt` und `kein Gutschein für eine fertiggestellte App, Pflegeberatung oder Notfallleistung` | PASS: Prototyp- und Nicht-Medizin-Claim erkennbar |
| S6 | Suche nach `onclick="window.print()"` | PASS: lokaler Druckaufruf vorhanden; Browserfunktion ungeprüft |
| S7 | Suche nach `@media(max-width:640px)` | PASS: mobiler Breakpoint vorhanden; Layout bei Zoom ungeprüft |

**Grenzen:** Der Link `https://github.com/AhaWissenschaft/SyntraVariga-Care` führt nur bei bewusster Navigation zu GitHub; dies ist keine eingebettete Ressource. Die sichtbaren `Für:`, `Von:`, `Wann:`-Zeilen sind für handschriftliche Einträge vorgesehen. Die leeren `span`-Elemente mit `aria-label` sind für Screenreader nicht zuverlässig als beschriftete Eingabefelder interpretierbar. Kein Beleg für Tastatur-/Screenreader-Eignung oder die Lesbarkeit des tatsächlichen A4-Ausdrucks.

## QA-Entscheidung

**STATISCH PASS / VISUELL UND ACCESSIBILITY OFFEN.** Keine medizinisch kritische Anleitung im Ticket festgestellt. Keine Freigabe für die Gesamt-App, keine Bestätigung vollständiger Barrierefreiheit und kein Website-Livegang. Keine Änderungen am Ticket vorgenommen, weil ein visueller Fix ohne Drucknachweis spekulativ wäre.

**Nächster Schritt für CARE-009 (Builder):** Die HTML-Datei in einem realen Browser öffnen, Druckvorschau auf A4 mit 100 % und 200 % Zoom prüfen, auf ein Blatt drucken/als PDF speichern und Seitenzahl, Abschneidungen, Kontrast und Tastaturbedienung mit reproduzierbaren Ergebnissen dokumentieren. Leere `span[aria-label]` mit einem Screenreader testen und gegebenenfalls durch einfachere, zugängliche handschriftliche Felder ersetzen. Keine menschlichen Nutzertests behaupten, wenn sie nicht stattgefunden haben.

**Unteraufträge:** Keine neuen; CARE-008 bleibt bis zum visuellen Nachweis teilweise offen, CARE-009 ist bereits in der Queue. Zusätzliche Ausgaben: 0 €.
