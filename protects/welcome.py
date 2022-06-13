from aiogram import types
from src.utils import get_full_name


async def p__welcome(event: types.Message):
    if getattr(event, "new_chat_members", None):
        if int(event.new_chat_member['id']) != 5504395725:
            await event.reply(
                f"👋 Приветствую, <b>{get_full_name(event.new_chat_member)}</b> в чате <b>{event.chat.title}</b>!"
            )
        else:
            await event.reply(
                "🧐 <b>Хм, а тут уютненько, жду <u>права администратора</u>, а чтобы начать использовать бота, напишите сюда <code>/protects</code>!</b>"
            )
