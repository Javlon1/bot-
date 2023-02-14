from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn1 = KeyboardButton('/help')
btn2 = KeyboardButton('/help')

keyboard.row(btn1, btn2)
