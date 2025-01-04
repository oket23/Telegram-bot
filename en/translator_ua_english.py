import en.f1_en

from googletrans import Translator
from aiogram import Dispatcher, types
from aiogram.enums import ParseMode

dp = Dispatcher()
translator = Translator()


@dp.message()
async def translate_text_ua_english(message: types.Message):
    text = message.text
    try:
        lang = "uk"
        dest_lang = "en"
        translation = translator.translate(text, dest="en")
        url_text = text.replace(" ", "%20")
        await message.answer(f"Original text: {text}\nTranslation: {translation.text}"
                             f"\nAll translation options:https://translate.google.com/?hl=en&sl={lang}&tl={dest_lang}"
                             f"&text={url_text}%0A%0A&op=translate",
                             parse_mode=ParseMode.MARKDOWN, reply_markup=en.f1_en.back)
    except ValueError:
        await message.answer("An error occurred while translating the text. Try again.")
