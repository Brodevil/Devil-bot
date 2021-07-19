import logging 
import sys

from discord.ext import commands
from discord import Embed
import discord 

import asyncio
from typing import Literal
import json

from src import constants                   # noqa
from src.utils import converter        # noqa


log = logging.getLogger(__name__)
__all__ = ("Bot_Controls", "setup")


class Bot_Controls(commands.Cog):
    """Bot Control by owner of the Bot"""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.is_owner()
    @commands.command(name="quit", aliases=("close", "bye", "logout",))
    async def quit(self, ctx: commands.Context):
        """Logout the bot!"""
        await ctx.message.add_reaction("✅")

        embed = Embed(title="🏃 Logged Out!", color=constants.Colours.soft_green)
        await ctx.send(embed=embed)

        await self.bot.logout()
        await self.bot.close()
        log.exception(f"{self.bot.user} had logged out by the bot author")
        sys.exit(0)
        
    
    @commands.is_owner()
    @commands.command(name="dm")
    async def send_dm(self, ctx, User: discord.Member, show_name: Literal[converter.total_bools] = True, *, content):
        """ Direct Messaging the user """
        channel = await User.create_dm()
        show_name = converter.msg_bool(show_name)
        
        if show_name:
            name = ctx.message.author.name
            url = f"https://discordapp.com/users/{ctx.message.author.id}"
            icon = ctx.message.author.avatar_url_as(format="png")

        elif not show_name:
            name = self.bot.user.name
            url = f"https://discordapp.com/users/{self.bot.user.id}"
            icon = self.bot.user.avatar_url_as(format="png")
        

        embed = discord.Embed(description=content, color=constants.Colours.soft_red)
        embed.set_author(name=name, icon_url=icon, url=url)

        await channel.send(embed=embed)
        await ctx.message.add_reaction("👌")
    

    @commands.is_owner()
    @commands.command(name="status", aliases=("set_status", "activity"))
    async def setstatus(self, ctx: commands.Context, status: Optional[str] = None, run_loop : Optional[converter.msg_bool] = True, *, text: str):
        """Adding the more status and run it"""
        
        if status is not None and status in ['dnd', 'do_not_disturb', 'idle', 'invisible', 'offline', 'online']:
            self.bot.status = status
        else:
            self.bot.status = discord.Status.online


        if run_loop == False:
            self.bot.change_status.cancel()
            await self.bot.change_presence(status=self.bot.status, activity=discord.Game(name=text))
            log.info(f"Bot's status loop stoped and status changed to  :- {text}")
            return
        
        self.bot.activies.append(text)

        with open("src\\resource\\extensions\\status.json", "r+") as activies:
            data = json.load(activies)
            data["Bot_Status"].append(text)
            activies.seek(0)
            json.dump(data, activies, indent=4)
            f.truncate()

        await self.bot.change_presence(status=self.bot.status, activity=discord.Game(name=text))
        await ctx.message.add_reaction("👍")
        await ctx.message.reply("Added a new status!")

        log.info(f"Added {text} in bot status loop")
        


        
    async def cog_command_error(self, ctx, error):
        """ Simply just send the error """
        await ctx.reply(error)
    

def setup(bot: commands.Bot):
    bot.add_cog(Bot_Controls(bot))