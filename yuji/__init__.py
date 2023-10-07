from pyrogram import filters, Client
from redis import Redis
import os

help_message = []

# class bot(Client):
#     super().__init__(
#         'bot',
#                      api_id=os.environ.get('API_ID'),
#                      api_hash=os.environ['API_HASH'],
#                      bot_token=os.environ['BOT_TOKEN'],
#                      plugins=dict(root=f"{__name__}/plugins"))

#     def add_cmd(module, help):
#         help_message.append({"Module_Name": module})
#         help.update({f"{module}_help": help})

api_id = '28731705'
api_hash = '7ed8bb45ea845bef652aa0606584f413'

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '6561918588:AAE74I_F1bpCi6SltNQHTYClgpM_AThQmNk'


# Create a Pyrogram client instance
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
