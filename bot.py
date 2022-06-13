import asyncio
import logging
from aiogram import Bot, Dispatcher

from handlers import *

logger = logging.getLogger(__name__)

BOT_TOKEN = ""

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    try:
        disp = Dispatcher()
        disp.message.register(start_handler, commands={"start"})
        disp.message.register(protects_handler, commands={"protects"})
        disp.message.register(mute_handler, commands={"mute", "unmute"})
        disp.message.register(ban_handler, commands={"ban", "unban"})
        # reports
        # warns
        disp.message.register(protect_handler)
        await disp.start_polling(bot)
    finally:
        #await bot.close()
        pass

asyncio.run(main())