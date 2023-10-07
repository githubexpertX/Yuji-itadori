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
# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual API credentials
api_id = '28731705'
api_hash = '7ed8bb45ea845bef652aa0606584f413'

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '6561918588:AAE74I_F1bpCi6SltNQHTYClgpM_AThQmNk'

# Create a Pyrogram client instance
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command('noi'))
async def handle_start(client, message):
    # Extract the information of the user who sent the /start command
    user = message.from_user
    first_name = user.first_name if user.first_name else ''
    last_name = user.last_name if user.last_name else ''

    # Send a welcome message to the user
    await message.reply_text(f"Hi {first_name} {last_name}! Welcome to the bot.")

# Start the client
ALIVE_PIC = getenv("ALIVE_PIC", 'https://te.legra.ph/file/af569efd713e32cf332a3.jpg')

HELPP_TEXT = """
 hello kya haal hai bhai kya sab ho raha hai 
 
 """

EMOJIOS = [ 
      "ʏᴏᴏᴏᴏ ♡"]
      
      
      
@app.on_message(filters.command(["start"]))
async def restart(client, m: Message):
    accha = await m.reply_text(
                text = random.choice(EMOJIOS),
    )
    await asyncio.sleep(0.6)
    await accha.edit("ʟᴇ ᴍᴇ ɪɴᴛʀᴏᴅᴜᴄᴇ ᴍʏsᴇʟғ ➳➳")
    await asyncio.sleep(0.7)
    await accha.edit("ɪ'ᴍ ʏᴜᴊɪ ɪᴛᴀᴅᴏʀɪ ♡")
    await asyncio.sleep(0.8)
    await accha.edit("ɪ ᴀᴍ ᴀ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ. ✦")
    await asyncio.sleep(0.5)
    await accha.delete()
    accha = await m.reply_photo(ALIVE_PIC,
    caption = HELPP_TEXT
                )
    
    
print("   ,,,,,,,,,,\n,,,,,,,,,DOWLOADING,,,,,,,,,\n,,,,,,,,,,,,      im alive babe")
     



app.run()
