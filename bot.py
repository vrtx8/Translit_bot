import os
import logging

from aiogram import Bot, Dispatcher, executor, types

from tr import translit     #функция транслита, лежит рядом

# from config import TOKEN

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {name}! Я Бот, который переводит с кириллицы на латиницу! Введи слово, которое нужно перевести!'

    logging.info(f'{name} {user_id} sent message {message.text}')
    await message.reply(text)


@dp.message_handler()
async def send_translit(message: types.Message):
    name = message.from_user.full_name
    user_id = message.from_user.id
    text = translit(message)

    logging.info(f'{name} {user_id} sent message {message.text}')
    await bot.send_message(user_id, text)


if __name__ == '__main__':
    executor.start_polling(dp)