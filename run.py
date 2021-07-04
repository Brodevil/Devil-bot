import logging
import sys

import traceback

from src.bot import bot
from src.constants import Client


log = logging.getLogger('discord')
log.setLevel(logging.DEBUG)
handler = log.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
log.addHandler(handler)


# extensions loading


bot.run(Client.TOKEN)
