import requests
from aiogram.types import Message
from aiogram.utils.markdown import hbold


async def search_ipska(messaga: Message):
    '''html = requests.get("https://2ip.ua/ru/").text
    pattern = r'\d{2,}\.\d{2,}\.\d{2,}\.\d{2,}'
    ip = re.search(pattern, html).group()
    response = requests.get(url=f'http://ip-api.com/json/{ip}')'''
    response = requests.get(url=f'http://ip-api.com/json/{messaga.text}')
    data = response.json()

    ipp = data["query"]
    country = data["country"]
    regionname = data["regionName"]
    city = data["city"]
    index = data["zip"]
    lat = data["lat"]
    lon = data["lon"]
    timezone = data["timezone"]
    org = data["org"]

    await messaga.answer("🤫")
    await messaga.answer(hbold(f"Ip - {ipp}\n"
                               f"Країна - {country}\n"
                               f"Регіон - {regionname}\n"
                               f"Місто - {city}\n"
                               f"Індекс - {index}\n"
                               f"Широта - {lat}\n"
                               f"Довгота - {lon}\n"
                               f"Часовий пояс - {timezone}\n"
                               f"Провайдер - {org}\n"))

