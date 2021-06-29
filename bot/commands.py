import logging
import sys
import time

import discord
from discord.ext import commands

from bot import constants

log = logging.getLogger(__name__)


class Commands(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="hello", aliases=("hey", "hlo",))
    async def hello_world(self, ctx: commands.Context):
        await ctx.add_reaction("\:wave:")

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        embed = discord.Embed(
            title="Pong!",
            color=constants.Colours.blue)
        embed.add_field(name=f"Gateway Latency : ", value=f"{round(self.bot.latency * 1000)} ms", inline=False)
        embed.add_field(name=f"Discord API latency :", value=f"{end_time - start_time: .3f} ms", inline=False)

        await message.edit(content="", embed=embed)

    @commands.command(name="quit", aliases=("close", "bye"))
    async def quit(self, ctx: commands.Context):
        is_owner = await ctx.bot.is_owner(ctx.author)
        if is_owner:
            await ctx.reply("Logged out!")
            await self.bot.close()
            log.exception(f"{self.bot.user} had logged out by the bot author")
            sys.exit(0)

    @commands.command(name="dm")
    async def send_dm(self, ctx, member: discord.Member, *, content):
        channel = await member.create_dm()
        await channel.send(f">>> **{content}**")

    @commands.command(name="setstatus", aliases=("status", "ss",))
    async def setstatus(self, ctx: commands.Context, *, text: str):
        is_owner = await ctx.bot.is_owner(ctx.author)
        if is_owner:
            await self.bot.change_presence(activity=discord.Game(name=text))

    @commands.command(pass_context=True, name="nick", aliases=("chnick", "nickname"))
    async def chnick(self, ctx, member: discord.Member, *, nick):
        await member.edit(nick=nick)


def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot))
