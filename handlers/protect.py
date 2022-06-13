from aiogram import types
from src.utils import get_full_name

from protects import welcome


async def protect_handler(event: types.Message):
    await welcome.p__welcome(event)
