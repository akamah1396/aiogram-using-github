import asyncio
from aiogram import Dispatcher
from bot.my_bot import bot
from aiogram.types import Message
from aiogram.filters import Command
from bot.handlers.send_photo import send_photo_router


dp = Dispatcher()

@dp.message(Command("start"))
async def reply_start(message: Message)->None:
    await message.answer(f"سلام {message.from_user.first_name} \n ربات شما فعال شد. ")

def register_routers():
    dp.include_router(send_photo_router)

async def main():
    register_routers()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())