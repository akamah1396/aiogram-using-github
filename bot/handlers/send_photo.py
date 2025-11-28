import asyncio
from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

send_photo_router = Router()

@send_photo_router.message(Command("photo"))
async def send_photos(message: Message):
    photo = FSInputFile("resources\\images\\gff.png")
    await message.answer_photo(photo=photo,caption="اینم از عکست!")