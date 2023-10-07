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
from pyrogram.types.messages_and_media import message
from bs4 import BeautifulSoup
import urllib
import glob
import io
import os
import re
import aiohttp
import urllib.request
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
from PIL import Image
from search_engine_parser import GoogleSearch
import bs4
import html2text
from bing_image_downloader import downloader
from telethon import *
from telethon.tl import functions
from telethon.tl import types
from telethon.tl.types import *

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

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]


@app(pattern="^/google (.*)")
async def _(event):
    if event.fwd_from:
        return
    
    webevent = await event.reply("searching........")
    match = event.pattern_match.group(1)
    page = re.findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"❍[{title}]({link})\n**{desc}**\n\n"
        except IndexError:
            break
    await webevent.edit(
        "**Search Query:**\n`" + match + "`\n\n**Results:**\n" + msg, link_preview=False
    )

@app(pattern="^/img (.*)")
async def img_sampler(event):
    if event.fwd_from:
        return
    
    query = event.pattern_match.group(1)
    jit = f'"{query}"'
    downloader.download(
        jit,
        limit=4,
        output_dir="store",
        adult_filter_off=False,
        force_replace=False,
        timeout=60,
    )
    os.chdir(f'./store/"{query}"')
    types = ("*.png", "*.jpeg", "*.jpg")  # the tuple of file types
    files_grabbed = []
    for files in types:
        files_grabbed.extend(glob.glob(files))
    await tbot.send_file(event.chat_id, files_grabbed, reply_to=event.id)
    os.chdir("/app")
    os.system("rm -rf store")


opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]


@app(pattern=r"^/reverse(?: |$)(\d*)")
async def okgoogle(img):
    """ For .reverse command, Google search images and stickers. """
    if os.path.isfile("okgoogle.png"):
        os.remove("okgoogle.png")
    
    message = await img.get_reply_message()
    if message and message.media:
        photo = io.BytesIO()
        await app.download_media(message, photo)
    else:
        await img.reply("`Reply to photo or sticker nigger.`")
        return

    if photo:
        dev = await img.reply("`Processing...`")
        try:
            image = Image.open(photo)
        except OSError:
            await dev.edit("`Unsupported sexuality, most likely.`")
            return
        name = "okgoogle.png"
        image.save(name, "PNG")
        image.close()
        # https://stackoverflow.com/questions/23270175/google-reverse-image-search-using-post-request#28792943
        searchUrl = "https://www.google.com/searchbyimage/upload"
        multipart = {"encoded_image": (name, open(name, "rb")), "image_content": ""}
        response = requests.post(searchUrl, files=multipart, allow_redirects=False)
        fetchUrl = response.headers["Location"]

        if response != 400:
            await dev.edit(
                "`Image successfully uploaded to Google. Maybe.`"
                "\n`Parsing source now. Maybe.`"
            )
        else:
            await dev.edit("`Google told me to fuck off.`")
            return

        os.remove(name)
        match = await ParseSauce(fetchUrl + "&preferences?hl=en&fg=1#languages")
        guess = match["best_guess"]
        imgspage = match["similar_images"]

        if guess and imgspage:
            await dev.edit(f"[{guess}]({fetchUrl})\n\n`Looking for this Image...`")
        else:
            await dev.edit("`Can't find this piece of shit.`")
            return

        if img.pattern_match.group(1):
            lim = img.pattern_match.group(1)
        else:
            lim = 3
        images = await scam(match, lim)
        yeet = []
        for i in images:
            k = requests.get(i)
            yeet.append(k.content)
        try:
            await app.send_file(
                entity=await tbot.get_input_entity(img.chat_id),
                file=yeet,
                reply_to=img,
            )
        except TypeError:
            pass
        await dev.edit(
            f"[{guess}]({fetchUrl})\n\n[Visually similar images]({imgspage})"
        )


async def ParseSauce(googleurl):
    """Parse/Scrape the HTML code for the info we want."""

    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, "html.parser")

    results = {"similar_images": "", "best_guess": ""}

    try:
        for similar_image in soup.findAll("input", {"class": "gLFyf"}):
            url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(
                similar_image.get("value")
            )
            results["similar_images"] = url
    except BaseException:
        pass

    for best_guess in soup.findAll("div", attrs={"class": "r5a77d"}):
        results["best_guess"] = best_guess.get_text()

    return results


