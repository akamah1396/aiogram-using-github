import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from aiogram.filters import Command
from aiogram.types import Message

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def reply_to_start(message: Message):
    await message.answer("سلام  به ربات خودت خوش امدی.")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    