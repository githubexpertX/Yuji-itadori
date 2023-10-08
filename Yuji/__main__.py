import logging
from pyrogram import Client, filters
from pyrogram.types import *
import random
import asyncio
from bs4 import BeautifulSoup
from os import getenv
from pyrogram import Client, filters
from pyrogram.types import *
import random
import asyncio
from random import choice
from requests import get
import time, datetime
from redis import Redis
from os import getenv
import pymongo
from pyrogram import filters
import os
import logging
from telethon import Button, events
from telethon import TelegramClient
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram import filters
import os
import asyncio
from typing import Dict, Union
from pyrogram import filters
from pyrogram.types import Message
from requests import post, get
from pymongo import MongoClient
from Yuji.db import MONGO_URL as db_url
from typing import List, Any
from telegraph import upload_file
from pyrogram import filters
from os import name
from pyrogram.methods import messages
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from re import escape
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as telever
from telethon import __version__ as tlhver
import random
from datetime import datetime
from pyrogram import filters




# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual API credentials
api_id = '28731705'
api_hash = '7ed8bb45ea845bef652aa0606584f413'

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '6338221023:AAF7XDPQv6p6ebWdunT1tcCLDdsY1mBy_KA'
BOT_TOKEN = getenv("BOT_TOKEN", '6338221023:AAF7XDPQv6p6ebWdunT1tcCLDdsY1mBy_KA')
# Create a Pyrogram client instance
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

bot = TelegramClient('N1', api_id, api_hash).start(bot_token=BOT_TOKEN)

ALIVE_PIC = getenv("ALIVE_PIC", 'https://te.legra.ph/file/403acffa5ca195e17112b.jpg')

HELPP_TEXT = ("ʜᴇʟʟᴏ [sɪʀ](tg://settings)\n\nʏᴜᴊɪ ɪᴛᴀᴅᴏʀɪ ʜᴇʀᴇ\nɪᴍ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ\nɪ ᴡɪʟʟ ʜᴇʟᴘ ʏᴏᴜ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ \n\nɪғ ʏᴏᴜ ɴᴏᴛɪᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴡɪᴛʜ ᴛʜᴇ ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ ʀᴇᴘᴏʀᴛ ɪᴛ ɪɴ ᴍʏ [sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ](@fuck_uff_XD).")

EMOJIOS = [ 
      "ʏᴏᴏᴏᴏ ♡"]

help_message = []

OWNER = 6647321265

OWNER_ID = int(getenv("OWNER_ID",'6647321265'))
      
@app.on_message(filters.command(["start"]))
async def restart(client, m: Message):
    accha = await m.reply_text(
                text = random.choice(EMOJIOS),
    )
    await asyncio.sleep(0.5)
    await accha.edit("ʟᴇ ᴍᴇ ɪɴᴛʀᴏᴅᴜᴄᴇ ᴍʏsᴇʟғ...")
    await asyncio.sleep(0.6)
    await accha.edit("ɪ'ᴍ ʏᴜᴊɪ ɪᴛᴀᴅᴏʀɪ ♡")
    await asyncio.sleep(0.7)
    await accha.edit("ɪ ᴀᴍ ᴀ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ. ✦")
    await asyncio.sleep(0.5)
    await accha.delete()
    accha = await m.reply_photo(ALIVE_PIC,
    caption = HELPP_TEXT,
    reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton('♡ ᴅᴇᴠᴇʟᴏᴘᴇʀ ♡', url="https://t.me/fuck_uff_XD")]])
  )


RUN_STRINGS = (
    "Now you see me, now you don't."
    "ε=ε=ε=ε=┌(;￣▽￣)┘",
    "Get back here!",
    "REEEEEEEEEEEEEEEEEE!!!!!!!",
    "Look out for the wall!",
    "Don't leave me alone with them!!",
    "You've got company!",
    "Chotto matte!",
    "Yare yare daze",
    "*Naruto run activated*",
    "*Nezuko run activated*",
    "Hey take responsibilty for what you just did!",
    "May the odds be ever in your favour.",
    "Run everyone, they just dropped a bomb 💣💣",
    "And they disappeared forever, never to be seen again.",
    "Legend has it, they're still running.",
    "Hasta la vista, baby.",
    "Ah, what a waste. I liked that one.",
    "As The Doctor would say... RUN!",
)

