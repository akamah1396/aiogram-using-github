import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
#from aiogram.types import Message
from bot_instance import bot
from bot.handlers.help_handler import help_router

my_bot = bot
dp = Dispatcher()
router = Router()

@router.message(Command("start"))
async def start_message(msg):
    await msg.answer("ربات شما فعال شد.")

dp.include_router(router)
dp.include_router(help_router)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())

