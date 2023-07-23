import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Hello {message.from_user.first_name}.')
    await message.answer(f'Hello {message.from_user.first_name}.')
    await message.reply(f'Hello {message.from_user.first_name}.')


async def start():
    bot = Bot(token='6387175579:AAGkGS1pe2Bvif9nMEoRprk3VxJ2wx6KCik')

    dp = Dispatcher()
    dp.message.register(get_start)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
