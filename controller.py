import requests
from PySide6.QtWidgets import QMessageBox

class WeatherController:
    def __init__(self, ui):
        self.ui = ui
        self.api_key = "1017f01b8e1a6fb569bfd12c4715f5c0" 
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self):
        city = self.ui.city_input.text()
        if not city:
            QMessageBox.warning(None, "Fehler", "Bitte geben Sie eine Stadt ein!")
            return

        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",  
            "lang": "de"       
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()

            # Wetterdaten extrahieren
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]

            
            self.ui.temperature_label.setText(f"Temperatur: {temperature} °C")
            self.ui.description_label.setText(f"Wetter: {description}")
            self.ui.humidity_label.setText(f"Luftfeuchtigkeit: {humidity}%")

        except requests.RequestException as e:
            QMessageBox.critical(None, "Fehler", f"Fehler beim Abrufen der Daten: {e}")
