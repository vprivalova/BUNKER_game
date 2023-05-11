from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

name = ['Lillian Powell', 'Brenda Bowen', 'Joseph Johnston', 'Glenn Fisher', 'Christina Horton', 'Jessica Mitchell', \
        'Roger Clark', 'Daniel Cole', 'Stephen Clark', 'Betty Wright', 'James Moody', 'Anita Kelly', 'John Perry', \
        'Harry Santiago', 'Robert Brooks', 'Douglas Williams', 'Sherry Allen', 'Kathryn Ruiz', 'James Wood', 'Jerry Harper', \
        'Lisa Graham', 'Donald McCoy', 'Virgil Baker', 'Glenn Page', 'Rose Dunn']
year = list(range(16, 51))
profession = ['Cooker', 'Didgey', 'Housekeeper']
hobby = ['something']
phobias = ['something']
backpack = ['something']
health = ['something']

TOKEN = "6241768567:AAGi9QmUr0oX5UIZCOQDbiE8KcQuEyf8Ehs"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    await message.reply(f"Добро пожаловать в игру, {user_full_name}")

    markup = InlineKeyboardMarkup()
    button = InlineKeyboardMarkup(text='ПОЛУЧИТЬ РОЛЬ', callback_data='butt_id')
    markup.add(button)

    await bot.send_message(message.chat.id, "Время выбрать роль", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "butt_id")
async def to_query(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, f'{random.choice(name)}, {random.choice(year)}')


if __name__ == '__main__':
    executor.start_polling(dp)

