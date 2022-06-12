import logging
import sys
from os import system

from discord.ext import commands
from discord import Embed
from discord import Status
import discord

from typing import Optional
import json

from src.constants import Colours
from src.exts.utils.converter import BoolConverter


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
        await ctx.confirm_action()
        await self.bot.change_presence(status=discord.Status.invisible)

        embed = Embed(title="🏃 Logged Out!", color=Colours.soft_red)
        await ctx.send(embed=embed)

        log.exception(f"{self.bot.user} had logged out by the bot author")
        await self.bot.logout()
        self.bot.database.pointer.close()
        self.bot.database.database.close()
        sys.exit(0)

    @commands.is_owner()
    @commands.command(name="dm")
    async def send_dm(self, ctx: commands.Context,
                      User: discord.Member,
                      show_name: Optional[bool] = True,
                      *, content):

        """ Direct Messaging the user """
        await ctx.confirm_action()
        await ctx.message.delete()

        channel = await User.create_dm()

        if show_name:
            name = ctx.message.author.name
            url = f"https://discordapp.com/users/{ctx.message.author.id}"
            icon = ctx.message.author.avatar_url_as(format="png")

        elif not show_name:
            name = self.bot.user.name
            url = f"https://discordapp.com/users/{self.bot.user.id}"
            icon = self.bot.user.avatar_url_as(format="png")

        embed = Embed(description=content, color=Colours.soft_red)
        embed.set_author(name=name, icon_url=icon, url=url)

        await channel.send(embed=embed)
        await ctx.reply("👌")
    
    @commands.is_owner()
    @commands.command(name="rerun", aliases=["rerun_bot", "restart", "runagain"])
    async def test(self, ctx: commands.Context):
        await ctx.confirm_action()
        msg = "Mr. Devil Bot is going to restart the Program"
        await ctx.send(msg, delete_after=10)
        system("python run.py")
        log.exception(msg)

        await self.bot.change_presence(status=discord.Status.invisible)
        await self.bot.logout()
        self.bot.database.pointer.close()
        self.bot.database.database.close()
        sys.exit(0)


    @commands.is_owner()
    @commands.command(name="status", aliases=("set_status", "activity"))
    async def setstatus(self, ctx: commands.Context,
                        status: Optional[Status] = Status.online,
                        run_loop: Optional[bool] = True, *,
                        text: Optional[str] = None):

        """Adding the more status and run it"""
        await ctx.confirm_action()

        # status
        self.bot.status = status

        # loop
        if run_loop == False and self.bot.change_status.is_running() == True:
            self.bot.change_status.cancel()
            log.info(
                f"Bot's status loop stoped and status changed to  :- {text}")
            await ctx.reply("Stoped the Activity Loop")

        if run_loop == True and self.bot.change_status.is_running() == False:
            self.bot.change_status.start()
            await ctx.reply("Started the Activity Loop")

        if text is not None and run_loop != False:
            self.bot.activies.insert(0, text)
            with open("src\\resource\\extensions\\status.json", "r+") as activies:
                data = json.load(activies)
                data["Bot_Status"].insert(0, text)
                activies.seek(0)
                json.dump(data, activies, indent=4)
                activies.truncate()

            await ctx.reply("Added a new status!")

        if text is None:
            text = f"Over {len(self.bot.guilds)} Servers, Over {len(set(self.bot.users))} Members"

        await self.bot.change_presence(status=self.bot.status, activity=discord.Game(name=text))
        await ctx.message.add_reaction("👍")

        log.info(f"Added {text} in bot status loop")


def setup(bot: commands.Bot):
    bot.add_cog(Bot_Controls(bot))
