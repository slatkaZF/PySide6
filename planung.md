# Projektplanung: Wiederverwendbare GUI-Vorlage mit PySide6

## Zielsetzung

Ziel dieses Projekts ist die Entwicklung einer wiederverwendbaren grafischen GUI-Vorlage mit **PySide6**, bestehend aus einer einfachen Benutzeroberfläche mit Eingabefeld, Button und Ausgabefeld. Die Oberfläche wird mit **Qt Designer** erstellt, in Python eingebunden und durch ein kommentiertes Bildschirmvideo ergänzt.  
Die Vorlage soll strukturiert aufgebaut sein, dokumentiert werden und sich als Ausgangspunkt für zukünftige Projekte wie z. B. **einen Passwortgenerator oder einen Mini-Rechner** eignen.

---

## Zeitrahmen und Tagesstruktur

Die Projektarbeit erfolgt von **Mittwoch, 16.07.2025 bis Freitag, 18.07.2025**, bei täglichen Arbeitszeiten von **07:00 bis 15:00 Uhr**.  
Die Abgabe der `planung.md` ist am **Mittwoch bis spätestens 13:00 Uhr** vorgesehen. Der Zeitplan ist so aufgebaut, dass pro Tag 6–7 Stunden produktive Arbeit unter Berücksichtigung von Pausen realistisch geplant werden können.

---

## Meilensteine und Fristen

| **Meilenstein**             | **Beschreibung**                                                            | **Frist**                            |
|----------------------------|-----------------------------------------------------------------------------|--------------------------------------|
| Projektplanung abschließen | `planung.md` finalisieren und abgeben                                       | Mittwoch, 16.07.2025, bis 13:00 Uhr  |
| GUI-Design                 | GUI mit Qt Designer erstellen und `.ui`-Datei speichern                      | Mittwoch, 16.07.2025, bis 15:00 Uhr  |
| Code-Implementierung       | Python-Projektstruktur aufsetzen, `.ui` laden, Logik implementieren         | Donnerstag, 17.07.2025, bis 14:00 Uhr |
| Dokumentation              | `README.md` schreiben und Projektstruktur erläutern                         | Donnerstag, 17.07.2025, bis 15:00 Uhr |
| Bildschirm-Video           | Projekt demonstrieren, aufnehmen und kommentieren                            | Freitag, 18.07.2025, bis 13:00 Uhr    |
| Finalisierung & Abgabe     | Letzte Tests, ZIP-Erstellung, Upload                                         | Freitag, 18.07.2025, bis 15:00 Uhr    |

---

## Geplante Teillaufzeiten

| **Teilaufgabe**                         | **Zeitaufwand (geschätzt)**    | **Geplanter Zeitraum**                                |
|----------------------------------------|-------------------------------|--------------------------------------------------------|
| Projektplanung                          | 1–2 Std.                      | Mittwochvormittag, 16.07., bis 13:00 Uhr               |
| GUI-Design (Qt Designer)                | 1–2 Std.                      | Mittwochnachmittag, 16.07.                             |
| Code-Implementierung (`main.py`, `controller.py`) | 3–4 Std.                      | Donnerstagvormittag, 17.07.                            |
| Dokumentation (`README.md`)            | 1–1,5 Std.                    | Donnerstagnachmittag, 17.07.                           |
| Bildschirmaufnahme & Kommentierung     | 1–1,5 Std.                    | Freitagvormittag, 18.07.                               |
| Tests, Debugging & ZIP-Erstellung      | ca. 2 Std.                    | Freitagmittag, 18.07., bis spätestens 15:00 Uhr        |

---

## Werkzeuge

- **Qt Designer** (UI-Erstellung, Aufruf über `pyside6-designer`)
- **Python 3.x mit PySide6**
- **Visual Studio Code** (für Code und Markdown)
- **OBS Studio** (für Bildschirmaufnahmen mit Kommentar)
- **Markdown** (`planung.md`, `README.md`)
- Optional: **Git** (Versionskontrolle)

---

## Erwartete Herausforderungen

| **Bereich**               | **Mögliche Schwierigkeit**                                                   |
|---------------------------|------------------------------------------------------------------------------|
| Qt Designer                | Erste Anwendung, Umgang mit Layouts und Widget-Struktur                     |
| `.ui`-Integration          | Importfehler, Pfadprobleme, dynamisches Laden in `main.py`                  |
| Event-Handling             | Signale/Slots korrekt binden, Fehler bei Button-Funktionen                  |
| Videoaufnahme              | Audioqualität, Nervosität, Tool-Bedienung                                   |
| Zeitmanagement             | Verzögerungen durch Debugging, Lernkurve bei PySide6                        |

---

## Pufferzeiten und Priorisierung

- **20–25 % Pufferzeit** je Phase (z. B. 30 Minuten Reserve bei GUI oder Code)
- **Gesamtpuffer:** ca. 3 Stunden auf drei Tage verteilt
- **Flexibles Verschieben möglich**, z. B. Videoteil von Freitagvormittag auf Nachmittag
- **Prioritäten bei Zeitmangel:**
  1. GUI-Design & Funktionalität
  2. Code-Struktur mit funktionierender Logik
  3. Dokumentation
  4. Video
  5. Bonus-Features nur bei Zeitüberschuss

---

## Erweiterungsideen (Bonus)

Wenn Zeit übrig bleibt, plane ich folgende optionale Features ein:

- **Eingabevalidierung**: nur numerische Eingabe im `QLineEdit`
- **Fehlermeldungen** per `QMessageBox`
- **Tooltip- und Platzhaltertexte**
- **Clear-Button** zum Zurücksetzen aller Felder
- **Dropdown (QComboBox)** mit vordefinierten Optionen
- **Exportfunktion**: Eingabe in `.txt` speichern

---

## Fazit

Dieses Projekt verbindet alle wesentlichen Phasen professioneller GUI-Entwicklung: Planung, Gestaltung, Implementierung, Dokumentation und Präsentation. Die entstehende Vorlage ist technisch klar strukturiert, modular aufgebaut und bietet langfristigen Nutzen für weitere Python-basierte Anwendungen.
