from logging import getLogger
from turtle import color
from googlesearch import search

import discord
from discord.ext.commands import Context, Bot, Cog, command
from discord.ext import commands

from src.constants import Colours


log = getLogger(__name__)


class Search(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = Bot
    
    @commands.guild_only()
    @command(name="google", aliases=("search", "google_search", "find", ))
    async def google_search(self, ctx: Context, *, queary: str):
        """Instent Google search Results"""
        async with ctx.typing():
            results = [_ for _ in search(queary, tld="com", lang="en", num=7, stop=7, pause=1)]
            description = ""

            for index, result in enumerate(results):
                description += f"{index}. [{results}]({results})"
                description += "\n"

            embed = discord.Embed(title=queary, 
                                description=description, 
                                color=Colours.soft_red)
            
            await ctx.send(embed=embed)
      


def setup(bot: Bot) -> None:
    bot.add_cog(Search(bot))