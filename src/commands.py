import logging
import typing 

import discord
from discord.ext import commands
from discord import Embed

from src import constants               # noqa
from src.utils.time import time_since   # noqa


log = logging.getLogger(__name__)


class Commands(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="hello", aliases=("hey", "hlo", "test"))
    async def hello_world(self, ctx: commands.Context):
        await ctx.message.add_reaction("👋")
        await ctx.reply("Hello")



def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot))
