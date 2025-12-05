from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from test import PeyghamMiddleware

middleware_router = Router()
middleware_router.message.middleware(PeyghamMiddleware())

@middleware_router.message(Command("name"))
async def midHandler(message):
    await message.answer("نام خود را وارد کنید")
