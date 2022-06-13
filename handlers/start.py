from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.utils import get_full_name


async def start_handler(event: types.Message):
    if event.chat.id == event.from_user.id:
        builder = InlineKeyboardBuilder()

        invite = types.InlineKeyboardButton(
            text="Добавить в чат",
            url="http://t.me/decent_catbot?startgroup=True"
        )
        url = types.InlineKeyboardButton(
            text="Политика конфиденциальности",
            url="https://telegra.ph/Politika-konfidencialnosti--Decent-catbot-06-13"
        )
        builder.add(*[invite, url])
        # t.me/bot_user_name?startgroup=True
        await event.answer(
            f"Привет, <b>{get_full_name(event.from_user)}</b> 👋\n\nДобавьте меня в чат, и выдайте права администратора, остальное расскажу по мере поступления!",
            reply_markup=builder.as_markup()
        )
