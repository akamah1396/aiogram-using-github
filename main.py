import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import authkey

BOT_TOKEN = authkey.BOT_TOKEN



bot = Bot(token=BOT_TOKEN
          )
dp = Dispatcher()



@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(f" سلام { message.from_user.first_name}! ربات با Aiogram آماده است 😊")

@dp.message()
async def echo_handler(message: Message):
    await message.answer(f"تو گفتی: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
