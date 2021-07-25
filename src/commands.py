import asyncio
import logging

from discord.ext import commands
import discord

from src.constants import Colours
from src.exts.utils.converter import acute_remover


log = logging.getLogger(__name__)


class Commands(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="hello", aliases=("hey", "hlo", "test"))
    async def hello_world(self, ctx: commands.Context):
        await ctx.message.add_reaction("👋")


    @commands.is_owner()
    @commands.command(name="eval", aliases=("e", ))
    async def eval_cog(self, ctx: commands.Contextm, code):
        code = acute_remover(code)
        output = eval(code)
        ctx.reply(f"```{output}```")


def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot))

