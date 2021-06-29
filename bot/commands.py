import logging
import sys
import time

import discord
from discord.ext import commands
from discord import Embed

from bot import constants

log = logging.getLogger(__name__)


class Commands(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command(name="hello", aliases=("hey", "hlo",))
    async def hello_world(self, ctx: commands.Context):
        await ctx.message.add_reaction("👋")


    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        embed = Embed(
            title="Pong!",
            color=constants.Colours.blue)
        embed.add_field(name=f"Gateway Latency : ", value=f"{round(self.bot.latency * 1000)} ms", inline=False)
        embed.add_field(name=f"Discord API latency :", value=f"{str(end_time - start_time)[2:5]} ms", inline=False)

        await message.edit(content="", embed=embed)


    @commands.command(name="quit", aliases=("close", "bye", "logout", ))
    async def quit(self, ctx: commands.Context):
        is_owner = await ctx.bot.is_owner(ctx.author)
        if is_owner:
            await ctx.message.add_reaction("👋")
            await self.bot.close()
            log.exception(f"{self.bot.user} had logged out by the bot author")
            sys.exit(0)


    @commands.command(name="dm")
    async def send_dm(self, ctx, member: discord.Member, *, content):
        channel = await member.create_dm()
        icon = ctx.message.author.avatar_url_as(format="png")


        embed = Embed(description=content, color=constants.Colours.orange)
        embed.set_author(name=f"[{ctx.message.author}](https://discordapp.com/users/{ctx.message.author.id})", icon_url=icon)
        await channel.send(embed=embed)


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