EYES = [
    ["⌐■", "■"],
    [" ͠°", " °"],
    ["⇀", "↼"],
    ["´• ", " •`"],
    ["´", "`"],
    ["`", "´"],
    ["ó", "ò"],
    ["ò", "ó"],
    ["⸌", "⸍"],
    [">", "<"],
    ["Ƹ̵̡", "Ʒ"],
    ["ᗒ", "ᗕ"],
    ["⟃", "⟄"],
    ["⪧", "⪦"],
    ["⪦", "⪧"],
    ["⪩", "⪨"],
    ["⪨", "⪩"],
    ["⪰", "⪯"],
    ["⫑", "⫒"],
    ["⨴", "⨵"],
    ["⩿", "⪀"],
    ["⩾", "⩽"],
    ["⩺", "⩹"],
    ["⩹", "⩺"],
    ["◥▶", "◀◤"],
    ["◍", "◎"],
    ["/͠-", "┐͡-\\"],
    ["⌣", "⌣”"],
    [" ͡⎚", " ͡⎚"],
    ["≋"],
    ["૦ઁ"],
    ["  ͯ"],
    ["  ͌"],
    ["ළ"],
    ["◉"],
    ["☉"],
    ["・"],
    ["▰"],
    ["ᵔ"],
    [" ﾟ"],
    ["□"],
    ["☼"],
    ["*"],
    ["`"],
    ["⚆"],
    ["⊜"],
    [">"],
    ["❍"],
    ["￣"],
    ["─"],
    ["✿"],
    ["•"],
    ["T"],
    ["^"],
    ["ⱺ"],
    ["@"],
    ["ȍ"],
    ["  "],
    ["  "],
    ["x"],
    ["-"],
    ["$"],
    ["Ȍ"],
    ["ʘ"],
    ["Ꝋ"],
    [""],
    ["⸟"],
    ["๏"],
    ["ⴲ"],
    ["◕"],
    ["◔"],
    ["✧"],
    ["■"],
    ["♥"],
    [" ͡°"],
    ["¬"],
    [" º "],
    ["⨶"],
    ["⨱"],
    ["⏓"],
    ["⏒"],
    ["⍜"],
    ["⍤"],
    ["ᚖ"],
    ["ᴗ"],
    ["ಠ"],
    ["σ"],
    ["☯"],
]


@app.on_message(filters.command('run'))
async def run(client, message):
    await message.reply_text(choice(RUN_STRINGS))
    return


@app.on_message(filters.command('eye'))
async def eye(client, message):
    await message.reply_text(choice(EYES))

mongo = MongoClient(db_url)
db = mongo.StringGen


