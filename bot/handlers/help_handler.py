from aiogram import Router
from aiogram.filters import Command

name = "saman"

help_router = Router()
@help_router.message(Command("help"))
async def help_comand_handler(msg):
    await msg.answer("شما درخواست کمک کردید!")