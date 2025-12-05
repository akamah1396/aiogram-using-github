from aiogram import BaseMiddleware
from aiogram.types import Message
import asyncio
from typing import Callable, Dict,Any


class PeyghamMiddleware(BaseMiddleware):
    async def __call__(self, handler: callable, event: Message, data:dict[str, Any]):
        print("middle ware is running...")
        result = await handler(event, data)
        print("code after middleware is running...")
        return result