from aiogram import Bot, Dispatcher, executor, types
from Keyboard import keyboard

BOT_TOKEN = "5989702181:AAGn6m-O_nS8WdvqHk_6Oq-WuUdbxvdsP8w"

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


COMMAND_START = """
    <em> Добро пожаловать </em>
"""

COMMAND_HELP = """
    <em> /start - начать работу с ботом </em>
    <em> /help - список команд </em>
"""


# пишет в терминал
async def on_startup(_):
    print('бот начал работу')


# кoманда start
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(text=COMMAND_START, parse_mode="HTML", reply_markup=keyboard)
    await message.delete()


# кoманда help, bot будет отправлять смс в личку
@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=COMMAND_HELP, parse_mode="HTML")
    await message.delete()


# bot


# bot отправляет смс user-a в отв
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=f'<em>{message.text}</em>', parse_mode="HTML")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
