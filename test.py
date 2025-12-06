from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any




class PeyghamMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        print("before mid is running...")
        result = await handler(event,data)
        print("after mid is running...")