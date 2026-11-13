# Care-Demo – Testkarte: Was passiert mit meiner Erinnerung?

**Status:** direkt nutzbare manuelle Testanleitung, **noch nicht ausgeführt**. Bezug: [lokale Alltagserinnerung](ALLTAGSERINNERUNG_LOKAL.html) (gelesener Blob `004266425ba36a94ea3adf23eb1260992bffaf96`). Keine medizinischen Daten und keine echte Terminplanung verwenden.

## Für eine freiwillige Testperson – einfache Sprache

Öffne die HTML-Datei `PRODUKT/ALLTAGSERINNERUNG_LOKAL.html` lokal in einem Browser. Die Demo ist noch keine fertige App. Sie zeigt Erinnerungen nur während der geöffneten Sitzung; beim Neuladen verschwinden sie. Benutze sie nicht für wichtige Termine.

1. Trage unter **„Woran möchtest du denken?“** den erfundenen Text **„Pflanzen gießen“** ein.
2. Wähle eine Uhrzeit **zwei Minuten in der Zukunft**. Klicke auf **„Für diese Sitzung hinzufügen“**. Erwartung: Eintrag mit Uhrzeit erscheint unter **„Meine Erinnerungen“**.
3. Lasse den Tab geöffnet und sichtbar, bis die Uhrzeit vorbei ist. Erwartung: Ein Hinweis erscheint, möglicherweise bis zu etwa 15 Sekunden verspätet. **Nicht garantiert**, etwa bei Hintergrundbetrieb.
4. Klicke beim Eintrag auf **„Erinnerung löschen“**. Erwartung: Eintrag verschwindet; **„Erinnerung gelöscht.“** erscheint.
5. Lege erneut „Pflanzen gießen“ an und lade die Seite neu. Erwartung: Die Liste ist leer. **Das ist bei dieser Demo beabsichtigt, kein Speicherfehler.**
6. Wiederhole Schritt 1 mit leerem Aufgabenfeld. Erwartung: **„Bitte gib eine Aufgabe ein.“**; kein neuer Eintrag.

**Freiwillige Rückmeldung (ohne persönliche Daten):** Welche Beschriftung war unverständlich? Konntest du den Eintrag selbstständig anlegen und löschen? War klar, dass nach Neuladen alles weg ist? Bitte nur allgemeine Beobachtungen, keine Namen, Diagnosen, Termine oder Gesundheitsinformationen in GitHub-Issues schreiben.

## Für Builder und QA – überprüfbare Abnahme

- Teste mit erfundenen Daten in einem benannten Browser; dokumentiere Browser-Version, Demo-Commit, Testzeit und Ergebnis je Schritt als **BESTANDEN / FEHLER / NICHT GETESTET**.
- Bei Schritt 3 ist der Timer im Quellcode auf 15 Sekunden eingestellt; Hintergrund-Tabs können stärker verzögern. Keine Garantie oder Betriebssystem-Benachrichtigung behaupten.
- Prüfe zusätzlich mit Tastatur: Tab zu den Feldern, Eingabe, Enter zum Hinzufügen und Tab/Enter zum Löschen. Sichtbare Rückmeldungen müssen erhalten bleiben.
- Wenn der Tab geschlossen oder die Seite neu geladen wird, sind Einträge erwartungsgemäß verloren. Eine dauerhafte Speicherung ist **nicht implementiert**.
- Bei Abweichung: konkreter Reproduktionsschritt, Ist/Soll, Fix-Commit und Retest. Bestehenden Auftrag [CARE-014](../agent_coordination/QUEUE.md) für Tastatur und Zugänglichkeit verwenden; keine neue Queue-Aufgabe anlegen.

**Übergabe:** Builder führt zuerst die sechs Schritte an der realen Demo aus und korrigiert den ersten reproduzierbaren UI-Fehler. QA prüft danach denselben Ablauf unabhängig. Diese Testkarte ist keine Bestätigung eines erfolgreichen Browser- oder Nutzertests.
