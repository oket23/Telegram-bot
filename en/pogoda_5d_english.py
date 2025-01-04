import requests
import datetime
import en.f1_en

from aiogram import types
from aiogram.utils.markdown import hbold
from tokens import weather_token


async def get_daily_weather_english(message: types.Message, days):
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
            f"https://api.openweathermap.org/data/2.5/forecast?q={message.text}&appid={weather_token}"
            f"&units=metric&cnt={days * 8}"
        )
        data = r.json()

        forecast_data = data["list"]

        for day in range(0, days):
            date = datetime.datetime.fromtimestamp(forecast_data[day * 8]["dt"])
            cur_weather = forecast_data[day * 8]["main"]["temp"]
            feels_like = forecast_data[day * 8]["main"]["feels_like"]
            weather_description = forecast_data[day * 8]["weather"][0]["main"]

            if weather_description in code_to_smile:
                wd = code_to_smile[weather_description]
            else:
                wd = "Look out the window, I don't understand what's going on there"

            humidity = forecast_data[day * 8]["main"]["humidity"]
            pressure = forecast_data[day * 8]["main"]["pressure"]
            wind = forecast_data[day * 8]["wind"]["speed"]

            await message.answer(hbold(f"---{date.strftime('%Y-%m-%d')}---\n"
                                       f"Average temperature: {cur_weather}C°\n"
                                       f"Feels like: {feels_like}C°\n"
                                       f"Humidity: {humidity}% / {wd}\n"
                                       f"Pressure: {pressure} mmHg\n"
                                       f"Wind speed: {wind}m/sec\n"))

        await message.answer("What are we doing⚙", reply_markup=en.f1_en.wea_back)

    except TypeError:
        await message.answer("Check the city name", reply_markup=en.f1_en.wea_back)
