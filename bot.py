import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import BOT

from handlers import *

logger = logging.getLogger(__name__)

BOT_TOKEN = BOT["token"]

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=BOT["parse_mode"])
    try:
        disp = Dispatcher()
        disp.message.register(start_handler, commands={"start"})
        disp.message.register(protects_handler, commands={"protects"})
        disp.message.register(mute_handler, commands={"mute", "unmute"})
        disp.message.register(ban_handler, commands={"ban", "unban", "kick"})
        disp.message.register(set_protect_handler, commands={"set_protect", "setprotect"})
        disp.message.register(notes_handler, commands={"nsave", "nstop", "notes"})
        # reports
        # warns
        disp.message.register(protect_handler)
        await disp.start_polling(bot)
    except Exception as e:
        print(e)
    finally:
        #await bot.close()
        pass

asyncio.run(main())
