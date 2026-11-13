# Care-Demo – reproduzierbarer Bedienungstest für CARE-014

**Status:** TESTPROTOKOLL-VORLAGE, noch nicht ausgeführt. **Geltungsbereich:** tatsächlicher Hauptpfad der lokalen Care-Web-Demo; nicht das Goldene Zeit-Ticket. Keine personenbezogenen Daten verwenden.

## Testumgebung vor Beginn eintragen

- Commit der getesteten Demo: `[SHA]`
- Startbefehl und lokale URL: `[Angabe]`
- Browser/Version, Betriebssystem: `[Angabe]`
- Desktop-Viewport und Mobil-Viewport in CSS-Pixeln: `[Angabe]`
- Prüfperson: `intern / extern freiwillig` (keine Namen veröffentlichen)
- Ergebnisstatus je Schritt: **BESTANDEN / FEHLER / NICHT TESTBAR**. „Nicht getestet“ ist niemals „bestanden“.

## Eine reale Aufgabe – ohne medizinische Daten

**Szenario:** „Ich möchte die Hauptfunktion der Care-Demo ohne Maus finden und wieder zur Startansicht zurückkehren.“ Nur wenn die Demo bereits eine Erinnerungsfunktion enthält: mit fiktivem Eintrag „Pflanzen gießen“ zusätzlich Anlegen und Löschen testen. Nicht vorhandene Funktionen nicht als Fehler dieses Navigationstests bewerten; getrennt als „noch nicht implementiert“ notieren.

1. **Tastatur:** Seite neu laden; ausschließlich Tab und Shift+Tab benutzen. Für jedes erreichbare Steuerelement sichtbaren Fokus prüfen; Fokusreihenfolge und unerreichbare Elemente notieren. Enter/Leertaste für die jeweils passende Aktion testen. Erwartung: keine Tastaturfalle, kein unsichtbarer Fokus.
2. **Touch-Ziele:** Auf Mobilansicht jedes interaktive Element des Hauptpfads mit Browser-Entwicklerwerkzeugen vermessen. Erwartung: mindestens 24 × 24 CSS-Pixel oder konkret dokumentierte Ausnahme nach WCAG 2.2 SC 2.5.8; für zentrale Aktionen 44 × 44 CSS-Pixel als Komfortziel. Abstand und Überlappungen notieren.
3. **Zoom:** Desktop-Browser auf 200 % vergrößern. Erwartung: Hauptaufgabe ohne verdeckte Schaltflächen und ohne Verlust von Text oder Funktion abschließbar. Eventuelle horizontale Scrollprobleme dokumentieren.
4. **Rückmeldung:** Jede ausgelöste Aktion auf eine eindeutige sichtbare Rückmeldung prüfen. Fehler dürfen nicht nur farblich angezeigt werden. Falls Screenreader-Test möglich: Browser, Screenreader und Ergebnis nennen; sonst „nicht getestet“.
5. **Datensparsamkeit:** Nur fiktive Testdaten eingeben. Netzwerk-Tab auf unerwartete Übertragungen prüfen, sofern die Demo tatsächlich läuft. Ohne Netzwerkmitschnitt keine Aussage „sendet nichts“ treffen.

## Befund pro Abweichung

`Schritt | Element/Ansicht | Soll | Ist | Screenshot/Datei/Zeile | Schweregrad | Fix-Commit | Retest`

**Abnahme CARE-014:** Alle Elemente des geprüften Hauptpfads mit tatsächlichen Messwerten oder belegten Ausnahmen dokumentiert; Tastatur, Fokus, 200-%-Zoom und die Hauptaktion auf mindestens einem Desktop-Browser geprüft. Mobilmessung dokumentiert. Jeder Fix erhält Commit und erneuten Test. Ein bestandener interner Test ist noch kein Nutzertest mit älteren Menschen.

**Übergabe:** Builder (:51) trägt echte Messwerte ein und behebt die erste reproduzierbare Abweichung direkt am Demo-Code. QA (:13) prüft Fix und Gegenprobe. Kein neuer Queue-Auftrag nötig; siehe [CARE-014](../agent_coordination/QUEUE.md).

**Normative Quellen:** [WCAG 2.2 – Target Size (Minimum) 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum), [Focus Visible 2.4.7](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible), [Resize Text 1.4.4](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html).
