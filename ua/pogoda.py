import requests
import datetime
import ua.f1

from aiogram import types
from aiogram.utils.markdown import hbold
from tokens import open_weather_token


async def get_weather(message: types.Message):
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
            wd = "Подивись в вікно, я не розумію що там відбувається"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        await message.answer(hbold(f"---{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}---\n"
                                   f"Погода в місті {city}:\nТемпература: {cur_weather}C°(Відчувається як {fell_weather}"
                                   f"C°)\n"
                                   f"Максимальна температура: {max_temp}C°\nМінімальна температура: {min_temp}C°\n"
                                   f"Вологість: {humidity}% / {wd}\nТиск: {pressure} мм.рт.ст\nШвидкість вітру: "
                                   f"{wind}м/сек\n"
                                   f"Схід сонця: {sunrise_timestamp} am\nЗахід сонця: {sunset_timestamp} pm"), reply_markup=ua.f1.wea_back)

    except TypeError:
        await message.answer("Провірьте назву міста")
