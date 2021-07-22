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

        await ctx.message.add_reaction("✅")
        await ctx.message.add_reaction("❌")
        
        def check(reaction, user):
            if user == ctx.message.author:
                if str(reaction.emoji) == '✅' or str(reaction.emoji) == "❌":
                    return True
        
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            embed = Embed(title="🚫 Action Cancled!", color=Colours.soft_red)
            await ctx.send(embed=embed)
            return 

        if str(reaction) == "❌":
            embed = Embed(title="🚫 Action Cancled!", color=Colours.soft_red)
            await ctx.send(embed=embed)
            return 


        with open("src\\resource\\extensions\\_cogs.json") as cogs:
            cogs = json.load(cogs)
            cogs = list(cogs["cogs"])
                
        if cog is None:
            self.bot.loading_extensions(extensions=cogs, reload=True)
            await ctx.reply("**Reloaded All the Cogs!**")

        elif cog in cogs:
            self.bot.loading_extensions(reload=True, single_cog=cog)
            await ctx.reply(f"**Sucessfully Reloaded `{cog}`` Cog!**")
        
        else:
            embed = Embed(title="Didn't Got such type of Cog \nAvailable Cogs are :",
            description="\n".join(cogs), color=Colours.soft_red)
            await ctx.send(embed=embed)
        
            

def setup(bot: Bot):
    bot.add_cog(Reload_cogs(bot))

