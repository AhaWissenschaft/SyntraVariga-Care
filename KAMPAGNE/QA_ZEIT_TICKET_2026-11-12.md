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


## Nachtrag: numerische Kontrastprüfung (2026-11-12T22:08:36.078Z)

**Prüfstand:** Branch `main`, Ausgangscommit [`530d75e913ac`](https://github.com/AhaWissenschaft/SyntraVariga-Care/commit/530d75e913aca83132f648c78d7202bbcff7cf66); Datei `KAMPAGNE/GOLDENES_ZEIT_TICKET.html`, Git-Blob `1c086e966c969ab32849f8ce48211ae0155c6eb5`. Prüfzeitpunkt: 2026-11-12T22:08:36.078Z (UTC).

**Methode:** Quelltext über öffentlichen GitHub-Dateizugriff gelesen; CSS-Farbwerte statisch extrahiert. Mit JavaScript die sRGB-Kanäle auf 0–1 normiert, nach WCAG linearisiert (bei c ≤ 0,04045: c/12,92; sonst ((c+0,055)/1,055)^2,4), relative Luminanz L = 0,2126R + 0,7152G + 0,0722B und Kontrast (Lmax+0,05)/(Lmin+0,05) berechnet. Mindestgrenzen: normaler Text 4,5:1 (AA), große Schrift 3:1 (AA). Berechnete statische Farbpaarungen:

| Geprüfte CSS-Farbpaarung | Kontrast | AA-Schwelle | Ergebnis |
|---|---:|---:|---|
| Ticket Haupttext #ffffff auf #0c1829 | 17,82:1 | 4,5:1 | BESTANDEN |
| Ticket Kleintext #e2eaf0 auf #0c1829 | 14,65:1 | 4,5:1 | BESTANDEN |
| Ticket Titel #ffdd8b auf #0c1829 | 13,55:1 | 3:1 | BESTANDEN |
| Druck Haupttext #111111 auf #ffffff | 18,88:1 | 4,5:1 | BESTANDEN |
| Druck Kleintext #333333 auf #ffffff | 12,63:1 | 4,5:1 | BESTANDEN |
| Druck Titel #664a0b auf #ffffff | 8,24:1 | 3:1 | BESTANDEN |
| Seitentext #3e4751 auf #f4f1e9 | 8,36:1 | 4,5:1 | BESTANDEN |

**Ergebnis:** 7/7 = 100 % der **ausgewählten statischen CSS-Farbpaarungen** bestehen die genannten rechnerischen WCAG-AA-Kontrastgrenzen. Das ist **keine** Aussage über alle Farbkombinationen, Bild-/Symbolkontrast, tatsächliche Bildschirmdarstellung oder allgemeine Barrierefreiheit. Außerdem per Quelltext-Suche erneut bestätigt: A4-/Print-CSS vorhanden; keine eingebetteten aktiven Fremdressourcen oder Formulare erkannt. Keine neue medizinische Funktionszusage entdeckt.

**NICHT GEPRÜFT:** tatsächliche Browser-Druckvorschau, Druckseitenzahl, Seitenumbrüche, 200-%-Zoom, Tastatur-/Screenreader-Verhalten, reale Bedienperson. Drei leere `span[aria-label]`-Felder bleiben ein Zugänglichkeitsrisiko; CARE-009 bleibt zuständig. **BLOCKIERT:** praktische Druck-/Nutzerfreigabe mangels nachgewiesenem Realtest. Keine rechtliche oder medizinische Freigabe, kein Website-Livegang.

**Primärquelle:** W3C, *Web Content Accessibility Guidelines (WCAG) 2.2*, Erfolgskriterien [1.4.3 Contrast (Minimum)](https://www.w3.org/TR/WCAG22/#contrast-minimum) und [Understanding Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), Spezifikation WCAG 2.2, abgerufen 2026-11-12; externer Seiteninhalt in diesem Lauf nicht erneut abgerufen, daher keine neue Aussage zu jüngsten Änderungen der Quelle. Reproduzierbar anhand des oben genannten Datei-Blobs und der angegebenen Formeln. Keine Änderungen am Ticket.


## Nachprüfung des Builder-Fixes – 2026-11-13T00:09:19.486Z

**Prüfzeit:** 2026-11-13T00:09:19.486Z UTC (Europe/Berlin: 13.11.2026, ca. 01:09 Uhr).  
**Branch / Ausgangscommit:** `main`, [f28ff1c758169cf2f22f96821deef92b5f0fd38a](https://github.com/AhaWissenschaft/SyntraVariga-Care/commit/f28ff1c758169cf2f22f96821deef92b5f0fd38a).  
**Prüfdatei:** [GOLDENES_ZEIT_TICKET.html](GOLDENES_ZEIT_TICKET.html), Git-Blob `a7d0c936c368e55a86c394f54d82894bc6b5cd2e`.  
**Methode:** Vollständigen HTML-Quelltext über GitHub-Dateizugriff von `main` gelesen und acht JavaScript-String-/Regulärausdruck-Prädikate auf den tatsächlichen Inhalt angewandt (kein Browserlauf, keine Browser-Druckvorschau). Die Ergebnisse beziehen sich ausschließlich auf diesen Blob.

| Statisches Kriterium | Nachweis / Suchmuster | Ergebnis |
|---|---|---|
| 3 sichtbare Feldbeschriftungen | `<strong>Für:</strong>`, `<strong>Von:</strong>`, `<strong>Wann:</strong>` | BESTANDEN |
| 3 dekorative handschriftliche Linien | exakt 3 × `<span class="line" aria-hidden="true"></span>` | BESTANDEN |
| Alte problematische ARIA-Beschriftung beseitigt | kein `span[aria-label]` | BESTANDEN |
| Kein digitales Formular | keine `form/input/textarea/select`-Tags | BESTANDEN |
| Keine bekannten eingebetteten Fremdressourcen | keine `script/iframe/img/link`-Tags, kein CSS-`@import` oder `url(` | BESTANDEN |
| Druckregeln vorhanden | `@page{size:A4; margin:12mm}`, `@media print`, `break-inside:avoid` | BESTANDEN |
| Prototyp und Gesundheitsleistung abgegrenzt | „noch in Entwicklung“, „keine App oder Gesundheitsleistung“ | BESTANDEN |
| Keine bekannten Netzwerk-/Speicher-APIs | kein `fetch`, `XMLHttpRequest`, `sendBeacon`, `localStorage`, `sessionStorage`, `document.cookie` | BESTANDEN |

**Ergebnis:** BESTANDEN **8/8 = 100 % der hier definierten statischen Einzelprüfungen**; FEHLGESCHLAGEN 0/8. Der frühere Hinweis in diesem Bericht zu drei `span[aria-label]` ist ein **historischer Befund am älteren Blob** und für den oben genannten neuen Stand nicht mehr zutreffend. Der Fix ist anhand des GitHub-Commits und des Quelltexts nachvollziehbar.

**NICHT GEPRÜFT:** echte A4-Druckseitenzahl, tatsächliche Zeilenumbrüche und Abschneidungen, 200-%-Zoom, Tastatur-/Screenreader-Ausgabe, reale Bedienperson, Browserkompatibilität, vollständige Sicherheit und WCAG-Konformität. **BLOCKIERT:** Praktische Freigabe beider Tickets und Website-/Produktfreigabe; CARE-009 bleibt als bestehender Builder-Auftrag zuständig. Keine neuen Queue-Aufträge.

**Primärquellen (Stand/Abruf):** [W3C, Web Content Accessibility Guidelines (WCAG) 2.2, 1.1.1 Non-text Content](https://www.w3.org/TR/WCAG22/#non-text-content), [W3C, 1.3.1 Info and Relationships](https://www.w3.org/TR/WCAG22/#info-and-relationships) und [W3C, 1.4.10 Reflow](https://www.w3.org/TR/WCAG22/#reflow). Technische Normreferenzen; externer Normtext in diesem Lauf nicht neu abgerufen und deshalb Aktualitätsstand **NICHT VERIFIZIERT**. Der überprüfte Projektquelltext und Builder-Commit sind oben direkt verlinkt. Die sichtbaren Beschriftungen sind eine plausible Verbesserung, kein realer Screenreader-Nachweis.

**Ausgaben:** 0 € zusätzlich. Keine neue Automation, kein Social-Post, keine GitHub Pages-Aktivierung.
