from aiogram import types
from db import funcs

anwer = '🛡 <b>Защита {} {}</b>'

async def set_protect_handler(event: types.Message):
    if event.chat.id != event.from_user.id:
        args = event.text.split(' ')
        if len(args) == 3:
            state = True if args[2] == 'on' else False
            funcs.set_protected(event.chat.id, args[1].lower(), state)
            await event.answer(anwer.format(args[1].lower(), 'включена' if state else 'отключена'))
        else:
            await event.answer('Неверный формат!')
