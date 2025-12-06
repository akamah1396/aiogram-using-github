from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from test import PeyghamMiddleware

middleware_router = Router()
middleware_router.message.middleware(PeyghamMiddleware())

@middleware_router.message(Command("name"))
async def midHandler(message: Message, harchi: str = None, access: str = "denied"):
    if access == "denied":
        await message.answer("شما مجاز نیستید")
       
    elif access == "approved":
        await message.answer("یو ار اتنتیکیتد.")
    
    else:
        await message.answer("سیستم با خطا مواجه شد.")
