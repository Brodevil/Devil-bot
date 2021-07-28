from typing import Optional, Literal

import logging
import json 

from discord.ext.commands import Bot
from discord.ext.commands import Cog
from discord.ext import commands

from discord import Embed
import asyncio

from src.constants import Colours


logger = logging.getLogger(__name__)
__all__ = ("Reload_cogs", "setup")


class Reload_cogs(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    
    @commands.is_owner()
    @commands.command(name="reload", aliases=("reload_cog", "recog", "cog", "load"))
    async def reload_cogs(self, ctx: commands.Context, cog: Optional[str] = None):
        """Reloads the cogs """
        
        await ctx.confirm_action()
    
        with open("src/resource/extensions/_cogs.json") as cogs:
            cogs = json.load(cogs)
            cogs = list(cogs["cogs"])
                
        if cog is None:
            self.bot.loading_extensions(extensions=cogs, reload=True)
            await ctx.reply("**Reloaded All the Cogs!**")
            print("Reloaded All the Cogs!")

        elif cog in cogs:
            self.bot.loading_extensions(reload=True, single_cog=cog)
            await ctx.reply(f"**Sucessfully Reloaded `{cog}` Cog!**")
            print(f"Sucessfully Reloaded `{cog}` Cog!")
        
        else:
            for _ in cogs:
                if cog in _:
                    self.bot.loading_extensions(reload=True, single_cog=cog)
                    await ctx.reply(f"**Sucessfully Reloaded `{cog}` Cog!**")
                    print(f"Sucessfully Reloaded `{cog}` Cog!")
                    break
    
            else:
                await self.cogs(ctx=ctx)
    

    @commands.is_owner()
    @commands.command(name="cogs", aliases=("total_cogs", "show_cogs",))
    async def cogs(self, ctx: commands.Context):
        """Show case the Total Cogs"""
        with open("src/resource/extensions/_cogs.json") as cogs:
            cogs = json.load(cogs)
            cogs = list(cogs["cogs"])
        
        description = "\n".join(cogs)
        embed = Embed(title="Total Available Cogs :", 
                description=f"```{description}```",
                color=Colours.soft_red)
        
        await ctx.send(embed=embed)


def setup(bot: Bot):
    bot.add_cog(Reload_cogs(bot))

