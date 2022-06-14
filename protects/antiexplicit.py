from aiogram import types
from src.utils import censore, get_full_name, get_link
from db import funcs

from config import STRING

answer = STRING['explicit']

async def p__censor(event: types.Message):
    if funcs.is_protected(event.chat.id, 'antiexplicit'):
        if getattr(event, "text", False):
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
        if getattr(event, "caption", False):
            text = censore(event.caption)
            if text:
                await event.delete()
                await event.answer(
                    f'🤐 Пожалуйста без таких выражений <b>{get_full_name(event.from_user)}</b>!'
                )