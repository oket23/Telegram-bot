import asyncio
import ua.f1
import en.f1_en
import logging

from en.kyrs_english import get_kurs_english
from en.pogoda_5d_english import get_daily_weather_english
from en.pogoda_english import get_weather_english
from en.translator_english import translate_text_english
from en.translator_ua_english import translate_text_ua_english
from en.translator_en_english import translate_text_en_english


from ua.kyrs import get_kurs
from ua.pogoda_5d import get_daily_weather
from ua.pogoda import get_weather
from ua.translator import translate_text
from ua.translator_ua import translate_text_ua
from ua.translator_en import translate_text_en


from googletrans import Translator
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.markdown import hbold
from commands import set_commads
from tokens import TOKEN
from ua.search_ip import search_ipska


dp = Dispatcher()
translator = Translator()
logging.basicConfig(level=logging.INFO)
F.data = None


@dp.message(Command('start'))
async def command_start(message: Message):
    await set_commads(bot)
    await message.answer(hbold(f'Вибери мову⬇️'), reply_markup=ua.f1.language_set)
    F.data = "st"


@dp.message(Command('stop'))
async def command_stop(message: Message):
    from time import sleep
    await message.answer(hbold("😴"))
    sleep(1)
    await message.answer(hbold("О ні, ваш пк пробує взламати невідома сутність. Негайно витягніть його з розетки!!"))
    for i in range(1, 101):
        if F.data == "st":
            break

        await message.answer(hbold(f"Процес взлому {i}%"))
        if 35 >= i <= 50:
            sleep(0.9)
        elif 51 >= i <= 80:
            sleep(0.8)
        elif 81 >= i:
            sleep(0.7)

        if i == 100:
            sleep(0.5)
            await message.answer("😈")
            await message.answer(hbold("Ви зробили велику помилку, ваш світ більше ніколи не буде колишнім..."))


@dp.message(Command('ip'))
async def command_ipp(messaga: Message):
    await messaga.answer("Введіть Ip:")
    F.data = "sip"

# основні калбеки


