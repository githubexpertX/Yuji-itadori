import logging
from pyrogram import Client, filters
from pyrogram.types import *
import random
import asyncio
from os import getenv
from pyrogram import Client, filters
from pyrogram.types import *
import random
import asyncio
from redis import Redis
from os import getenv
from pyrogram import filters
import os
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
from pyrogram import filters
from pyrogram.types import Message
from pymongo import MongoClient
from Yuji.db import MONGO_URL as db_url

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual API credentials
api_id = '28731705'
api_hash = '7ed8bb45ea845bef652aa0606584f413'

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '6561918588:AAE74I_F1bpCi6SltNQHTYClgpM_AThQmNk'

# Create a Pyrogram client instance
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(
    filters.command('start') | filters.command('start@KomiSanRobot'))
def start(_, message):
    try:
        if message.chat.type == "private":
            users = col.find({})
            mfs = []
            for x in users:
                mfs.append(x['user_id'])
            if message.from_user.id not in mfs:
                user = {"type": "user", "user_id": message.from_user.id}
                col.insert_one(user)

        else:
            users = grps.find({})
            mfs = []
            for x in users:
                mfs.append(x['chat_id'])
            if message.chat.id not in mfs:
                grp = {"type": "group", "chat_id": message.chat.id}
                grps.insert_one(grp)

    except Exception as e:
        app.send_message(-1001954317013, f"error in adding stats:\n\n{e}")

    if message.chat.type == "private" and not "help" in message.text:

        app.send_message(
            message.chat.id,
            f"ʜᴇʟʟᴏ {message.from_user.mention}\n\nʏᴜᴊɪ ɪᴛᴀᴅᴏʀɪ ʜᴇʀᴇ\nɪᴍ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ\nɪ ᴡɪʟʟ ʜᴇʟᴘ ʏᴏᴜ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ \n\nɪғ ʏᴏᴜ ɴᴏᴛɪᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴡɪᴛʜ ᴛʜᴇ ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ ʀᴇᴘᴏʀᴛ ɪᴛ ɪɴ ᴍʏ [sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ](https://t.me/NiGhT_StARs_ll)",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton('help', callback_data="help")]]))
    if "help" in message.text:
        app.send_message(message.chat.id,
                         "Help",
                         reply_markup=InlineKeyboardMarkup([[
                             InlineKeyboardButton('help', callback_data="help")
                         ]]))
    if not message.chat.type == "private":
        message.reply("ʜᴇʟʟᴏ ᴛʜᴇʀᴇ ɪᴍ ʏᴜᴊɪ ɪᴛᴀᴅᴏʀɪ")


users_db = MongoClient(db_url)['users']
col = users_db['USER']
grps = users_db['GROUPS']


@app.on_message(filters.command("stats"))
async def stats(_, m: Message):
    users = col.find({})
    mfs = []
    for x in users:
        mfs.append(x['user_id'])

    total = len(mfs)

    grp = grps.find({})
    grps_ = []
    for x in grp:
        grps_.append(x['chat_id'])

    total_ = len(grps_)

    await m.reply_text(f"👥 Total Users: `{total}`\n💭 Total Groups: `{total_}`")

print("yooo babe im alive.")

app.run()
