from tinydb import TinyDB, Query

db = TinyDB('../db.json')
Chat = Query()

"""
[
    {
        "id": '1234567890',
        "antichannel": False,
        "antigif": False,
        "antiraid": False,
        "antiexplicit": False,
        "antitagall": False,
        "antitarab": False,
        "antinsfw": False,
        "antiflood": False,
        "banninja": False,
        "welcome": True,
        "welcome_text": "✌️ Hi, {mention}!",
        "report": True,
        "warns": [{"id": "1234567890", "reasons": ["spam", "flood"]}],
        "notes": [{"name": "dev", "text": "@vsecoder"}]
    }
]
"""

def init_chat(id):
    #print(db.search(Chat.id == id))
    if db.search(Chat.id == id):
        return False
    db.insert({
        "id": id,
        "antichannel": False,
        "antigif": False,
        "antiraid": False,
        "antiexplicit": True,
        "antitagall": False,
        "antitarab": False,
        "antinsfw": True,
        "antiflood": False,
        "banninja": False,
        "welcome": True,
        "welcome_text": "✌️ Hi, {mention}!",
        "report": True,
        "warns": [],
        "notes": [{"name": "dev", "text": "@vsecoder"}]
    })

def is_protected(id, protect):
    try:
        return db.search(Chat.id == id)[0][protect]
    except:
        return False

def set_protected(id, protect, value):
    db.update({protect: value}, Chat.id == id)
    return True

def create_note(id, name, text):
    notes = db.search(Chat.id == id)[0]["notes"]
    notes.append({"name": name, "text": text})
    db.update({"notes": notes}, Chat.id == id)
    return True

def delete_note(id, name):
    notes = db.search(Chat.id == id)[0]["notes"]
    for note in notes:
        if note["name"] == name:
            notes.remove(note)
            db.update({"notes": notes}, Chat.id == id)
            return True
    return False

def get_notes(id):
    notes = db.search(Chat.id == id)[0]["notes"]
    return notes

def get_note(id, name):
    notes = db.search(Chat.id == id)[0]["notes"]
    for note in notes:
        if note["name"] == name:
            return note["text"]

def create_warn(id, text):
    warns = db.search(Chat.id == id)[0]["warns"]
    warns.append(text)
    db.update({"warns": warns}, Chat.id == id)
    return True

def delete_warn(id, text):
    warns = db.search(Chat.id == id)[0]["warns"]
    for warn in warns:
        if warn == text:
            warns.remove(warn)
            db.update({"warns": warns}, Chat.id == id)
            return True
    return False

def get_warns(id, user_id):
    warns = db.search(Chat.id == id)[0]["warns"][user_id]
    return warns

set_protected(-1001698285437, 'antitagall', True)