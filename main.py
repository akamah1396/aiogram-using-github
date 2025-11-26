import asyncio
from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
#from aiogram.types import Message
from bot_instance import bot
from bot.handlers.help_handler import help_router
from bot.handlers import create_admin
from bot.handlers.create_admin import create_admin_router
from bot.handlers.menu import menu_router




my_bot = bot

dp = Dispatcher()
router = Router()

@router.message(Command("start"))
async def start_message(msg):
    await msg.answer("ربات شما فعال شد.")

dp.include_router(router)
dp.include_router(help_router)
dp.include_router(create_admin_router)
dp.include_router(menu_router)


async def main():
    # bot.set_my_commands([
    #     BotCommand(command="auth", description="درخواست ادمینی"),
    # ])
    await dp.start_polling(bot)

asyncio.run(main())

