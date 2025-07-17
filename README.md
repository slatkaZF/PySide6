# PySide6

venv.
benutzen für Abkapselung, 
python -m venv .venv 

(BEI PDF: Keine emotes benutzen, pdf importiert diese nicht richtig)
.ui Datei in .py datei umwandeln, Klasse diese in main.py erzeugen als Objekt 


Arbeite in deiner venv (aktiviere mit venv\Scripts\activate).
Nutze Qt Designer für Design-Änderungen.
Nach jeder Änderung: Speichere main.ui, wandle um mit pyside6-uic main.ui -o gui.py, teste mit python controller.py.
Optische Verbesserungen: Wir fügen Spacer hinzu (für Abstände), ändern Fonts/Farben und verwenden Stylesheets.
Struktur-Ziel: Trenne UI (Design), Logik (Controller) und Start (main.py) für Wiederverwendbarkeit.

# GUI-Vorlage mit PySide6

## Ziel und Funktionsweise
Das Projekt ist eine wiederverwendbare grafische Benutzeroberfläche (GUI) mit PySide6. Es enthält ein Eingabefeld für mathematische Ausdrücke (z. B. "6+6"), einen Button "Berechnen", der die Berechnung auslöst, und ein Ausgabefeld für das Ergebnis (z. B. "Ergebnis: 12"). Die Funktion in `controller.py` verwendet `eval()` zur Auswertung, mit Fehlerbehandlung für ungültige Eingaben.

## Anleitung zum Starten
1. Navigiere in die Kommandozeile zum Projektordner.
2. Aktiviere die virtuelle Umgebung: `venv\Scripts\activate`.
3. Starte die GUI: `python controller.py`.
4. Gib einen Ausdruck ein, klicke "Berechnen" – siehe Ergebnis.

## Beschreibung der Dateien
- `main.ui`: Das GUI-Design, erstellt mit Qt Designer.
- `gui.py`: Generierter Python-Code aus der .ui-Datei (mit `pyside6-uic`).
- `controller.py`: Enthält die Logik, verbindet Widgets und die Berechnungsfunktion.
- `README.md`: Diese Dokumentation.
- `planung.md`: Meine Planung und Reflexion (siehe unten).
- `praesentation.mp4`: Das Bildschirmvideo.

## Reflexion zu Problemen und Lösungen
- Problem: Layout anwenden war schwierig (Widgets auswählen). Lösung: Strg+A verwendet.
- Problem: Button-Funktion hat nicht funktioniert. Lösung: Widget-Namen angepasst und `eval()` hinzugefügt.
- Problem: Umwandlung von .ui zu .py fehlgeschlagen. Lösung: PySide6 neu installiert und Pfade korrigiert.
- Gesamt: Das Projekt hat mir geholfen, Qt Designer und PySide6 zu lernen. Zeitaufwand: Ca. 5 Stunden.
