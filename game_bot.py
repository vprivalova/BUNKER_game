from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import ru_local as ru

name = ru.ALL_NAME
all_year = list(range(16, 51))
year = random.sample(all_year, 10)
all_profession = ru.ALL_PROFESSION
profession = random.sample(all_profession, 10)
all_hobby = ru.ALL_HOBBY
hobby = random.sample(all_hobby, 10)
all_phobias = ru.ALL_PHOBIAS
phobias = random.sample(all_phobias, 10)
all_backpack = ru.ALL_BACKPACK
backpack = random.sample(all_backpack, 10)
all_health = ru.ALL_HEALTH
health = random.sample(all_health, 10)

TOKEN = "6241768567:AAHpYDBlU4kz06BgwUx9j92NzLbJ15GJtuw"

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
    await bot.send_message(call.message.chat.id, f'{random.choice(name)}, {random.choice(year)}, {random.choice(profession)}')
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardMarkup(text='Голосование закончилось', callback_data='butt_show1')
    markup.add(button)

    await bot.send_message(call.message.chat.id, "По окончании голосования нажмите здесь", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "butt_show1")
async def to_query(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, 'продолжаем')
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardMarkup(text='ПОЛУЧИТЬ ХОББИ', callback_data='butt_hobby')
    markup.add(button)

    await bot.send_message(call.message.chat.id, "Время узнать ваше хобби", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "butt_hobby")
async def to_query(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, random.choice(hobby))
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardMarkup(text='Голосование закончилось', callback_data='butt_show2')
    markup.add(button)

    await bot.send_message(call.message.chat.id, "По окончании голосования нажмите здесь", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "butt_show2")
async def to_query(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, 'продолжаем')
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardMarkup(text='ПОЛУЧИТЬ ФОБИЮ', callback_data='butt_phobia')
    markup.add(button)

    await bot.send_message(call.message.chat.id, "Время узнать вашу фобию", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "butt_phobia")
async def to_query(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, random.choice(phobias))
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardMarkup(text='Голосование закончилось', callback_data='butt_show3')
    markup.add(button)

    await bot.send_message(call.message.chat.id, "По окончании голосования нажмите здесь", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "butt_show3")
async def to_query(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, 'продолжаем')
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardMarkup(text='ПОЛУЧИТЬ ВЕЩЬ ИЗ РЮКЗАКА', callback_data='butt_pack')
    markup.add(button)

    await bot.send_message(call.message.chat.id, "Время узнать какая вещь у вас в рюкзаке", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "butt_pack")
async def to_query(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, random.choice(backpack))
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardMarkup(text='Голосование закончилось', callback_data='butt_show4')
    markup.add(button)

    await bot.send_message(call.message.chat.id, "По окончании голосования нажмите здесь", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "butt_show4")
async def to_query(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, 'продолжаем')
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardMarkup(text='ПОЛУЧИТЬ ИНФОРМАЦИЮ О ЗДОРОВЬЕ', callback_data='butt_health')
    markup.add(button)

    await bot.send_message(call.message.chat.id, "Время узнать информацию о вашем здоровье", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "butt_health")
async def to_query(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, random.choice(health))
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardMarkup(text='Голосование закончилось', callback_data='butt_show5')
    markup.add(button)

    await bot.send_message(call.message.chat.id, "По окончании голосования нажмите здесь", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "butt_show5")
async def to_query(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, 'игра окончена')


if __name__ == '__main__':
    executor.start_polling(dp)

