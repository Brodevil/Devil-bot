import logging
import json

from src.bot import bot             
from src.constants import Client     


log = logging.getLogger('discord')
log.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='devil.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s'))
log.addHandler(handler)


# extensions loading
with open("src/resource/_cogs.json", "rb") as _cog:
    _cog = json.load(_cog)
    _cog = _cog["cogs"]


bot.load_extensions(_cog)

bot.run(Client.TOKEN)
