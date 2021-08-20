from logging import getLogger
from webbrowser import get

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
    async def google_search(self, ct: Context, *, search: str):
        """Instent Google search Results"""
        pass


def setup(bot: Bot) -> None:
    bot.add_cog(Search(bot))