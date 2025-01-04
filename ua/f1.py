from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


menu = [
    [InlineKeyboardButton(text='Привітайся🖐', callback_data="hello")],
    [InlineKeyboardButton(text='Погода🌡', callback_data="wea")],
    [InlineKeyboardButton(text='Перекладач🔠', callback_data="tran")],
    [InlineKeyboardButton(text='Конвертер валют💵', callback_data="conv")],
    [InlineKeyboardButton(text='Допомога🆘', callback_data="support")],
    [InlineKeyboardButton(text='інформаціяℹ️', callback_data="info")],
    [InlineKeyboardButton(text='Мова🌐', callback_data="language_bot")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)

back = [
    [InlineKeyboardButton(text='⬅Вийти в меню⬅', callback_data="back")]
]
back = InlineKeyboardMarkup(inline_keyboard=back)

tran_back = [
    [InlineKeyboardButton(text='⬅Повернутися⬅', callback_data="backk")],
    [InlineKeyboardButton(text='⬅Вийти в меню⬅', callback_data="back")]
]
tran_back = InlineKeyboardMarkup(inline_keyboard=tran_back)

wea_back = [
    [InlineKeyboardButton(text='⬅Повернутися⬅', callback_data="back_wea")],
    [InlineKeyboardButton(text='⬅Вийти в меню⬅', callback_data="back")]
]
wea_back = InlineKeyboardMarkup(inline_keyboard=wea_back)


tran_sell = [
    [InlineKeyboardButton(text='English🇺🇸 --> Українська🇺🇦', callback_data="tran_sell_en")],
    [InlineKeyboardButton(text='Українська🇺🇦 --> English🇺🇸', callback_data="tran_sell_ua")],
    [InlineKeyboardButton(text='🇯🇵Визначати мову самостійно🇨🇦', callback_data="tran_sell_all")],
    [InlineKeyboardButton(text='⬅Вийти в меню⬅', callback_data="back")]
]

tran_sell = InlineKeyboardMarkup(inline_keyboard=tran_sell)

wea_set = [
    [InlineKeyboardButton(text='Сьогодні☀︎', callback_data="one_day")],
    [InlineKeyboardButton(text='5 днів📆', callback_data="five_day")],
    [InlineKeyboardButton(text='⬅Вийти в меню⬅', callback_data="back")]
]
wea_set = InlineKeyboardMarkup(inline_keyboard=wea_set)

language_set = [
    [InlineKeyboardButton(text='Українська🇺🇦', callback_data="ukr_language")],
    [InlineKeyboardButton(text='English🇺🇸', callback_data="en_language")]
]
language_set = InlineKeyboardMarkup(inline_keyboard=language_set)

