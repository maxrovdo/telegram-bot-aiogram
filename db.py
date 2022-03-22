import sqlite3
import config
from aiogram import types, Bot

bot = Bot(token=config.TOKEN)
# bot=Bot(token='5120898350:AAGIiFskc-JAeF874l7c8GhlaXqTIWomUg4')

db = sqlite3.connect('bot.db')
cursor = db.cursor()
admin_id = 5253160477


def connect_to_bd():
    db.execute('''CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            first_name, 
            last_name, 
            uesrname, 
            datetime
            )''')
    db.commit()


def write_to_bd(message: types.Message):
    cursor.execute('SELECT id FROM users WHERE id == ?', (message.from_user.id,))
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?)', (
            message.from_user.id, f'{message.from_user.first_name}', f'{message.from_user.last_name}',
            f'{message.from_user.username}', f'{message.date}'))
        db.commit()
    else:
        pass


async def send_users_id_to_admin(message: types.Message):
    if message.from_user.id == admin_id:
        users_id = []
        for id in cursor.execute("SELECT id FROM users").fetchall():
            users_id.append(str(id[0]))
        await bot.send_message(admin_id, '\n'.join(users_id))
