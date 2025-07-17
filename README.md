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

Wetter-App mit PySide6
Ziel und Funktionsweise des Projekts
Diese Anwendung ist eine wiederverwendbare GUI-Vorlage basierend auf PySide6, die als Bonusaufgabe eine einfache Wetter-App mit API-Integration implementiert. Das Ziel ist es, eine modulare, erweiterbare Struktur zu schaffen, die für zukünftige Projekte (z. B. BMI-Rechner oder ToDo-Liste) wiederverwendet werden kann. Die App ermöglicht die Eingabe einer Stadt und holt aktuelle Wetterdaten (Temperatur, Beschreibung, Luftfeuchtigkeit) von der OpenWeatherMap API ab. Die Daten werden in einer grafischen Oberfläche angezeigt, die mit rosa Farben, einem Farbverlauf und einer klaren Schriftart (Arial) gestaltet ist. Die GUI ist symmetrisch und mittig ausgerichtet für bessere Lesbarkeit und Ästhetik.

Die Funktionsweise:

Der Benutzer gibt eine Stadt in ein Eingabefeld ein.
Beim Klicken auf "Wetter abrufen" wird eine API-Anfrage gesendet.
Die Ergebnisse werden in Labels aktualisiert, mit Fehlerbehandlung (z. B. für ungültige Städte oder Netzwerkprobleme).
Die App ist modular: UI-Design in .ui-Datei (Qt Designer), Logik in controller.py, Start in main.py.
Anleitung zum Starten
Voraussetzungen installieren:
Stelle sicher, dass Python (empfohlen: 3.11) installiert ist.
Erstelle eine virtuelle Umgebung (optional, aber empfohlen): python -m venv .venv und aktiviere sie mit .\.venv\Scripts\activate.
Installiere Abhängigkeiten aus requirements.txt: pip install -r requirements.txt (enthält PySide6 und requests).
API-Key einrichten:
Registriere dich bei OpenWeatherMap und hole einen kostenlosen API-Key.
Füge ihn in src/controller.py ein (ersetze "DEIN_API_KEY_HIER_EINFUEGEN").
App starten:
Navigiere zum Projektordner: cd C:\Users\Serka\Desktop\Projektwoche.
Führe aus: python src/main.py.
Die GUI öffnet sich. Gib eine Stadt ein (z. B. "Berlin") und klicke "Wetter abrufen".
Hinweis: Wenn Änderungen am Design vorgenommen werden, öffne ui/weather_app.ui in Qt Designer (pyside6-designer), speichere und konvertiere mit pyside6-uic ui/weather_app.ui -o src/ui_weather_app.py.

Beschreibung der Dateien und deren Funktion
/ui/weather_app.ui: Die Qt Designer-Datei mit dem GUI-Design (Widgets wie Eingabefeld, Button und Labels). Enthält rosa Farben, Farbverlauf (im Code ergänzt), Arial-Schrift und symmetrisches Layout mit Spacern für Mittenausrichtung.
/src/ui_weather_app.py: Generierte Python-Datei aus der .ui-Datei (mittels pyside6-uic). Definiert die UI-Struktur und wird in main.py importiert. Nicht manuell bearbeiten!
/src/main.py: Hauptskript zum Starten der App. Lädt die UI, verbindet den Button mit der Logik und setzt zusätzliche Styles (z. B. Farbverlauf für den Hintergrund).
/src/controller.py: Enthält die App-Logik, inklusive API-Aufruf zu OpenWeatherMap, Datenverarbeitung und GUI-Updates. Handhabt Fehler mit QMessageBox.
/docs/README.md: Diese Dokumentation.
/docs/planung.md: Planungsdokument (optional, für deine Projektplanung).
/media/demo_video.mp4: Bildschirm-Video mit Vorstellung der GUI, Code-Erklärung und Demo (4-6 Minuten, mit Stimme).
requirements.txt: Liste der Abhängigkeiten (PySide6, requests).
Ordnerstruktur:

text

Einklappen

Zeilenumbruch

