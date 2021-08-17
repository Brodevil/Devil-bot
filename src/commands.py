import asyncio
import logging
from os import system

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
        await ctx.confirm_action()

        code = acute_remover(str(code))
        output = eval(code)
        await ctx.reply(f"```{output}```")


    @commands.is_owner()
    @commands.command(name="cmd", aliases=("os", "shell", "bash", ))
    async def cmd(self, ctx: commands.Context, *, command: str):
        await ctx.confirm_action()
    
        command = acute_remover(str(command))
        system(command)
        await ctx.message.add_reaction("👌")


    @commands.command(name='devil', aliases=("mr_devil",))
    async def devil(self, ctx: commands.Context):
        async with ctx.typing():
            embed = discord.Embed(color=Colours.soft_red)
            embed.set_image(url="https://bit.ly/3iNqBjp")
            await ctx.send(embed=embed)
    
    @commands.is_owner()
    @commands.command(name="send", aliases=("send_msg", "repeat"))
    async def repeat(self, ctx: commands.Context, *, msg: str):
        await ctx.send(msg)



def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot))

