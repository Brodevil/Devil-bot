import logging

import discord

from bot.bot import bot
from bot.constants import Client


logging.getLogger(__name__)


cogs = [
    "bot.exts.backend.logging",
    "bot.commands"

]

for cog in cogs:
    bot.load_extension(cog)


bot.run(Client.TOKEN)
