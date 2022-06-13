import time

from aiogram import Bot, types
from src.utils import convert_time, get_full_name, get_link

ban_text = '🔒 <b><a href="{}">{}</a> забанен на {} минут. Причина: </b><i>{}</i>'
unban_text = '🔑 <b><a href="{}">{}</a> unbanned</b>'

async def ban_handler(event: types.Message, bot: Bot):
    command = event.text.split()[0]
    try:
        member = await bot.get_chat_member(event.chat.id, event.from_user.id)
        if 'administrator' == member.status or 'creator' == member.status:
            if event.reply_to_message:
                args = event.text.replace(command, '').split()
                if command == '/ban':
                    if len(args) != 2:
                        return await event.reply(f'♦️ <b>Ошибка, текст аргументов</b>\n\nПример: <code>/ban 1d flood</code> or <code>/unban</code>')
                    t = convert_time(args[0])
                    await bot.kick_chat_member(
                        chat_id=event.chat.id, 
                        user_id=event.reply_to_message.from_user.id,
                        until_date=time.time()+t
                    )
                    await event.reply(ban_text.format(get_link(event.reply_to_message.from_user), get_full_name(event.reply_to_message.from_user), t/60, args[1]))
                if command == '/unban':
                    await bot.unban_chat_member(chat_id=event.chat.id, user_id=event.reply_to_message.from_user.id)
                    await event.reply(unban_text.format(get_link(event.reply_to_message.from_user), get_full_name(event.reply_to_message.from_user)))
            else:
                await event.reply(f'♦️ <b>Ошибка, команда должна быть в ответ на сообщение</b>\n\nПример: <code>/ban 1d flood</code> or <code>/unban</code>')
    except:
        await event.reply(f'♦️ <b>Ошибка, проверьте права бота, и правильность команды</b>\n\nПример: <code>/ban 1d flood</code> or <code>/unban</code>')
