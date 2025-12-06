from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any




class PeyghamMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data)->Any:
        data["harchi"] = "دیتای میان افزار"
        await event.answer("این نوشته قبل از هندلر فرستاده شد.")
        result = await handler(event,data)
        await event.answer("بعد از هندلر اجرا شد این.")
        return result