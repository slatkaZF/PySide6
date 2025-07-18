import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QMovie
from ui_weather_app import Ui_MainWindow
from controller import WeatherController

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.controller = WeatherController(self.ui)
        
        # Verbinde den Button mit der Funktion im Controller
        self.ui.weather_button.clicked.connect(self.controller.get_weather)
        
        # Farbverlauf und Styles
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #FFD3E0, stop: 1 #FFA7C4);
            }
            QPushButton {
                background-color: #FFA7C4;
                color: #FFFFFF;
                border: 2px solid #C2185B;
                padding: 8px;
                border-radius: 8px;
                font-family: Arial;
                font-size: 14px;A
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #C2185B;
            }
            QLineEdit {
                background-color: #FFFFFF;
                color: #C2185B;
                border: 2px solid #FFA7C4;
                border-radius: 5px;
                padding: 5px;
                font-family: Arial;
                font-size: 14px;
            }
            QLabel {
                color: #C2185B;
                font-family: Arial;
                font-size: 16px;
                font-weight: normal;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec())
