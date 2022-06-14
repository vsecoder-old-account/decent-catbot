from aiogram import types
from src.utils import get_full_name

from config import BOT, STRING

async def p__welcome(event: types.Message):
    if getattr(event, "new_chat_members", None):
        if int(event.new_chat_member['id']) != BOT['id']:
            await event.reply(
                STRING["welcome_user"].format(get_full_name(event.new_chat_member), event.chat.title)
            )
        else:
            await event.reply(
                STRING["welcome_bot"]
            )
