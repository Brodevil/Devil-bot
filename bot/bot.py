import logging

from discord.ext import commands
import discord 

from bot.constants import Channels
from bot.exts.backend.logging import setup

logging.getLogger(__name__)


class Bot(commands.bot):
    def __init__(self):
        super().__init__()




    async def on_ready(self):
        print('Bot had Logged in as :- {0} ({0.id})'.format(self.user))
        print('------' * 10)

