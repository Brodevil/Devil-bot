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
    @commands.command(name="reload", aliases=("reload_cog", "recog", "cog", "load"))
    async def reload_cogs(self, ctx: commands.Context, cog: Optional[str] = None):
        """Reloads the cogs """

        with open("src\\resource\\extensions\\_cogs.json") as cogs:
            cogs = json.load(cogs)
            cogs = list(cogs["cogs"])
                
        if cog is None:
            self.bot.loading_extensions(extensions=cogs, reload=True)
            await ctx.message.add_reaction("👍")

        elif cog in cog:
            work = self.bot.load_extension(reload=True, extension=cog)
            if work:
                await ctx.message.add_reaction("👍")
            else:
                await ctx.message.add_reaction("👎")
        
        else:
            embed = Embed(title="Didn't Got such type of Cog \nAvailable Cogs are :",
            description="\n".join(cogs))

            await ctx.send(embed=embed)
        
            

def setup(bot: Bot):
    bot.add_cog(Reload_cogs(bot))