@app.on_message(filter("string"))
async def start(app: Client, msg: Message):
    me2 = (await app.get_me()).mention
    await app.send_message(
        chat_id=msg.chat.id,
        text=f"""ʜᴇʏ {msg.from_user.mention}🍷,

ɪ ᴀᴍ ʏᴜᴊɪ !!
ᴛʀᴜsᴛᴇᴅ sᴛʀɪɴɢ ɢʀɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.
ғᴜʟʟʏ sᴀғᴇ & sᴇᴄᴜʀᴇ.
ɴᴏ ᴀɴʏ ᴇʀʀᴏʀ

ᴍᴀᴅᴇ ʙʏ  : [ʏᴜᴊɪ](tg://user?id=6647321265) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="✦ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ ✦", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("♡ sᴜᴘᴘᴏʀᴛ ♡", url="https://t.me/fuck_uff_XD"),
                    InlineKeyboardButton("დ ᴀɴʏ ᴇʀʀᴏʀs დ", url="https://t.me/fuck_uff_XD")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )

BUTTON = [[Button.url("🍒 ꜱᴜᴘᴘᴏʀᴛ 🍒", "https://t.me/fuck_uff_XD")]]
HOT = "https://telegra.ph/file/daad931db960ea40c0fca.gif"
SMEXY = "https://telegra.ph/file/a23e9fd851fb6bc771686.gif"
LEZBIAN = "https://telegra.ph/file/5609b87f0bd461fc36acb.gif"
BIGBALL = "https://i.gifer.com/8ZUg.gif"
LANG = "https://telegra.ph/file/423414459345bf18310f5.gif"
CUTIE = "https://64.media.tumblr.com/d701f53eb5681e87a957a547980371d2/tumblr_nbjmdrQyje1qa94xto1_500.gif"
SIGMA = "https://te.legra.ph/file/7ff836ce726f9efce590c.mp4"


@bot.on(events.NewMessage(pattern="/horny ?(.*)"))
async def horny(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)}]"
    mm = random.randint(1, 100)
    HORNY = f"**🔥** {mention} **ɪꜱ** {mm}**% ʜᴏʀɴʏ!**"
    await e.reply(HORNY, buttons=BUTTON, file=HOT)


@bot.on(events.NewMessage(pattern="/gay ?(.*)"))
async def gay(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    GAY = f"**🍷** {mention} **ɪꜱ** {mm}**% ɢᴀʏ!**"
    await e.reply(GAY, buttons=BUTTON, file=SMEXY)


@bot.on(events.NewMessage(pattern="/lezbian ?(.*)"))
async def lezbian(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    FEK = f"**💜** {mention} **ɪꜱ** {mm}**% ʟᴇᴢʙɪᴀɴ!**"
    await e.reply(FEK, buttons=BUTTON, file=LEZBIAN)


@bot.on(events.NewMessage(pattern="/boob ?(.*)"))
async def boob(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    BOOBS = f"**🍒** {mention}**'ꜱ ʙᴏᴏʙꜱ ꜱɪᴢᴇ ɪᴢ** {mm}**!**"
    await e.reply(BOOBS, buttons=BUTTON, file=BIGBALL)


@bot.on(events.NewMessage(pattern="/cock ?(.*)"))
async def cock(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    COCK = f"**🍆** {mention}**'ꜱ ᴄᴏᴄᴋ ꜱɪᴢᴇ ɪᴢ** {mm}**ᴄᴍ**"
    await e.reply(COCK, buttons=BUTTON, file=LANG)


@bot.on(events.NewMessage(pattern="/cute ?(.*)"))
async def cute(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CUTE = f"**🍑** {mention} {mm}**% ᴄᴜᴛᴇ**"
    await e.reply(CUTE, buttons=BUTTON, file=CUTIE)


@bot.on(events.NewMessage(pattern="/chad ?(.*)"))
async def chad(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CHAD = f"**🔥** {mention} **ɪꜱ** {mm}**% ᴄʜᴀᴅ!**"
    await e.reply(CHAD, buttons=BUTTON, file=SIGMA)





# SHIVA MISHRA

@app.on_message(filters.command("alive"))
async def awake(_, message: Message):
    TEXT = f"**ʜᴇʏ {message.from_user.mention},\nɪ ᴀᴍ ʏᴜᴊɪ ɪᴛᴀᴅᴏʀɪ**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ :** [ᴋɪɴɢ](tg://user?id=6647321265)\n\n"
    TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n"
    TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n"
    BUTTON = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/fuck_uff_XD"),
        ]
    ]
    await message.reply_photo(
        photo=ALIVE_PIC,
        caption=TEXT,
        reply_markup=InlineKeyboardMarkup(BUTTON),
    )



def define(word: str):
    url = "http://urbandictionary.com/define.php?term=" + word
    response = get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find("div", {"class": "p-5 md:p-8"})
    word = content.find("div", class_="sm:flex sm:flex-row-reverse")
    meaning = content.find("div", class_="meaning my-4")

    return {"word": word.text, "meaning": meaning.text}


@app.on_message(filters.regex(r"(?i)^define (.*)$"))
def ok(client, m: Message):
    word = m.text.replace(m.text.split(" ")[0], "").strip()
    data = define(word)
    m.reply(f"**{data['word']}**\n\n{data['meaning']}")



def latest():

    url = 'https://subsplease.org/api/?f=schedule&h=true&tz=Japan'
    res = get(url).json()

    k = None
    for x in res['schedule']:
        title = x['title']
        time = x['time']
        try:
            aired = bool(x['aired'])
            title = f"**[{title}](https://subsplease.org/shows/{x['page']})**" if not aired else f"**~~[{title}](https://subsplease.org/shows/{x['page']})~~**"
        except KeyError:
            title = f"**[{title}](https://subsplease.org/shows/{x['page']})**"
        data = f"{title} - {time}"

        if k:
            k = f"{k}\n{data}"

        else:
            k = data

    return k


@app.on_message(filters.command('latest'))
def lates(_, message):
    mm = latest()
    message.reply_text(f"Today's Schedule:\nTZ: Japan\n{mm}")



@app.on_message(filters.command('paste'))
def pastex(_, message):
    text = message.reply_to_message
    if text:
        x = paste(text.text)
        message.reply(x,
                      reply_markup=InlineKeyboardMarkup(
                          [[InlineKeyboardButton("Open", url=x)]]),
                      disable_web_page_preview=True)

    else:
        message.reply_text("Reply to a message!")


@app.on_message(filters.command('id'))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**Your ID**: `{message.from_user.id}`\n**{reply.from_user.first_name}'s ID**: `{reply.from_user.id}`\n**Chat ID**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**Your id**: `{message.from_user.id}`\n**chat id**: `{message.chat.id}`"
        )


HELPP_TEXT = """ʏᴏ, ʏᴜᴊɪ ɪᴛᴀᴅᴏʀɪ ʜᴇʀᴇ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ written ᴏɴ ᴘʏʀᴏɢʀᴀᴍ ʟɪʙʀᴀʀʏ 

ᴄʜᴇᴄᴋ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʙᴜᴛᴛᴏɴs ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ 

ʀᴇᴘᴏʀᴛ ʙᴜɢs ᴀᴛ - @fuck_uff_XD"""


@app.on_message(filters.command('help') | filters.command('help@KomiSanRobot'))
def bothelp(_, message):
    if message.chat.type == "private":
        keyboard = []
        for x in help_message:
            keyboard.append([
                InlineKeyboardButton(f"{x['Module_Name']}",
                                     callback_data=f"help:{x['Module_Name']}")
            ])

        app.send_message(message.chat.id,
                         HELPP_TEXT,
                         reply_markup=InlineKeyboardMarkup(keyboard))

    else:
        app.send_photo(message.chat.id,
                       "https://telegra.ph/file/769474503795f6d4f406c.jpg",
                       caption=HELPP_TEXT,
                       reply_markup=InlineKeyboardMarkup([[
                           InlineKeyboardButton(
                               "Pm me for more details",
                               url="t.me/YuJi_ItAdOrI_RoBoT?start=help")
                       ]]))


@app.on_message(filters.command('ul'))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("**Downloading....**")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'Your telegraph [link]({url})', disable_web_page_preview=True)

help_message.append({"Module_Name": "fun"}, )

help_message.append({"Module_Name": "telegraph"})

help_message.append({"Module_Name": "alive"})

help_message.append({"Module_Name": "sexsy"})


class Help_Text:
    helpp = {
          "admin_help": """
➻ /ban - __reply to a user__
➻ /unban __user id or username__
➻ /pin - __reply to a message__
➻ /unpin - __reply to a message__
➻ /id - __to get the user id__
➻ /purge - __purge the messages__

""",
          "sexsy_help": """
➻ /horny - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ʜᴏʀɴʏᴇꜱꜱ

➻ /gay - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ɢᴜʏɴᴇꜱꜱ

➻ /lezbian - ᴄʜᴇᴄᴋ ᴜʀ ᴄᴜʀʀᴇɴᴛ ʟᴀᴢʙɪᴀɴ

➻ /boob - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ʙᴏᴏʙꜱ ꜱɪᴢᴇ

➻ /cute - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴄᴜᴛᴇɴᴇꜱꜱ

➻ /chad - ᴄʜᴇᴄᴋ ʜᴏᴡ ᴄʜᴀᴅ ʏᴏᴜ ᴀʀᴇ
""",
          "meme _help": """
➻ /rmeme - __to get random anime memes__
""",
          "alive_help": """
➻ /alive - __to check bot alive or not__
""",
          "notes_help": """
➻ /addnote note __name text - to add a note__\n•/delnote __NoteName - to delete a note__\n•/getnote __NoteName - get a note or use #notename__\n• /notes - __to get a list of notes in your chats__
""",
          "extra_help": """• /watchorder __anime name - to get watchorder__
➻ /quote - __to get random anime quotes__
➻ /pat - __ to pat someone__
➻ /invitelink - __get invitelink of the current chat__
➻ /whatanime - __reply to a gif or video__
➻ /wall your query - __wallpapers__ 
➻ /paste - __reply to a message__
➻ define word - __get meaning of a word__

""",
          "welcome_help": """• /setwelcome __welcome message - text for welcome__
➻ /clearwelcome - __clear welcome message__""",
        "fun_help": """•/eye
➻ /run""",
        "telegraph_help": """• /ul - __Reply to a photo or video__""",
    }

fk = Help_Text()


def call_back_in_filter(data):
    return filters.create(lambda flt, _, query: flt.data in query.data,
                          data=data)


def is_admin(group_id: int, user_id: int):
    try:
        user_data = bot.get_chat_member(group_id, user_id)
        return bool(user_data.status == 'administrator'
                    or user_data.status == 'creator')
    except:
        # print('Not admin')
        return False


@app.on_callback_query(call_back_in_filter('help'))
def callback_help(_, query):

    if not query.data == "help":
        try:
            for x in help_message:
                module = query.data.split(':')[1]
                module_name = f'{module}_help'
                query.message.edit(fk.helpp.get(module_name),
                                   reply_markup=InlineKeyboardMarkup([[
                                       InlineKeyboardButton(
                                           "Back", callback_data="help:back")
                                   ]]))

            msg = query.message
            callback_module_name = query.data.split(':')[1]
            txt = helptext_

            query.message.edit(txt)
        except Exception as e:
            app.send_message(-1001954317013, f"error in help:\n\n{e}")

    if query.data == "help":
        keyboard = []
        for x in help_message:
            keyboard.append([
                InlineKeyboardButton(x['Module_Name'],
                                     callback_data=f"help:{x['Module_Name']}")
            ])

        query.message.edit(HELPP_TEXT,
                           reply_markup=InlineKeyboardMarkup(keyboard))

    if query.data.split(":")[1] == "back":
        keyboard = []
        for x in help_message:
            keyboard.append([
                InlineKeyboardButton(x['Module_Name'],
                                     callback_data=f"help:{x['Module_Name']}")
            ])
        try:
            query.message.edit(HELPP_TEXT,
                               reply_markup=InlineKeyboardMarkup(keyboard))
        except:
            pass



@app.on_message(filters.command("info"))
def info(_, message):
    if message.text == "/info":
        user = message.from_user.id
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    if not message.reply_to_message and message.text != "/info" and user.isnumeric(
    ):
        user = message.text.split(" ")[1]

    if not message.reply_to_message and message.text != "/info" and not user.isnumeric(
    ):
        k = app.get_users(message.text.split(" ")[1])
        user = k.id

    if user == OWNER:
        status = "This Person is my Owner"

    elif user in sudos:
        status = "This person is one of my Sudo users !"

    else:
        status = "member"

    pfp_count = app.get_profile_photos_count(user)

    if not pfp_count == 0:
        pfp = app.get_profile_photos(user, limit=1)
        pfp_ = pfp[0]['thumbs'][0]['file_id']

    foo = app.get_users(user)
    data = f"""**First Name** : {foo.first_name}
**Last Name**: {foo.last_name}
**Telegram Id**: {foo.id}
**PermaLink**: {foo.mention(foo.first_name)}
**is_bot**: {foo.is_bot}
**Status**: {status}
"""

    if pfp_count != 0:
        message.reply_photo(pfp_, caption=data)

    else:
        message.reply_text(data)


sudos = [6647321265]

print("yooo babe im alive.")

app.run()
