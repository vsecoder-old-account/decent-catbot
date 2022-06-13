from aiogram import types
from db import funcs

async def p__antichannel(event: types.Message):
    if funcs.is_protected(event.chat.id, 'antichannel'):
        if event.from_user.id == 136817688:
            await event.delete()