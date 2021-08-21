from logging import getLogger

import discord
from discord.ext.commands import Context, Bot, Cog, command
from discord.ext import commands

from src.constants import Colours
import pyjoke


log = getLogger(__name__)


class Laugh(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
    
    @command(name="joke", aliases=("text_joke", "small_joke", ))
    async def shortJokes(self, ctx: Context):
        pass



def setup(bot: Bot) -> None:
    bot.add_cog(Laugh(bot))
