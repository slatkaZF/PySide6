from PySide6.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow  # Importiere die generierte UI

class Controller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Verbinde den Button mit der Funktion (passe 'calculateButton' an deinen Namen an)
        self.ui.calculateButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        input_text = self.ui.inputField.text()  # Hole die Eingabe (passe 'inputField' an, falls dein Name anders ist)
        try:
            result = eval(input_text)  # Berechne den mathematischen Ausdruck (z. B. 6+6 -> 12)
            self.ui.outputField.setText(f"Ergebnis: {result}")  # Setze die Ausgabe (passe 'outputField' an)
        except Exception as e:
            self.ui.outputField.setText("Fehler: Ungültige Eingabe!")  # Fehlerbehandlung, z. B. bei Buchstaben

if __name__ == "__main__":
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec()
