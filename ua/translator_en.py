import ua.f1

from googletrans import Translator
from aiogram import Dispatcher, types
from aiogram.enums import ParseMode

dp = Dispatcher()
translator = Translator()


@dp.message()
async def translate_text_en(message: types.Message):
    text = message.text
    try:
        lang = "en"
        dest_lang = "uk"
        translation = translator.translate(text, dest="uk")
        url_text = text.replace(" ", "%20")
        await message.answer(f"Оригінальний текст: {text}\nПереклад: {translation.text}"
                                  f"\nУсі варіанти перекладу:https://translate.google.com/?hl=ua&sl={lang}&tl={dest_lang}"
                                  f"&text={url_text}%0A%0A&op=translate",
                             parse_mode=ParseMode.MARKDOWN, reply_markup=ua.f1.back)
    except ValueError:
        await message.answer("Виникла помилка при перекладі тексту. Спробуйте ще раз.")
