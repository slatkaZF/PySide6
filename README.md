# Wetter-App mit PySide6

## Ziel und Funktionsweise des Projekts
Das Projekt zielt darauf ab, eine wiederverwendbare grafische Benutzeroberfläche (GUI) mit PySide6 zu entwickeln, die als Vorlage für weitere Anwendungen dient. Als Bonusaufgabe wurde eine Mini-Wetter-App mit API-Integration umgesetzt. Die App ermöglicht die Eingabe einer Stadt und zeigt aktuelle Wetterdaten (Temperatur, Beschreibung, Luftfeuchtigkeit) von der OpenWeatherMap API an. Die GUI ist in einem rosa Design gestaltet, mit einem Farbverlauf, klarer Schriftart (Arial) und symmetrischer Ausrichtung für optimale Lesbarkeit.

Funktionsweise:
- Der Benutzer gibt eine Stadt in das Eingabefeld ein.
- Der Button "Wetter abrufen" löst eine Funktion in `controller.py` aus, die die API abfragt.
- Die Daten werden in Labels aktualisiert.
- Fehlerbehandlung (z. B. ungültige Stadt) wird mit QMessageBox gehandhabt.
- Die `.ui`-Datei wird zur Laufzeit in `.py` konvertiert und geladen.
- Der Code ist kommentiert und sauber strukturiert für Wiederverwendbarkeit.

## Anleitung zum Starten
1. **Voraussetzungen installieren**:
   - Python 3.11 (oder höher) installieren.
   - Virtuelle Umgebung erstellen (optional): `python -m venv .venv` und aktivieren mit `.\.venv\Scripts\activate`.
   - Abhängigkeiten installieren: `pip install PySide6 requests`.
2. **API-Key einrichten**:
   - Registrieren bei [OpenWeatherMap](https://openweathermap.org/) und API-Key holen.
   - In `controller.py` den Key ersetzen (`self.api_key = "DEIN_API_KEY"`).
   - API KEY 1017f01b8e1a6fb569bfd12c4715f5c0
3. **GUI-Design bearbeiten (optional)**:
   - Qt Designer starten: `pyside6-designer`.
   - `ui/weather_app.ui` öffnen, ändern und speichern.
   - Konvertieren: `cd ui` und `pyside6-uic weather_app.ui -o ../src/ui_weather_app.py`.
4. **App starten**:
   - Im Projektordner: `python src/main.py`.
   - Stadt eingeben (z. B. "Schweinfurt") und Button klicken.

## Beschreibung der Dateien und deren Funktion
- **ui/weather_app.ui**: Qt Designer-Datei mit dem GUI-Design (Eingabefeld, Button, Labels). Enthält rosa Farben, Verlauf (im Code), Arial-Schrift und symmetrisches Layout.
- **src/ui_weather_app.py**: Generierte Python-Datei aus `.ui` (mit `pyside6-uic`). Definiert die UI-Struktur, wird in `main.py` importiert. Nicht manuell bearbeiten!
- **src/main.py**: Hauptskript zum Starten der App. Lädt UI, verbindet Button mit Controller und setzt Styles.
- **src/controller.py**: Logik der App: API-Aufruf, Datenverarbeitung und GUI-Updates. Handhabt Fehler.
- **docs/README.md**: Diese Dokumentation.
- **docs/planung.md**: Planung (z. B. PDF-Auszüge).
- **requirements.txt**: Abhängigkeiten (PySide6, requests).

Ordnerstruktur:
```
/projektwoche
├── /ui              # Design-Dateien
├── /src             # Code
├── /docs            # Dokumentation
└── requirements.txt # Abhängigkeiten
```

## Reflexion zu Problemen und Lösungen
Probleme:
- OCR-Fehler im PDF (z. B. "zu, $0$ zu") machten Anforderungen unklar.
- Design: Farben zu intensiv, Schrift zu klein, Layout nicht mittig.
- Konvertierung: "Could not create output file" durch Pfadfehler.
- Code: Import-Fehler, Größenanpassungen.

Lösungen:
- Anforderungen extrahiert und schrittweise umgesetzt.
- Design in Qt Designer angepasst (mildere Rosa, Arial 14-16px, Spacer für Mitte).
- Konvertierung: `cd ui` und absoluter Pfad verwenden, PySide6 neu installieren.
- Code: OOP-Struktur (Klassen, Methoden), Größen in `main.py` gesetzt. Tests mit Städten wie "Schweinfurt".

