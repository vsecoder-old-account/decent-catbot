from aiogram import types
from src.utils import get_full_name


async def p__welcome(event: types.Message):
    if getattr(event, "new_chat_members", None):
        if event.new_chat_member['id'] != 5504395725:
            await event.reply(
                f"Привет, <b>{get_full_name(event.new_chat_member)}</b> 👋",
            )
        else:
            await event.reply(
                f"Хм, а тут уютненько, жду права администратора, а чтобы начать использовать бота, напишите мне /protects"
            )
