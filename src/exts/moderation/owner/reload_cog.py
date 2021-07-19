from typing import Optional, Literal

import logging

from discord.ext.commands import Bot
from discord.ext.commands import Cog
from discord.ext import commands

__all__ = ("Reload_cog", "setup")

class Reload_cogs(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    
    @commands.is_owner()
    @commands.command(name="reload", aliases=("reload_cog", "recog", "cog"))
    async def cog_reloader(self, ctx: commands.Context, ):
        pass


def setup(bot: Bot):
    bot.add_cog(Reload_cogs(bot))

