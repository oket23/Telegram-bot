from langdetect import detect
import ua.f1

from googletrans import Translator
from aiogram import Dispatcher, types
from aiogram.enums import ParseMode

dp = Dispatcher()
translator = Translator()


@dp.message()
async def translate_text(message: types.Message):
    text = message.text
    try:
        lang = detect(text)
        dest_lang = 'uk' if lang == 'en' else 'en'
        translation = translator.translate(text, dest=dest_lang)
        url_text = text.replace(" ", "%20")
        await message.answer(f"Оригінальний текст({lang}): {text}\nПереклад({dest_lang}): {translation.text}"
                             f"\nУсі варіанти перекладу:https://translate.google.com/?hl=ua&sl={lang}&tl={dest_lang}"
                             f"&text={url_text}%0A%0A&op=translate",
                             parse_mode=ParseMode.MARKDOWN, reply_markup=ua.f1.back)
    except ValueError:
        await message.answer("Виникла помилка при перекладі тексту. Спробуйте ще раз.")
