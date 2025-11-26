from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot.Config import BotConfig


create_admin_router = Router()

admins = []

@create_admin_router.message(Command("اجازه"))
async def get_id(msg: Message):
    id = await msg.from_user.id
    msg.answer("درخواست شما در حال اجراست...")
    if id in admins:
        await msg.answer("شما در حال حاضر ادمین هستید")
        
    else:
        admins.append(id)
        await msg.answer("درخواست شما پذیرفته شد")



    
    
