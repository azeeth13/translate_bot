from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup



menu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Uz -> Ru'),KeyboardButton(text='Ru -> Uz')],
        [KeyboardButton(text='Uz -> En'),KeyboardButton(text='En -> Uz')],
    ], 
    resize_keyboard=True
)


voice=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='audio',callback_data='voice')]
    ]
)