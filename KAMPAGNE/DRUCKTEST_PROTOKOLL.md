# Reproduzierbarer Druck- und Lesbarkeitstest – Goldene Zeit-Tickets

**Stand:** 13.11.2026 · **Status:** TESTPLAN, nicht durchgeführt.  
**Auftrag:** CARE-008 (QA) und CARE-009 (Builder). Keine Produktfreigabe.

## Zu prüfende Dateien

- [Goldenes Zeit-Ticket](GOLDENES_ZEIT_TICKET.html)
- [Zeit-Ticket in großer Schrift](ZEIT_TICKET_GROSSE_SCHRIFT.html)

Lade die HTML-Datei jeweils über GitHub **Raw / Download raw file** herunter und öffne sie lokal im Browser. Die GitHub-Codeansicht ist **nicht** der eigentliche Ticketbildschirm. Keine persönlichen Daten in öffentliche Issues oder Screenshots eintragen. Für Tests ausschließlich Fantasienamen verwenden.

## Testprotokoll zum Ausfüllen

Pro Kombination **Datum, Gerät, Betriebssystem, Browser und Version** festhalten. „Nicht getestet“ ist kein bestandenes Ergebnis.

| ID | Handlung | Erwartung | Ergebnis (PASS / FAIL / BLOCKED / NOT TESTED) | Beleg / Fehler |
|---|---|---|---|---|
| T01 | Beide HTML-Dateien lokal ohne Internet öffnen | Text und Layout lesbar, keine Netzverbindung erforderlich | NOT TESTED | – |
| T02 | Smartphone mit ca. 320 px Breite hochkant, dann quer öffnen | Kein horizontal abgeschnittener Inhalt, alle Texte erreichbar | NOT TESTED | – |
| T03 | Browserzoom 200 % und 400 % prüfen | Text nicht abgeschnitten; Umbruch statt Überlagerung | NOT TESTED | – |
| T04 | Mit Tab-Taste zu Drucktaste und Projektlink navigieren | Fokus sichtbar, beide mit Tastatur erreichbar | NOT TESTED | – |
| T05 | Browserdruck A4, 100 % Skalierung, Standardränder | Keine abgeschnittenen Zeilen, alle Ausfülllinien sichtbar | NOT TESTED | – |
| T06 | Drucken mit ausgeschalteten Hintergrundgrafiken | Text und Felder weiterhin kontrastreich lesbar | NOT TESTED | – |
| T07 | Über Browsermenü drucken, ohne JavaScript auszuführen | Ausdruck auch ohne Drucktaste möglich | NOT TESTED | – |
| T08 | Screenreader (z. B. NVDA oder TalkBack) lesen lassen | „Für“, „Von“, „Wann/Unser Termin“ verständlich; dekorative Linien nicht vorgelesen | NOT TESTED | – |
| T09 | Mindestens eine freiwillige ältere Testperson bittet um Erklärung | Verständlichkeit, Dauer und Stolperstellen wortgetreu anonym dokumentieren | NOT TESTED | – |
| T10 | HTML auf Formulare, Tracker, externe Ressourcen und kritische Versprechen prüfen | Keine Formulare/Tracker; keine zugesagte Notfall-, Pflege- oder Medizinleistung | NOT TESTED | – |

## Abnahmeregel

**CARE-008:** Erst schließen, wenn die ausführbaren technischen Tests mit nachvollziehbaren Resultaten dokumentiert sind. Nicht verfügbare Geräte oder Drucker als BLOCKED angeben, niemals als PASS. Sicherheits-/Datenschutzbefunde getrennt protokollieren.

**CARE-009:** Erst schließen, wenn mindestens eine tatsächliche freiwillige Bedienperson getestet hat und das Ergebnis ohne personenbezogene Details vorliegt. Keine fingierten Nutzertests.

**Nicht bestanden:** Reproduktionsschritte, betroffene Datei, Browser und eine minimal sichere Korrektur dokumentieren. Nach Fix betroffene Tests erneut ausführen. Kein öffentlicher App-Livegang, keine pauschale Aussage „barrierefrei“.

**Datenminimierung:** Keine Namen, Kontaktadressen, Gesundheitsangaben, Fotos oder identifizierbare Zitate von Testpersonen in dieses öffentliche Repository übernehmen. Einverständnis für freiwilliges Feedback vorab einholen. Ein Testbericht kann vollständig ohne personenbezogene Angaben erstellt werden.
