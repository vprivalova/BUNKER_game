from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6241768567:AAGi9QmUr0oX5UIZCOQDbiE8KcQuEyf8Ehs"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    await message.reply(f"Добро пожаловать в игру, {user_full_name}")


if __name__ == '__main__':
    executor.start_polling(dp)
