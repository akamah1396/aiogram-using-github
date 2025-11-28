from aiogram import Router
from aiogram.types import Message, InputFileUnion
from aiogram.filters import Command

send_photo_router = Router()

@send_photo_router.message(Command("photo"))
async def send_photo(message: Message):
    photo = "resources\images\gff.png"
    message.answer_photo(photo=photo,caption="اینم از عکست!")