@dp.callback_query(lambda callback_query: callback_query.data == "ukr_language")
async def ukt_bot(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(hbold(f'Привіт, {callback_query.from_user.full_name} вибери одну з моїх функцій⬇'), reply_markup=ua.f1.menu)


@dp.callback_query(lambda callback_query: callback_query.data == "en_language")
async def eng_bot(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(hbold(f'Hello, {callback_query.from_user.full_name} select choose one of my features⬇'), reply_markup=en.f1_en.menu)


@dp.callback_query(lambda callback_query: callback_query.data == 'support')
async def support(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("🐣")
    await callback_query.message.answer(hbold("Знайшов баг або є питання? Пиши мені @oket13😉"), reply_markup=ua.f1.back)  # кнопка допомога


@dp.callback_query(lambda callback_query: callback_query.data == 'support_english')
async def support(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("🐣")
    await callback_query.message.answer(hbold("Found a bug or have a question? Write me @oket13😉"), reply_markup=en.f1_en.back)  # кнопка допомога англ мова


@dp.callback_query(lambda callback_query: callback_query.data == 'language_bot')
async def support(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("🌐")
    await callback_query.message.answer("Вибери мову⬇️", reply_markup=ua.f1.language_set)  # кнопка вибору мови


@dp.callback_query(lambda callback_query: callback_query.data == 'language_bot_english')
async def support(callback_query: types.CallbackQuery):
    await callback_query.message.answer("🌐")
    await callback_query.message.answer("Сhoose language⬇️", reply_markup=ua.f1.language_set)  # кнопка вибору мови англ


@dp.callback_query(lambda callback_query: callback_query.data == 'info')
async def info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("🤖")
    await callback_query.message.answer(hbold(f"Команди:\n/start - запуск бота\n/stop - зупинити бота\nFollow my twitch https://www.twitch.tv/oket13 ❤️"), reply_markup=ua.f1.back)  # кнопка інфо


@dp.callback_query(lambda callback_query: callback_query.data == 'info_english')
async def info(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("🤖")
    await callback_query.message.answer(hbold(f"Command:\n/start - launch bot\n/stop - stop bot\nFollow my twitch https://www.twitch.tv/oket13 ❤️"), reply_markup=en.f1_en.back)  # кнопка інфо англ мова


@dp.callback_query(lambda callback_query: callback_query.data == 'hello')
async def hello_callback(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("🖐")
    await callback_query.message.answer(hbold(f'Привіт мій любий/моя люба, {callback_query.from_user.full_name}❤️'), reply_markup=ua.f1.back)  # кнопка привітайся


@dp.callback_query(lambda callback_query: callback_query.data == 'hello_english')
async def hello_callback(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("🖐")
    await callback_query.message.answer(hbold(f'Hello my dear, {callback_query.from_user.full_name}❤️'), reply_markup=en.f1_en.back)  # кнопка привітайся англ мова


@dp.callback_query(lambda callback_query: callback_query.data == 'back')
async def back_to_menu(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(hbold("Ти знову у меню⬇"), reply_markup=ua.f1.menu)  # кнопка назад
    F.data = None


@dp.callback_query(lambda callback_query: callback_query.data == 'back_english')
async def back_to_menu(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(hbold("You are in the menu again⬇"), reply_markup=en.f1_en.menu)  # кнопка назад англ мова
    F.data = None


# калбеки для перекладача


@dp.callback_query(lambda callback_query: callback_query.data == 'backk')
async def back_to_menu(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(hbold("Вибери варіант перекладу⬇"), reply_markup=ua.f1.tran_sell)
    F.data = None


@dp.callback_query(lambda callback_query: callback_query.data == 'backk_english')
async def back_to_menu(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(hbold("Choose a translation option⬇"), reply_markup=en.f1_en.tran_sell)   # назад англ мова
    F.data = None


@dp.callback_query(lambda callback_query: callback_query.data == 'tran')
async def callback_trans_start(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("💬")
    await callback_query.message.answer(hbold("Вибери варіант перекладу⬇"), reply_markup=ua.f1.tran_sell)


@dp.callback_query(lambda callback_query: callback_query.data == 'tran_english')
async def callback_trans_start(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("💬")
    await callback_query.message.answer(hbold("Choose a translation option⬇"), reply_markup=en.f1_en.tran_sell)  # англ мова


@dp.callback_query(lambda callback_query: callback_query.data == 'tran_sell_all')
async def callback_trans_start(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(hbold("Напиши, що хочеш перекрасти в чат📝"), reply_markup=ua.f1.tran_back)
    F.data = "tran"


@dp.callback_query(lambda callback_query: callback_query.data == 'tran_sell_all_english')
async def callback_trans_start(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(hbold("Write what you want to translate in the chat📝"), reply_markup=en.f1_en.tran_back)  # англ мова
    F.data = "tran_english"


@dp.callback_query(lambda callback_query: callback_query.data == 'tran_sell_ua')
async def callback_trans_start(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(hbold("Напиши, що хочеш перекрасти в чат📝"), reply_markup=ua.f1.tran_back)
    F.data = "tran_ua"


@dp.callback_query(lambda callback_query: callback_query.data == 'tran_sell_ua_english')
async def callback_trans_start(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(hbold("Write what you want to translate in the chat📝"), reply_markup=en.f1_en.tran_back)  # англ мова
    F.data = "tran_ua_english"


@dp.callback_query(lambda callback_query: callback_query.data == 'tran_sell_en')
async def callback_trans_start(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(hbold("Напиши, що хочеш перекрасти в чат📝"), reply_markup=ua.f1.tran_back)
    F.data = "tran_en"


@dp.callback_query(lambda callback_query: callback_query.data == 'tran_sell_en_english')
async def callback_trans_start(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(hbold("Write what you want to translate in the chat📝"), reply_markup=en.f1_en.tran_back)  # англ мова
    F.data = "tran_en_english"


# калбеки для погоди


@dp.callback_query(lambda callback_query: callback_query.data == 'wea')
async def show_wea(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("⛅", reply_markup=ua.f1.wea_set)


@dp.callback_query(lambda callback_query: callback_query.data == 'wea_english')
async def show_wea(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("⛅", reply_markup=en.f1_en.wea_set)  # англ мова


@dp.callback_query(lambda callback_query: callback_query.data == 'back_wea')
async def show_wea(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("⛅", reply_markup=ua.f1.wea_set)
    F.data = None


@dp.callback_query(lambda callback_query: callback_query.data == 'back_wea_english')
async def show_wea(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("⛅", reply_markup=en.f1_en.wea_set)  # англ мова
    F.data = None


@dp.callback_query(lambda callback_query: callback_query.data == 'one_day')
async def show_wea_1day(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Напиши місто у якому хочеш дізнатися погоду🏙️", reply_markup=ua.f1.back)
    F.data = "wea"


@dp.callback_query(lambda callback_query: callback_query.data == 'one_day_english')
async def show_wea_1day(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Write the city in which you want to know the weather🏙️", reply_markup=en.f1_en.back)  # англ мова
    F.data = "wea_english"


@dp.callback_query(lambda callback_query: callback_query.data == 'five_day')
async def show_wea_5day(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Напиши місто у якому хочеш дізнатися погоду🏙️", reply_markup=ua.f1.back)
    F.data = "wea5"


@dp.callback_query(lambda callback_query: callback_query.data == 'five_day_english')
async def show_wea_5day(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Write the city in which you want to know the weather🏙️", reply_markup=en.f1_en.back)  # англ мова
    F.data = "wea5_english"


@dp.callback_query(lambda callback_query: callback_query.data == 'wea_menu')
async def back_to_menu(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(hbold("Ти знову у меню⬇"), reply_markup=ua.f1.menu)


@dp.callback_query(lambda callback_query: callback_query.data == 'wea_menu_english')
async def back_to_menu(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer(hbold("You are in the menu again⬇"), reply_markup=en.f1_en.menu)  # англ мова


# калбеки для конвектора


@dp.callback_query(lambda callback_query: callback_query.data == "conv")
async def show_conv_menu(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("💸")
    await callback_query.message.answer("Напиши кількість гривень для конвертації у різні валюти📈", reply_markup=ua.f1.back)
    F.data = "convert"


@dp.callback_query(lambda callback_query: callback_query.data == "conv_english")
async def show_conv_menu(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("💸")
    await callback_query.message.answer("Write the amount of hryvnias to convert into different currencies📈", reply_markup=en.f1_en.back)  # англ мова
    F.data = "convert_english"


@dp.message(F.text)
async def text_answer(message: Message) -> None:
    functions_mapping = {
        "tran": translate_text,
        "wea": get_weather,
        "wea5": lambda m: get_daily_weather(m, days=5),
        "tran_ua": translate_text_ua,
        "tran_en": translate_text_en,
        "convert": get_kurs,
        "tran_english": translate_text_english,
        "wea_english": get_weather_english,
        "wea5_english": lambda m: get_daily_weather_english(m, days=5),
        "tran_ua_english": translate_text_ua_english,
        "tran_en_english": translate_text_en_english,
        "convert_english": get_kurs_english,
        "sip": search_ipska
    }

    function = functions_mapping.get(F.data)
    if function:
        await function(message)


async def main() -> None:
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
