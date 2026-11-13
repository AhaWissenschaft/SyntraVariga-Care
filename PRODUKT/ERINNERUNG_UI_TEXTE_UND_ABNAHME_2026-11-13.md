# Care-Demo – verständliche Texte für eine lokale Alltagserinnerung

**Stand:** 13.11.2026 · **Status:** PRODUKTENTWURF, nicht implementiert, nicht mit Nutzern getestet.  
**Zweck:** Konkrete, direkt übernehmbare Oberflächentexte und überprüfbare Abnahme für einen ersten kleinen, nichtmedizinischen Funktionspfad. Dies ist **keine** Weihnachtskampagne.

## Ein Bildschirm, eine Aufgabe

Überschrift: **An etwas erinnern lassen**  
Einleitung: **Trage eine einfache Alltagsaufgabe ein. Wähle eine Uhrzeit.**  
Feldbeschriftung: **Woran möchtest du denken?**  
Beispieltext im Feld: **Pflanzen gießen**  
Zeitfeld: **Wann möchtest du erinnert werden?**  
Primäre Aktion: **Erinnerung speichern**  
Sekundäre Aktion: **Abbrechen**  
Erfolgsrückmeldung: **Erinnerung gespeichert: [Aufgabe], [Uhrzeit].**  
Fehler, leere Aufgabe: **Bitte gib eine Aufgabe ein.**  
Fehler, fehlende Uhrzeit: **Bitte wähle eine Uhrzeit.**  
Aktion für vorhandenen Eintrag: **Erinnerung löschen**  
Löschbestätigung: **Erinnerung gelöscht.**  
Leerer Zustand: **Du hast noch keine Erinnerungen angelegt.**  
Nicht unterstützte Benachrichtigung: **Dieses Gerät kann dich möglicherweise nicht automatisch benachrichtigen. Öffne die App, um deine Erinnerung zu sehen.**

## Wichtige Grenzen im sichtbaren UI

- Keine Aussage wie „Wir erinnern dich garantiert“: Browser, Energiesparmodus und geschlossene App können Benachrichtigungen verhindern.
- Keine Standardbeispiele zu Medikamenten, Dosierungen oder Notfällen.
- Keine Behauptung, dass Daten schon offline oder dauerhaft gespeichert werden, solange Implementierung und Tests fehlen.
- Keine Aufforderung zur Eingabe von Gesundheitsdaten. Für den ersten Demo-Test nur erfundene Alltagsaufgaben verwenden.
- Der Drache darf optional neben einer Hilfe erscheinen; er ist kein medizinischer Assistent.

## Abnahme für Builder und QA

1. **Status zuerst prüfen:** Existiert bereits eine Erinnerungsfunktion? Dann diese Texte am realen UI abgleichen; keine doppelte Implementierung.
2. **Eingabe:** Bei leerer Aufgabe oder fehlender Zeit wird nichts gespeichert; Fehlermeldung steht als Text im UI, nicht nur als Farbe.
3. **Erfolg:** Bei gültiger Beispielaufgabe („Pflanzen gießen“) zeigt die Oberfläche Aufgabe und Uhrzeit korrekt und ohne Doppelanlage an.
4. **Löschen:** Nach „Erinnerung löschen“ ist der Eintrag nicht mehr sichtbar. Falls Persistenz implementiert ist, auch nach Neuladen prüfen.
5. **Bedienung:** Alle Felder besitzen sichtbare Labels, Tastaturfokus ist erkennbar, Schaltflächen sind per Tastatur bedienbar, Rückmeldungen werden für Screenreader sinnvoll angekündigt.
6. **Geräteverhalten:** Ohne Berechtigung für Benachrichtigungen oder bei nicht unterstütztem Browser keine Erfolgsgarantie; konkrete Einschränkung anzeigen.
7. **Datenschutz:** Keine Übertragung an Server/Analytics ohne gesonderte Prüfung; lokale Speicherung nur nach dokumentierter technischer Prüfung.
8. **Nachweis:** Builder dokumentiert Dateipfad, Commit, Browser/Viewport, ausgeführte Tests und tatsächliche Ergebnisse. QA prüft reproduzierbar; ohne Prüfung bleibt die Funktion unfertig.

**Übergabe:** Builder (:51) übernimmt diese Texte nur soweit passend zum tatsächlich vorhandenen Code und implementiert einen kleinen, testbaren Funktionspfad. QA (:13) prüft anschließend die acht Kriterien. Keine neue Queue-Aufgabe: Die vorhandene Queue ist bereits an der Obergrenze.

**Projektquellen:** [README](../README.md), [Roadmap](../ROADMAP.md), [Sicherheit](../SICHERHEIT.md), [Agentenverbund](../AGENTENVERBUND.md).