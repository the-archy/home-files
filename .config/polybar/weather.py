#lol
#Credits: the-archy, Call-Me-Apro, 

from metno_locationforecast import Place, Forecast
import math

class Formatter:
    """
    Auxiliary class for formatting forecast.
    """
    def __init__(self):
        self.temperature_symbol = "🌡️"
        self.cloudliness_symbols = [
            (12.5, "☀️"),
            (37.5, "🌤️"),
            (62.5, "⛅"),
            (75.0, "🌥️"),
            (float("inf"), "☁️")
        ]
    
    def cloudliness_to_symbol(self, perc):
        """
        Gets symbol by cloudliness percentage.
        """
        for value, symbol in self.cloudliness_symbols:
            if perc < value:
                return symbol
        return None

    def format_cloudliness(self, forecast_interval):
        """
        Gets formated text of cloudliness by forecast interval.
        """
        return self.cloudliness_to_symbol(forecast_interval.variables["cloud_area_fraction"].value)

    def format_temperature(self, forecast_interval):
        """
        Gets formated text of temperature by forecast interval.
        """
        return f'{self.temperature_symbol} {forecast_interval.variables["air_temperature"].value}°C'

    def format_rainfall(self, forecast_interval):
        """
        Gets formated text of rainfall by forecast interval.
        """
        rainfall = forecast_interval.variables["precipitation_amount"].value
        result = ""

        if rainfall > 0:
            result = f"💧 {rainfall} mm"
        
        return result

    def format_wind(self, forecast_interval):
        """
        Gets formated text of wind speed by forecast interval.
        """
        forecast_interval.variables["wind_speed"].convert_to("km/h")
        wind_speed = forecast_interval.variables["wind_speed"].value
        result = ""

        if wind_speed > 0.5:
            result = f"💨 {round(wind_speed, 1)} km/h"

        return result

    def format_forecast(self, forecast_interval):
        """
        Gets formatted text of forecast by forecast interval.
        """
        parts = [
            formatter.format_temperature(forecast_interval),
            formatter.format_cloudliness(forecast_interval),
            formatter.format_rainfall(forecast_interval),
            formatter.format_wind(forecast_interval)
        ]
        return " ".join([part for part in parts])


#defining the place we want to get info of
your_place = Place("Šumperk", 49.9653, 16.9706, 336)

#getting the info from met-no
your_place_forecast = Forecast(your_place, "polybar_met-no_weather_module https://github.com/the-archy")
your_place_forecast.update()

#current hour
first_interval = your_place_forecast.data.intervals[0]

formatter = Formatter()
forecast_text = formatter.format_forecast(first_interval)

print(forecast_text)