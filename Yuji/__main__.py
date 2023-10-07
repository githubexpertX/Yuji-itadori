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
from random import choice
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
from pyrogram.types.messages_and_media import message

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual API credentials
api_id = '28731705'
api_hash = '7ed8bb45ea845bef652aa0606584f413'

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '6561918588:AAE74I_F1bpCi6SltNQHTYClgpM_AThQmNk'

# Create a Pyrogram client instance
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


ALIVE_PIC = getenv("ALIVE_PIC", 'https://te.legra.ph/file/403acffa5ca195e17112b.jpg')

HELPP_TEXT = ("ʜᴇʟʟᴏ [sɪʀ](tg://settings)\n\nʏᴜᴊɪ ɪᴛᴀᴅᴏʀɪ ʜᴇʀᴇ\nɪᴍ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ\nɪ ᴡɪʟʟ ʜᴇʟᴘ ʏᴏᴜ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ \n\nɪғ ʏᴏᴜ ɴᴏᴛɪᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴡɪᴛʜ ᴛʜᴇ ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ ʀᴇᴘᴏʀᴛ ɪᴛ ɪɴ ᴍʏ [sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ](@fuck_uff_XD).")

EMOJIOS = [ 
      "ʏᴏᴏᴏᴏ ♡"]

help_message = []

OWNER = 65299686966529968696


      
      
      
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
                               url="t.me/@Testing_pydroid3_robot?start=help")
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


class Help_Text:
    helpp = {
        "admin_help": """
• /ban - __reply to a user__
• /unban __user id or username__
• /pin - __reply to a message__
• /unpin - __reply to a message__
• /id - __to get the user id__
• /purge - __purge the messages__

""",
        "meme_help": """
• /rmeme - __to get random anime memes__
""",
        "notes_help":
        '• /addnote note __name text - to add a note__\n•/delnote __NoteName - to delete a note__\n•/getnote __NoteName - get a note or use #notename__\n• /notes - __to get a list of notes in your chats__',
        "extra_help": """• /watchorder __anime name - to get watchorder__
• /quote - __to get random anime quotes__
• /pat - __ to pat someone__
• /invitelink - __get invitelink of the current chat__
• /whatanime - __reply to a gif or video__
• /wall your query - __wallpapers__ 
• /paste - __reply to a message__
• define word - __get meaning of a word__

""",
        "welcome_help": """• /setwelcome __welcome message - text for welcome__
• /clearwelcome - __clear welcome message__""",
        "fun_help": """•/eye
•/run""",
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


def is_admin(group_id: int, user_id: int):
    try:
        user_data = bot.get_chat_member(group_id, user_id)
        if user_data.status == 'administrator' or user_data.status == 'creator':
            # print(f'is admin user_data : {user_data}')
            return True
        else:
            # print('Not admin')
            return False
    except:
        # print('Not admin')
        return False


@app.on_callback_query(call_back_in_filter("admin"))
def admeme_callback(_, query):
    scammer = query.data.split(":")[2]
    if is_admin(query.message.chat.id,
                query.from_user.id) and query.data.split(":")[1] == "unban":
        app.unban_chat_member(query.message.chat.id, scammer)
        query.answer('Unbanned!')
        query.message.edit(f'unbanned [{scammer}](tg://user?id={scammer})',
                           parse_mode='markdown')
    else:
        message.reply('You are not admin!')


@app.on_message(filters.command('ban'))
def ban(_, message):
    # scammer = reply.from_user.id
    reply = message.reply_to_message
    if is_admin(
            message.chat.id, message.from_user.id
    ) and not reply.from_user.id in sudos and reply.from_user.id != 825664681:
        message.chat.ban_member(message.reply_to_message.from_user.id)
        app.send_message(
            message.chat.id,
            f"Banned! {reply.from_user.username}",
            parse_mode="markdown",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "Unban",
                        callback_data=
                        f"admin:unban:{message.reply_to_message.from_user.id}")
                ],
            ]))

    elif reply.from_user.id == 6647321265:
        message.reply('This Person is my owner!')

    elif reply.from_user.id in sudos:
        message.reply("This Person is my sudo user !")

    elif message.from_user.id == 6647321265 or message.from_user.id in sudos:
        user = reply.from_user.username if not None else reply.from_user.id
        app.kick_chat_member(message.chat.id,
                             message.reply_to_message.from_user.id)
        app.send_message(
            message.chat.id,
            f"Banned! {user}",
            parse_mode="markdown",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "Unban",
                        callback_data=
                        f"admin:unban:{message.reply_to_message.from_user.id}")
                ],
            ]))
    else:
        message.reply('You are not admin')


