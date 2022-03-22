import config
import time
import db
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from asyncio import sleep

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


async def connect_to_bd(_):
    db.connect_to_bd()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    db.write_to_bd(message)
    await message.answer(f'Первое сообщение {message.date}')
    time.sleep(0.35)
    await sleep(15*60)
    await message.answer(f'Второе сообщение {message.date}')
    await sleep(15*60)
    await message.answer(f'Третье сообщение {message.date}')
    await sleep(15*60)
    await message.answer(f'Четвертое сообщение {message.date}')


@dp.message_handler(commands=['users_id'])
async def send_users_id_to_admin(message: types.Message):
    await db.send_users_id_to_admin(message)


executor.start_polling(dp, skip_updates=True, on_startup=connect_to_bd)
