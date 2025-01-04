import requests
import datetime
import en.f1_en

from aiogram import types
from aiogram.utils.markdown import hbold
from tokens import open_weather_token


async def get_weather_english(message: types.Message):
    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Cloudy \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Rain \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Fog \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}"
            f"&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        fell_weather = data["main"]["feels_like"]
        max_temp = data["main"]["temp_max"]
        min_temp = data["main"]["temp_min"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Look out the window, I don't understand what's going on there"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        await message.answer(hbold(f"---{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}---\n"
                                   f"Weather in the city {city}:\nTemperature: {cur_weather}C°(Feels like {fell_weather}C°)\n"
                                   f"Maximum temperature: {max_temp}C°\nMinimum temperature: {min_temp}C°\n"
                                   f"Humidity: {humidity}% / {wd}\nPressure: {pressure} mmHg\nWind speed: {wind}m/sec\n"
                                   f"Sunrise: {sunrise_timestamp} am\nSunset: {sunset_timestamp} pm"), reply_markup=en.f1_en.wea_back)

    except TypeError:
        await message.answer("Check the city name", reply_markup=en.f1_en.wea_back)
