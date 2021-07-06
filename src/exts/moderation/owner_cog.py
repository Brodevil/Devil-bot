import logging 
import sys

from discord.ext import commands
from discord import Embed
import discord 

import asyncio

from src import constants
from src.exts.utils import converter


log = logging.getLogger(__name__)
__all__ = ("Bot_Controls", "setup")


class Bot_Controls(commands.Cog):
    """Bot Control by owner of the Bot"""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    
    @commands.command(name="quit", aliases=("close", "bye", "logout",))
    @commands.is_owner()
    async def quit(self, ctx: commands.Context):
        react_yes = await ctx.message.add_reaction("✅")

        embed = Embed(title="Logged Out!", color=constants.Colours.soft_green)
        await ctx.send(embed=embed)

        await self.bot.logout()
        await self.bot.close()
        log.exception(f"{self.bot.user} had logged out by the bot author")
        sys.exit(0)
        
    
    @commands.command(name="status", aliases=("set_status", ))
    @commands.is_owner()
    async def setstatus(self, ctx: commands.Context, *, text: str):
        await self.bot.change_presence(activity=discord.Game(name=text))
        await ctx.message.add_reaction("👍")

        log.info(f"Bot's status changed to  :- {text}")
        

    @commands.command(name="dm")
    @commands.is_owner()
    async def send_dm(self, ctx, member: discord.Member, *, content, show_name: str):
        """ Direct Messaging the user """
        channel = await member.create_dm()
        show_name = converter.msg_bool(show_name)

        if show_name:
            name = ctx.message.author.name
            url = f"https://discordapp.com/users/{ctx.message.author.id}"
            icon = ctx.message.author.avatar_url_as(format="png")

        else:
            name = self.bot.user.name
            url = f"https://discordapp.com/users/{self.bot.user.id}"
            icon = self.bot.user.avatar_url_as(format="png")
        

        embed = discord.Embed(description=content, color=constants.Colours.soft_red)
        embed.set_author(name=name, icon_url=icon, url=url)

        await channel.send(embed=embed)
        await ctx.message.add_reaction("👌")

        

def setup(bot: commands.Bot):
    bot.add_cog(Bot_Controls(bot))