@app.on_message(filters.command('unban'))
def unban(_, message):
    try:
        user = message.text.split(" ")[1]
        if is_admin(message.chat.id, message.from_user.id):
            app.unban_chat_member(message.chat.id, user)
            message.reply('Unbanned!')
        if not is_admin(message.chat.id, message.from_user.id):
            message.reply("You aren't admin!")
        else:
            message.reply("I can't unban that uset")
    except Exception as e:
        message.reply(e)


@app.on_message(filters.command('pin'))
def pin(_, message):
    if message.reply_to_message:
        message_id = message.reply_to_message.message_id
        if is_admin(message.chat.id, message.from_user.id):
            app.pin_chat_message(message.chat.id, message_id)

    elif not is_admin(message.chat.id, message.from_user.id):
        message.reply("You're not admin")
    elif not message.reply_to_message:
        message.reply("Reply to a message")
    else:
        message.reply("Make sure I'm admin and Can Pin Messages")


@app.on_message(filters.command('unpin'))
def unpin(_, message):
    if message.reply_to_message:
        message_id = message.reply_to_message.message_id
        if is_admin(message.chat.id, message.from_user.id):
            bot.unpin_chat_message(message.chat.id, message_id)
    elif not is_admin(message.chat.id, message.from_user.id):
        message.reply("You're not admin")
    elif not message.reply_to_message:

        message.reply("Reply to a message")
    else:
        message.reply("Make sure I'm admin and Can Pin Messages")


@app.on_message(filters.command('kick'))
def kick(_, message):
    reply = message.reply_to_message
    if is_admin(message.chat.id, message.from_user.id) and reply:
        app.kick_chat_member(message.chat.id,
                             message.reply_to_message.from_user.id)
        app.unban_chat_member(message.chat.id,
                              message.reply_to_message.from_user.id)
        message.reply('kick @{} !'.format(
            message.reply_to_message.from_user.username))
    elif reply.from_user.id == 6647321265:
        message.reply('This Person is my owner!')
    else:
        message.reply('You are not admin')


@app.on_message(filters.command('promote'))
def promote(_, message):
    if is_admin(message.chat.id,
                message.from_user.id) and message.reply_to_message:
        message.chat.promote_member(message.reply_to_message.from_user.id)
        message.reply('Promoted @{} !'.format(
            message.reply_to_message.from_user.username))


@app.on_message(filters.command('demote'))
def demote(_, message):
    if is_admin(message.chat.id,
                message.from_user.id) and message.reply_to_message:
        message.chat.promote_member(message.reply_to_message.from_user.id,
                                    False, False, False, False, False, False,
                                    False, False)
        message.reply('Demoted @{} !'.format(
            message.reply_to_message.from_user.username))


@app.on_message(filters.command("cban") & filters.group)
def bam(_, message):
    try:
        user = message.reply_to_message
        admeme = app.get_users(message.from_user.id)
        if admeme.status == "creator" or "administrator" and user.sender_chat:
            bot.kick_chat_member(message.chat.id, user.sender_chat.id)
            message.reply_text("Banned {}".format(user.sender_chat.id))

    except Exception as e:
        from nksama.utils.sendlog import send_log
        send_log(e, "cban")


@app.on_message(filters.command("cunban") & filters.group)
def bam(_, message):
    user = message.reply_to_message
    admeme = app.get_users(message.from_user.id)
    if admeme.status == "creator" or "administrator" and user.sender_chat:
        app.unban_chat_member(message.chat.id, user.sender_chat.id)
        message.reply_text("UNBanned {}".format(user.sender_chat.id))


@app.on_message(filters.command("purge"))
def purge(_, m: Message):
    if is_admin(m.chat.id, m.from_user.id) and m.reply_to_message:
        msgs = []

        for x in range(m.reply_to_message.message_id, m.message_id):
            msgs.append(x)

        app.delete_messages(m.chat.id, msgs)
        m.reply("Purge Complete")

    elif not m.reply_to_message and is_admin(m.chat.id, m.from_user.id):
        m.reply("Reply to a Message!")

    else:
        m.reply("reply to a message")


help_message.append({'Module_Name': 'admin'})

    

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
