import asyncio
from aiogram import Dispatcher
from bot.AkamTestBot import bot
from aiogram.filters import Command
from aiogram.types import Message


dp = Dispatcher()


@dp.message(Command('start'))
async def reply_to_start(message: Message) -> None:
    username = message.from_user
    await message.answer(f"سلام {username} به ربات خودت خوش امدی.")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    