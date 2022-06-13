import re

from aiogram import types


def get_full_name(user) -> str:
    try:
        return _process(f"{user.first_name} "
                + (user.last_name if getattr(user, "last_name", False) else ""))
    except:
        return _process(f"{user['first_name']} "
                + (user['last_name'] if getattr(user, "last_name", False) else ""))


def get_link(user) -> str:
    try:
        return (
            f"tg://user?id={user.id}"
            if user.username
            else (
                f"tg://resolve?domain={user.username}"
                if getattr(user, "username", None)
                else ""
            )
        )
    except:
        return (
            f"tg://user?id={user['id']}"
            if user['username']
            else (
                f"tg://resolve?domain={user['username']}"
                if getattr(user, "username", None)
                else ""
            )
        )

def _process(text: str) -> str:
    return text.replace("<", "&lt;").replace(">", "&gt;")

def convert_time(t: str) -> int:
    try:
        if not str(t)[:-1].isdigit():
            return 0
        if "d" in str(t):
            t = int(t[:-1]) * 60 * 60 * 24
        if "h" in str(t):
            t = int(t[:-1]) * 60 * 60
        if "m" in str(t):
            t = int(t[:-1]) * 60
        if "s" in str(t):
            t = int(t[:-1])
        t = int(re.sub(r"[^0-9]", "", str(t)))
    except ValueError:
        return 0
    return t
