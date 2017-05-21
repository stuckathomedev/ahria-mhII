import pyowm
from pyowm import OWM

def get_weather(place):
    api_key = '4becd4f5bd426b1adc8d23b8496d7d00'
    owm = OWM(api_key)
    owm_en = OWM()

    observation = owm.weather_at_place(place)

    temp = observation.get_weather().get_temperature('fahrenheit')

    daily_forecasts = owm.daily_forecast(place).get_forecast()

    print(temp)
    print()
    for forecast in daily_forecasts:
        date = forecast.get_reference_time('iso')
        status = forecast.get_status()
        temps = forecast.get_temperature('fahrenheit')

        print(date, status, temps)


