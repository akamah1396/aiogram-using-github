from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot.Config import BotConfig


create_admin_router = Router()

admins = []

@create_admin_router.message(Command("auth"))
async def get_id(msg: Message):
    admin_id = msg.from_user.id
    msg.answer("درخواست شما در حال اجراست...")
    if admin_id in admins:
        await msg.answer("شما در حال حاضر ادمین هستید")
        
    else:
        admins.append(admin_id)
        await msg.answer("درخواست شما پذیرفته شد")



    
    
