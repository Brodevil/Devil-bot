import logging
import sys
import time
from pprint import pprint

import discord
from discord.ext import commands
from discord import Embed

from src import constants
from src.utils.time import time_since


log = logging.getLogger(__name__)


class Commands(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="hello", aliases=("hey", "hlo",))
    async def hello_world(self, ctx: commands.Context):
        await ctx.message.add_reaction("👋")



def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot))
