from aiogram import types
from db import funcs

nsave = '💼 <b>Заметка </b><code>{}</code><b> сохранена!</b>'
nstop = '💼 <b>Заметка </b><code>{}</code><b> удалена!</b>'
answer = '💼 <b>Заметки:</b>\n'

async def notes_handler(event: types.Message):
    if event.chat.id != event.from_user.id:
        args = event.text.split(' ')
        command = args[0]
        if len(args) == 2:
            if command == '/nsave' and event.reply_to_message:
                funcs.create_note(
                    event.chat.id, 
                    args[1], 
                    event.reply_to_message.text
                )
                await event.answer(nsave.format(args[1]))
            if command == '/nstop':
                funcs.delete_note(event.chat.id, args[1])
                await event.answer(nstop.format(args[1]))
        if len(args) == 1:
            if command == '/notes':
                msg = answer
                notes = funcs.get_notes(event.chat.id)
                for note in notes:
                    msg += f' - <code>#{note["name"]}</code>\n'
                await event.answer(msg)