async def scam(results, lim):

    single = opener.open(results["similar_images"]).read()
    decoded = single.decode("utf-8")

    imglinks = []
    counter = 0

    pattern = r"^,\[\"(.*[.png|.jpg|.jpeg])\",[0-9]+,[0-9]+\]$"
    oboi = re.findall(pattern, decoded, re.I | re.M)

    for imglink in oboi:
        counter += 1
        if counter < int(lim):
            imglinks.append(imglink)
        else:
            break

    return imglinks


@app(pattern="^/app (.*)")
async def apk(e):
    
    try:
        app_name = e.pattern_match.group(1)
        remove_space = app_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get(
            "https://play.google.com/store/search?q=" + final_name + "&c=apps"
        )
        lnk = str(page.status_code)
        soup = bs4.BeautifulSoup(page.content, "lxml", from_encoding="utf-8")
        results = soup.findAll("div", "ZmHEEd")
        app_name = (
            results[0].findNext("div", "Vpfmgd").findNext("div", "WsMG1c nnK0zc").text
        )
        app_dev = results[0].findNext("div", "Vpfmgd").findNext("div", "KoLSrc").text
        app_dev_link = (
            "https://play.google.com"
            + results[0].findNext("div", "Vpfmgd").findNext("a", "mnKHRc")["href"]
        )
        app_rating = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "pf5lIe")
            .find("div")["aria-label"]
        )
        app_link = (
            "https://play.google.com"
            + results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "vU6FJ p63iDd")
            .a["href"]
        )
        app_icon = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "uzcko")
            .img["data-src"]
        )
        app_details = "<a href='" + app_icon + "'>📲&#8203;</a>"
        app_details += " <b>" + app_name + "</b>"
        app_details += (
            "\n\n<code>Developer :</code> <a href='"
            + app_dev_link
            + "'>"
            + app_dev
            + "</a>"
        )
        app_details += "\n<code>Rating :</code> " + app_rating.replace(
            "Rated ", "⭐ "
        ).replace(" out of ", "/").replace(" stars", "", 1).replace(
            " stars", "⭐ "
        ).replace(
            "five", "5"
        )
        app_details += (
            "\n<code>Features :</code> <a href='"
            + app_link
            + "'>View in Play Store</a>"
        )
        app_details += "\n\n===> GroupMenter <==="
        await e.reply(app_details, link_preview=True, parse_mode="HTML")
    except IndexError:
        await e.reply("No result found in search. Please enter **Valid app name**")
    except Exception as err:
        await e.reply("Exception Occured:- " + str(err))


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

welcome_db = pymongo.MongoClient(db_url)['Welcome']['WelcomeX']


@app.on_message(filters.command('setwelcome'))
def setwelcome(_, message):
    if is_admin(message.chat.id, message.from_user.id):
        try:
            ids = []
            all_welcome = welcome_db.find()
            for x in all_welcome:
                ids.append(x['chat_id'])

            if message.chat.id not in ids:
                msg = message.text.replace(message.text.split(' ')[0], "")
                welcome_db.insert_one({
                    "type": "welcome",
                    "chat_id": message.chat.id,
                    "welcome_text": msg
                })
                message.reply("Done!")
            else:
                message.reply("use /clearwelcome first!")

        except Exception as e:
            app.send_message(-1001646296281, f"error in setwelcome:\n]n{e}")


@app.on_message(filters.command("clearwelcome"))
def clearwelcome(_, message):
    if is_admin(message.chat.id, message.from_user.id):
        welcome_db.delete_many({"chat_id": message.chat.id})
        message.reply("Ok!")


@app.on_message(filters.new_chat_members)
def welcome(_, message):
    try:
        welcome_msg = welcome_db.find_one({"chat_id": message.chat.id
                                           })['welcome_text'] or ""
        if not welcome_msg == "":
            message.reply_text(welcome_msg)

        else:
            message.reply("Hello")

    except Exception as e:
        app.send_message(-1001954317013, f"error in welcome:\n]n{e}")


help_message.append({"Module_Name": "welcome"})

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
