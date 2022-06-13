FROM python:3.7-slim

WORKDIR /decent-catbot

COPY requirements.txt /decent-catbot/
RUN pip install -r /decent-catbot/requirements.txt
COPY . /decent-catbot/

CMD python3 /decent-catbot/bot.py
