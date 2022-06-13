from aiogram import types, Bot
import time
from src.utils import convert_time, get_link, get_full_name

mute_text = '🔇 <b><a href="{}">{}</a> замучен на {} минут. Причина: </b><i>{}</i>'
unmute_text = '🔊 <b><a href="{}">{}</a> unmuted</b>'

async def mute_handler(event: types.Message, bot: Bot):
    try:
        command = event.text.split()[0]
        member = await bot.get_chat_member(event.chat.id, event.from_user.id)
        if 'administrator' == member.status or 'creator' == member.status:
            if event.reply_to_message:
                args = event.text.replace('/mute ', '').split()
                if command == '/mute':
                    if len(args) != 2:
                        return await event.reply('♦️ <b>Ошибка, текст аргументов</b>\n\nПример: <code>/mute 1m flood</code>')
                    t = convert_time(args[0])
                    await bot.restrict_chat_member(
                        event.chat.id, 
                        event.reply_to_message.from_user.id, 
                        permissions=types.ChatPermissions(can_send_messages=False),
                        until_date=time.time()+t
                    )
                    await event.reply(mute_text.format(get_link(event.reply_to_message), get_full_name(event.reply_to_message), t/60, args[1]))
                if command == '/unmute':
                    await bot.restrict_chat_member(
                        event.chat.id, 
                        event.reply_to_message.from_user.id, 
                        permissions=types.ChatPermissions(
                            can_send_messages=True,
                            can_send_media_messages=True,
                            can_send_polls=True,
                            can_send_other_messages=True,
                            can_add_web_page_previews=True
                        ),
                        until_date=time.time()
                    )
                    await event.reply(unmute_text.format(get_link(event.reply_to_message), get_full_name(event.reply_to_message)))
            else:
                await event.reply('♦️ <b>Ошибка, команда должна быть в ответ на сообщение</b>\n\nПример: <code>/mute 1m flood</code>')
    except:
        await event.reply('♦️ <b>Ошибка, проверьте права бота, и правильность команды</b>\n\nПример: <code>/mute 1m flood</code>')