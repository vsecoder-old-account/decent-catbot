from aiogram import types
from src.utils import censore, get_full_name, get_link
from db import funcs

answer = '🤐 <a href="{}">{}</a>:\n <i>{}</i>'

async def p__censor(event: types.Message):
    if funcs.is_protected(event.chat.id, 'antiexplicit') and getattr(event, "text", False):
        text = censore(event.text)
        if text:
            await event.delete()
            await event.answer(
                answer.format(
                    get_link(event.from_user),
                    get_full_name(event.from_user), 
                    text
                )
            )