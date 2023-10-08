import logging
from pyrogram import Client, filters
from pyrogram.types import *
import random
import asyncio
from bs4 import BeautifulSoup
from os import getenv
from pyrogram.types import Message
from telethon import TelegramClient
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
