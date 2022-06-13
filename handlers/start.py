from aiogram import types
from src.utils import get_full_name

async def start_handler(event: types.Message):
    if event.chat.id == event.from_user.id:
        await event.reply(
            f"Привет, <b>{get_full_name(event)}</b> 👋\n\nДобавьnt меня в чат, и выдай права администратора!",
        )