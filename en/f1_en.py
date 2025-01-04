from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


menu = [
    [InlineKeyboardButton(text='Say hello🖐', callback_data="hello_english")],
    [InlineKeyboardButton(text='Weather🌡', callback_data="wea_english")],
    [InlineKeyboardButton(text='Translator🔠', callback_data="tran_english")],
    [InlineKeyboardButton(text='Currency converter💵', callback_data="conv_english")],
    [InlineKeyboardButton(text='Help🆘', callback_data="support_english")],
    [InlineKeyboardButton(text='Infoℹ️', callback_data="info_english")],
    [InlineKeyboardButton(text='Language🌐', callback_data="language_bot_english")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)

back = [
    [InlineKeyboardButton(text='⬅Exit⬅', callback_data="back_english")]
]
back = InlineKeyboardMarkup(inline_keyboard=back)

tran_back = [
    [InlineKeyboardButton(text='⬅Back⬅', callback_data="backk_english")],
    [InlineKeyboardButton(text='⬅Exit⬅', callback_data="back_english")]
]
tran_back = InlineKeyboardMarkup(inline_keyboard=tran_back)

wea_back = [
    [InlineKeyboardButton(text='⬅Back⬅', callback_data="back_wea_english")],
    [InlineKeyboardButton(text='⬅Exit⬅', callback_data="back_english")]
]
wea_back = InlineKeyboardMarkup(inline_keyboard=wea_back)


tran_sell = [
    [InlineKeyboardButton(text='English🇺🇸 --> Ukrainian🇺🇦', callback_data="tran_sell_en_english")],
    [InlineKeyboardButton(text='Ukrainian🇺🇦 --> English🇺🇸', callback_data="tran_sell_ua_english")],
    [InlineKeyboardButton(text='🇯🇵Detect language🇨🇦', callback_data="tran_sell_all_english")],
    [InlineKeyboardButton(text='⬅Exit⬅', callback_data="back_english")]
]

tran_sell = InlineKeyboardMarkup(inline_keyboard=tran_sell)

wea_set = [
    [InlineKeyboardButton(text='Today☀︎', callback_data="one_day_english")],
    [InlineKeyboardButton(text='5 day📆', callback_data="five_day_english")],
    [InlineKeyboardButton(text='⬅Exit⬅', callback_data="back_english")]
]
wea_set = InlineKeyboardMarkup(inline_keyboard=wea_set)

language_set = [
    [InlineKeyboardButton(text='Українська🇺🇦', callback_data="ukr_language")],
    [InlineKeyboardButton(text='English🇺🇸', callback_data="en_language")]
]
language_set = InlineKeyboardMarkup(inline_keyboard=language_set)
