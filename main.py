import asyncio
from aiogram import Dispatcher, html
from bot.my_bot import CreateBot
from aiogram.types import Message
from aiogram.filters import Command
from bot.handlers.send_photo import send_photo_router



bot = CreateBot().get_bot()

dp = Dispatcher()

@dp.message(Command("start"))
async def reply_start(message: Message)->None:
    await message.answer(f"<code>سلام</code>{html.bold(message.from_user.first_name)} \n{html.bold("ربات شما فعال شد.")} ")

def register_routers():
    dp.include_router(send_photo_router)

async def main():
    register_routers()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())