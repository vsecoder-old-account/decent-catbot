from aiogram import types, Bot
from aiogram.utils.markdown import hide_link
from src.utils import get_full_name, get_random_gif
from db.funcs import is_protected

from config import BOT, STRING


async def p__welcome(event: types.Message):
    if getattr(event, "new_chat_members", None):
        if int(event.new_chat_member['id']) != BOT['id']:
            welcome_text = "👋 Приветствую, <b>{}</b> в чате <b>{}</b>!".format(get_full_name(event.new_chat_member), event.chat.title)
        else:
            welcome_text = STRING["welcome_bot"]

        await event.answer_video(
            get_random_gif(),
            caption=welcome_text,
        )
