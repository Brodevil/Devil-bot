import asyncio
import logging

from discord.ext import commands
import discord

from src.constants import Colours
from src.exts.utils.converter import acute_remover
from src.bot import bot


log = logging.getLogger(__name__)


class Commands(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="hello", aliases=("hey", "hlo", "test"))
    async def hello_world(self, ctx: commands.Context):
        await ctx.message.add_reaction("👋")
        # await ctx.reply("Hello World!")


    @commands.is_owner()
    @commands.command(name="eval", aliases=("e", ))
    async def eval_cog(self, ctx: commands.Context, code: str):
        code = acute_remover(str(code))
        output = eval(code)
        await ctx.reply(f"```{output}```")


def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot))

