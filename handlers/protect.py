from aiogram import types
from src.utils import get_full_name

from protects import welcome
from protects import antiexplicit
from protects import antichannel
from protects import antitagall

from db import funcs


async def protect_handler(event: types.Message):
    if event.chat.id == event.from_user.id:
        return
    funcs.init_chat(event.chat.id)

    await welcome.p__welcome(event)

    await antichannel.p__antichannel(event)

    await antitagall.p__antitagall(event)

    await antiexplicit.p__censor(event)