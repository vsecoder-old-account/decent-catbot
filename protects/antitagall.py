from aiogram import types
from db import funcs

async def p__antitagall(event: types.Message):
    if funcs.is_protected(event.chat.id, 'antitagall') and getattr(event, "text", False):
        if event.text.count("tg://user?id=") >= 5:
            await event.delete()