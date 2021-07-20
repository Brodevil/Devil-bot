from typing import Optional, Literal

import logging
import json 

from discord.ext.commands import Bot
from discord.ext.commands import Cog
from discord.ext import commands

from discord import Embed

from src.constants import Colours


logger = logging.getLogger(__name__)
__all__ = ("Reload_cog", "setup")


class Reload_cogs(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    
    @commands.is_owner()
    @commands.command(name="reload", aliases=("reload_cog", "recog", "cog"))
    async def cog_reloader(self, ctx: commands.Context, cog: Optional[str] = None):
        """Reloads the cogs """

        with open("src\\resource\\extensions\\status.json") as f:
            f = json.load(f)
            f = list(f["cogs"])
                
        if cog is None:
            self.bot.loading_extensions(extensions=f, reload=True)

        elif cog in f:
            self.bot.load_extension(reload=True, extension=cog)
        
        else:
            embed = Embed(color=Colours.soft_red)
            embed.add_field(name=""
            
        

def setup(bot: Bot):
    bot.add_cog(Reload_cogs(bot))

