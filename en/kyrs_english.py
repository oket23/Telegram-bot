import requests
import datetime
import en.f1_en

from aiogram import types
from aiogram.utils.markdown import hbold


async def get_kurs_english(message: types.Message):

    try:
        r = requests.get(f"https://api.monobank.ua/bank/currency")
        data = r.json()

        usd_sell = 0
        euro_sell = 0
        gbp = 0
        jpy = 0
        chf = 0
        zl = 0
        yun = 0

        for currency in data:
            if currency["currencyCodeA"] == 840:
                usd_sell = currency["rateSell"]
            elif currency["currencyCodeA"] == 978 and currency["currencyCodeB"] == 980:
                euro_sell = currency["rateSell"]
            elif currency["currencyCodeA"] == 826:
                gbp = currency["rateCross"]
            elif currency["currencyCodeA"] == 392:
                jpy = currency["rateCross"]
            elif currency["currencyCodeA"] == 756:
                chf = currency["rateCross"]
            elif currency["currencyCodeA"] == 985:
                zl = currency["rateCross"]
            elif currency["currencyCodeA"] == 156:
                yun = currency["rateCross"]

        usd_sell = round(usd_sell, 2)
        euro_sell = round(euro_sell, 2)
        gbp = round(gbp, 2)
        jpy = round(jpy, 2)
        chf = round(chf, 2)
        zl = round(zl, 2)
        yun = round(yun, 2)

        await message.answer(hbold(f"---{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}---\n"
                                   f"{message.text} hryvnias in different currencies:\n"
                                   f"{message.text} ₴ = {round(float(message.text) / usd_sell, 2)} $\n"
                                   f"{message.text} ₴ = {round(float(message.text) / euro_sell, 2)} €\n"
                                   f"{message.text} ₴ = {round(float(message.text) / gbp, 2)} £\n"
                                   f"{message.text} ₴ = {round(float(message.text) / jpy, 2)} ¥\n"
                                   f"{message.text} ₴ = {round(float(message.text) / chf, 2)} SFr\n"
                                   f"{message.text} ₴ = {round(float(message.text) / zl, 2)} zł\n"
                                   f"{message.text} ₴  = {round(float(message.text) / yun, 2)} ¥"), reply_markup=en.f1_en.back)

    except ValueError:
        await message.answer("Too many requests, try again later", reply_markup=en.f1_en.back)