Kopieren
/projektwoche
├── /ui              # GUI-Design-Dateien
├── /src             # Python-Quellcode
├── /docs            # Dokumentation
├── /media           # Video
└── requirements.txt # Abhängigkeiten
Reflexion zu Problemen und Lösungen
Probleme:

OCR-Fehler im Original-Dokument: Das PDF hatte viele Tippfehler (z. B. "zu, $0$ zu"), was die Anforderungen unklar machte.
Design-Herausforderungen: Ursprüngliche Farben waren zu intensiv (schlechte Lesbarkeit), Schrift zu klein, Layout nicht symmetrisch/mittig.
Konvertierungsfehler: "Could not create output file" bei pyside6-uic durch falschen Ordnerpfad oder fehlende Rechte.
Undo-Probleme: Versehentliche Ruiniation der .ui-Datei durch Experimente.
API-Integration: Ohne Key oder bei Netzwerkfehlern keine Daten; falsche Städte verursachten Fehler.
Lösungen:

Dokument analysiert und Anforderungen extrahiert; schrittweise Anleitung für Klarheit.
Design in Qt Designer angepasst: Mildere Rosa-Töne (#FFD3E0, #FFA7C4), größere Arial-Schrift (14-16px), Spacer für Symmetrie/Mittenausrichtung, weißer Hintergrund für Eingabe. Farbverlauf im Code ergänzt.
Konvertierung: Terminal in /ui wechseln, absoluten Pfad verwenden, PySide6 neu installieren. Administrator-Modus für Rechte.
Undo: Undo in Qt Designer (Strg+Z), Backups empfohlen (z. B. via Git oder Kopien). Neuaufbau der .ui als Fallback.
API: Fehlerbehandlung mit QMessageBox implementiert; Key-Anleitung hinzugefügt. Tests mit Städten wie "Berlin" für Validierung.
Das Projekt ist nun robust und erweiterbar. Frühe Fertigstellung ermöglichte die Bonusaufgabe (Wetter-App).

# Wetter-App mit PySide6

## Ziel und Funktionsweise des Projekts
Diese Anwendung ist eine wiederverwendbare GUI-Vorlage basierend auf PySide6, die als Bonusaufgabe eine einfache Wetter-App mit API-Integration implementiert. Das Ziel ist es, eine modulare, erweiterbare Struktur zu schaffen, die für zukünftige Projekte (z. B. BMI-Rechner oder ToDo-Liste) wiederverwendet werden kann. Die App ermöglicht die Eingabe einer Stadt und holt aktuelle Wetterdaten (Temperatur, Beschreibung, Luftfeuchtigkeit) von der OpenWeatherMap API ab. Die Daten werden in einer grafischen Oberfläche angezeigt, die mit rosa Farben, einem Farbverlauf und einer klaren Schriftart (Arial) gestaltet ist. Die GUI ist symmetrisch und mittig ausgerichtet für bessere Lesbarkeit und Ästhetik.

Die Funktionsweise:
- Der Benutzer gibt eine Stadt in ein Eingabefeld ein.
- Beim Klicken auf "Wetter abrufen" wird eine API-Anfrage gesendet.
- Die Ergebnisse werden in Labels aktualisiert, mit Fehlerbehandlung (z. B. für ungültige Städte oder Netzwerkprobleme).
- Die App ist modular: UI-Design in `.ui`-Datei (Qt Designer), Logik in `controller.py`, Start in `main.py`.

## Anleitung zum Starten
1. **Voraussetzungen installieren**:
   - Stelle sicher, dass Python (empfohlen: 3.11) installiert ist.
   - Erstelle eine virtuelle Umgebung (optional, aber empfohlen): `python -m venv .venv` und aktiviere sie mit `.\.venv\Scripts\activate`.
   - Installiere Abhängigkeiten aus `requirements.txt`: `pip install -r requirements.txt` (enthält PySide6 und requests).
2. **API-Key einrichten**:
   - Registriere dich bei [OpenWeatherMap](https://openweathermap.org/) und hole einen kostenlosen API-Key.
   - Füge ihn in `src/controller.py` ein (ersetze `"DEIN_API_KEY_HIER_EINFUEGEN"`).
3. **App starten**:
   - Navigiere zum Projektordner: `cd C:\Users\Serka\Desktop\Projektwoche`.
   - Führe aus: `python src/main.py`.
   - Die GUI öffnet sich. Gib eine Stadt ein (z. B. "Berlin") und klicke "Wetter abrufen".

**Hinweis**: Wenn Änderungen am Design vorgenommen werden, öffne `ui/weather_app.ui` in Qt Designer (`pyside6-designer`), speichere und konvertiere mit `pyside6-uic ui/weather_app.ui -o src/ui_weather_app.py`.

## Beschreibung der Dateien und deren Funktion
- **/ui/weather_app.ui**: Die Qt Designer-Datei mit dem GUI-Design (Widgets wie Eingabefeld, Button und Labels). Enthält rosa Farben, Farbverlauf (im Code ergänzt), Arial-Schrift und symmetrisches Layout mit Spacern für Mittenausrichtung.
- **/src/ui_weather_app.py**: Generierte Python-Datei aus der .ui-Datei (mittels `pyside6-uic`). Definiert die UI-Struktur und wird in `main.py` importiert. Nicht manuell bearbeiten!
- **/src/main.py**: Hauptskript zum Starten der App. Lädt die UI, verbindet den Button mit der Logik und setzt zusätzliche Styles (z. B. Farbverlauf für den Hintergrund).
- **/src/controller.py**: Enthält die App-Logik, inklusive API-Aufruf zu OpenWeatherMap, Datenverarbeitung und GUI-Updates. Handhabt Fehler mit QMessageBox.
- **/docs/README.md**: Diese Dokumentation.
- **/docs/planung.md**: Planungsdokument (optional, für deine Projektplanung).
- **/media/demo_video.mp4**: Bildschirm-Video mit Vorstellung der GUI, Code-Erklärung und Demo (4-6 Minuten, mit Stimme).
- **requirements.txt**: Liste der Abhängigkeiten (PySide6, requests).

Ordnerstruktur:
```
/projektwoche
├── /ui              # GUI-Design-Dateien
├── /src             # Python-Quellcode
├── /docs            # Dokumentation
├── /media           # Video
└── requirements.txt # Abhängigkeiten
```

## Wichtige Terminal-Befehle
Hier sind alle relevanten Terminal-Befehle, die während der Entwicklung verwendet wurden, inklusive derer zum Umwandeln der `.ui`-Datei in `.py`. Jeder Befehl wird mit Erklärung und Kontext beschrieben. Die Befehle wurden in PowerShell (PS) auf Windows ausgeführt, basierend auf deinem Setup. Führe sie im Projekt-Root-Ordner (`C:\Users\Serka\Desktop\Projektwoche`) aus, es sei denn anders angegeben.

- **Virtuelle Umgebung erstellen und aktivieren** (um Abhängigkeiten isoliert zu installieren):
  ```
  python -m venv .venv
  .\.venv\Scripts\activate
  ```
  - Erklärung: Erstellt eine venv und aktiviert sie. Das vermeidet Konflikte mit globalem Python.

- **Abhängigkeiten installieren** (PySide6 für GUI und requests für API):
  ```
  pip install PySide6
  pip install requests
  ```
  - Oder aus `requirements.txt`:
    ```
    pip install -r requirements.txt
    ```
  - Erklärung: Installiert die benötigten Bibliotheken. Wenn Probleme: `pip uninstall PySide6` und neu installieren.

- **Qt Designer starten** (zum Bearbeiten der .ui-Datei):
  ```
  pyside6-designer
  ```
  - Erklärung: Öffnet Qt Designer. Lade `ui/weather_app.ui` mit "File > Open".

- **.ui-Datei in .py-Datei umwandeln** (Hauptbefehl zum "Umschreiben" des Programms):
  - Wechsle zuerst in den `/ui`-Ordner:
    ```
    cd ui
    ```
  - Dann der Befehl:
    ```
    pyside6-uic weather_app.ui -o ../src/ui_weather_app.py
    ```
  - Alternative mit absolutem Pfad (bei Fehlern wie "Could not create output file"):
    ```
    pyside6-uic C:\Users\Serka\Desktop\Projektwoche\ui\weather_app.ui -o C:\Users\Serka\Desktop\Projektwoche\src\ui_weather_app.py
    ```
  - Erklärung: Konvertiert `weather_app.ui` (Design) in `ui_weather_app.py` (Python-Code). Führe das nach jeder Änderung in Qt Designer aus. `-o` spezifiziert den Output. Wenn Fehler: Stelle sicher, dass `/src` existiert (`mkdir src`), Terminal als Admin ausführen oder Pfad überprüfen.

- **App ausführen** (zum Testen):
  ```
  python src/main.py
  ```
  - Oder mit voller venv-Pfad (wie in deinen Logs):
    ```
    & C:/Users/Serka/Desktop/Projektwoche/.venv/Scripts/python.exe c:/Users/Serka/Desktop/Projektwoche/src/main.py
    ```
  - Erklärung: Startet die App. Wenn Import-Fehler: Überprüfe, ob alle Dateien (z. B. `controller.py`) existieren.

- **Ordner wechseln und Dateien überprüfen** (bei Pfad-Problemen):
  ```
  cd ui  # In /ui gehen
  dir    # Dateien auflisten (suche nach weather_app.ui)
  cd ..  # Zurück zum Root
  ```
  - Erklärung: Hilft, den aktuellen Ordner zu überprüfen und Dateien zu finden.

- **PySide6 überprüfen oder neu installieren** (bei "command not found" oder Modul-Fehlern):
  ```
  pip show PySide6  # Zeigt Installations-Info
  pip uninstall PySide6 && pip install PySide6  # Neu installieren
  ```
  - Erklärung: Überprüft und behebt Installationsprobleme.

Diese Befehle decken die gesamte Entwicklung ab: Installation, Design-Bearbeitung, Konvertierung und Ausführung. Bei Fehlern (z. B. "Could not create output file") war der Grund oft falscher Ordner oder fehlende Rechte – immer in `/ui` ausführen und Pfade prüfen.

## Reflexion zu Problemen und Lösungen
**Probleme:**
- OCR-Fehler im Original-Dokument: Das PDF hatte viele Tippfehler (z. B. "zu, $0$ zu"), was die Anforderungen unklar machte. 
- Design-Herausforderungen: Ursprüngliche Farben waren zu intensiv (schlechte Lesbarkeit), Schrift zu klein, Layout nicht symmetrisch/mittig.
- Konvertierungsfehler: "Could not create output file" bei `pyside6-uic` durch falschen Ordnerpfad oder fehlende Rechte.
- Undo-Probleme: Versehentliche Ruiniation der .ui-Datei durch Experimente.
- API-Integration: Ohne Key oder bei Netzwerkfehlern keine Daten; falsche Städte verursachten Fehler.

**Lösungen:**
- Dokument analysiert und Anforderungen extrahiert; schrittweise Anleitung für Klarheit.
- Design in Qt Designer angepasst: Mildere Rosa-Töne (#FFD3E0, #FFA7C4), größere Arial-Schrift (14-16px), Spacer für Symmetrie/Mittenausrichtung, weißer Hintergrund für Eingabe. Farbverlauf im Code ergänzt.
- Konvertierung: Terminal in /ui wechseln, absoluten Pfad verwenden, PySide6 neu installieren. Administrator-Modus für Rechte.
- Undo: Undo in Qt Designer (Strg+Z), Backups empfohlen (z. B. via Git oder Kopien). Neuaufbau der .ui als Fallback.
- API: Fehlerbehandlung mit QMessageBox implementiert; Key-Anleitung hinzugefügt. Tests mit Städten wie "Berlin" für Validierung.

Das Projekt ist nun robust und erweiterbar. Frühe Fertigstellung ermöglichte die Bonusaufgabe (Wetter-App).
