from aiogram import types

async def protects_handler(event: types.Message):
    await event.reply(
        (
            "<b>🛡 My protects:</b>\n"
            "<b>🐵 <code>AntiTagAll</code> - Ограничивает тег всех участников</b>\n"
            "<b>👋 <code>Welcome</code> - Приветствует новых участников</b>\n"
            "<b>🐶 <code>AntiRaid</code> - Банит новых участников</b>(in dev)\n"
            "<b>📯 <code>AntiChannel</code> - Запрещает написание сообщений от лица каналов</b>\n"
            "<b>🎑 <code>AntiGIF</code> - Запрещает GIFs</b>\n"
            "<b>🍓 <code>AntiNSFW</code> - Запрещает NSFW фото и стикеры</b>(now off)\n"
            "<b>⏱ <code>AntiFlood</code> - Запрещает флудить</b>(in dev)\n"
            "<b>😒 <code>AntiExplicit</code> - Запрещает материться </b>\n"
            "<b>🥷 <code>BanNinja</code> - Автоматическая версия защиты AntiRaid(</b>in dev)\n"
            "<b>👾 Админ: </b><code>/ban</code> <code>/kick</code> <code>/mute</code>\n"
            "<code>/unban</code> <code>/unmute</code> <b>- Инструменты администраторов</b>\n"
            "<b>👮‍♂️ Предупреждения:</b> <code>/warn</code> <code>/warns</code>(in dev)\n"
            "<b>🗒 Заметки:</b> <code>/nsave</code> <code>/nstop</code> <code>/notes</code> - заметки\n"
            "<b>⏳ Настроить защиту:</b> <code>/setprotect {name} [on/off]</code>\n"
        ),
    )