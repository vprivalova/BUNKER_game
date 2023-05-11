from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

all_name = ['Lillian Powell', 'Brenda Bowen', 'Joseph Johnston', 'Glenn Fisher', 'Christina Horton', 'Jessica Mitchell',
            'Roger Clark', 'Daniel Cole', 'Stephen Clark', 'Betty Wright', 'James Moody', 'Anita Kelly', 'John Perry',
            'Harry Santiago', 'Robert Brooks', 'Douglas Williams', 'Sherry Allen', 'Kathryn Ruiz', 'James Wood',
            'Jerry Harper', 'Lisa Graham', 'Donald McCoy', 'Virgil Baker', 'Glenn Page', 'Rose Dunn']
name = random.sample(all_name, 10)
all_year = list(range(16, 51))
year = random.sample(all_year, 10)
all_profession = ['Cooker', 'Didgey', 'Housekeeper', 'Cooker', 'Didgey', 'Housekeeper', 'Cooker', 'Didgey',
                  'Housekeeper', 'Cooker', 'Didgey', 'Housekeeper']
profession = random.sample(all_profession, 10)
all_hobby = ['something', 'something', 'something', 'something', 'something', 'something', 'something',
             'something', 'something', 'something', 'something', 'something']
hobby = random.sample(all_hobby, 10)
all_phobias = ['something', 'something', 'something', 'something', 'something', 'something', 'something',
               'something', 'something', 'something', 'something', 'something', 'something']
phobias = random.sample(all_phobias, 10)
all_backpack = ['something', 'something', 'something', 'something', 'something', 'something', 'something', 'something',
                'something', 'something', 'something', 'something', 'something']
backpack = random.sample(all_backpack, 10)
all_health = ['something', 'something', 'something', 'something', 'something', 'something', 'something', 'something',
              'something', 'something', 'something', 'something', 'something']
health = random.sample(all_health, 10)

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

