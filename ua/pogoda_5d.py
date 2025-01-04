import requests
import datetime
import ua.f1

from aiogram import types
from aiogram.utils.markdown import hbold
from tokens import weather_token


async def get_daily_weather(message: types.Message, days):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Хмарно \U00002601",
        "Rain": "Дощ \U00002614",
        "Drizzle": "Дощ \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Сніг \U0001F328",
        "Mist": "Туман \U0001F32B"
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
                wd = "Подивись в вікно, я не розумію що там відбувається"

            humidity = forecast_data[day * 8]["main"]["humidity"]
            pressure = forecast_data[day * 8]["main"]["pressure"]
            wind = forecast_data[day * 8]["wind"]["speed"]

            await message.answer(hbold(f"---{date.strftime('%Y-%m-%d')}---\n"
                                       f"Середня Температура: {cur_weather}C°\n"
                                       f"Відчувається як: {feels_like}C°\n"
                                       f"Вологість: {humidity}% / {wd}\n"
                                       f"Тиск: {pressure} мм.рт.ст\n"
                                       f"Швидкість вітру: {wind}м/сек\n"))

        await message.answer("Що робимо⚙", reply_markup=ua.f1.wea_back)

    except TypeError:
        await message.answer("Провірьте назву міста", reply_markup=ua.f1.wea_back)
