# -*- coding: utf-8 -*-
import twilio.rest
import pyowm
from pyowm import OWM
from twilio.rest import Client


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

    return temp


def parse_weather(temp):
    cur_temp = str(temp['temp'])
    max_temp = str(temp['temp_max'])
    min_temp = str(temp['temp_min'])

    return cur_temp, max_temp, min_temp


def send_text(phone_number, place):
    place = "Boston, MA"
    weather_dict = get_weather(place)
    cur_temp, max_temp, min_temp = parse_weather(weather_dict)

    weather_body = "Current Temperature: " + cur_temp + " F°. Maximum Temperature: " + max_temp + " F°. Minimum Temperature: " + min_temp + " F°."

    account_sid = "AC984fee9fe6cc06c84923b4466a0c99a6"
    auth_token = "f107dd35e35b59857bbe03917ee1f83e"
    client = Client(account_sid, auth_token)

    message = client.api.account.messages.create(to="+1" + phone_number,
                                                 from_="+19788493104 ",
                                                 body= weather_body)





