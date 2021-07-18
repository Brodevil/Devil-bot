import logging
import json 

from src.bot import bot             # noqa
from src.constants import Client     # noqa
from discord.ext import command     # noqa


log = logging.getLogger('discord')
log.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
log.addHandler(handler)

@bot.event()
async def on_message(message):
    if message.author == bot.user:
        return
    
    elif message.guild:
        print(f"Author : {message.author} \nServer :{message.guild.name} \nMessage : {message.content}\n\n")
    else:
        print(f"DM User : {message.author} \nMessage : {message.content}\n\n")


# extensions loading
with open("src\\resource\\extensions\\_cogs.json") as _cog:
    _cog = json.load(_cog)
    _cog = list(_cog["cogs"])

bot.loading_extensions(_cog)

bot.run(Client.TOKEN)
