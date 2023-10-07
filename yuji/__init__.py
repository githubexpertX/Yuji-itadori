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

app = Client('bot',
             api_id=os.environ.get('28731705'),
             api_hash=os.environ['7ed8bb45ea845bef652aa0606584f413'],
             bot_token=os.environ['6561918588:AAE74I_F1bpCi6SltNQHTYClgpM_AThQmNk'],
             plugins=dict(root=f"yuji/plugins"))
