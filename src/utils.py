import re

import random
import os
import sys
sys.path.append("./censure")

from censure import Censor

censor_ru = Censor.get(lang='ru')
censor_en = Censor.get(lang='en')

#from nsfw_detector import predict

#model = predict.load_model('./src/nsfw_model.h5')


def is_nsfw(file, format):
    pass

def get_random_gif() -> str:
    with open("src/gifs/cats.txt", "r") as f:
        gifs = f.read().splitlines()
    return random.choice(gifs)

def censore(text):
    text1 = censor_ru.clean_line(text)
		
    if text != text1[0]:
        return text1[0]

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
