import logging
import time

import discord
from discord.ext.commands import Bot 
from discord.ext import commands 
from discord import Embed

from src import constants                   


logging.getLogger(__name__)


class Bot_info(commands.Cog):
    """Few Commands for Bot informations"""

    def __init__(self, bot: Bot):
        self.bot = bot
    

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Ping of Bot in miliseconds"""
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        embed = Embed(title="Pong!", color=constants.Colours.soft_red)
        
        embed.add_field(name=f"Gateway Latency : ", value=f"{round(self.bot.latency * 1000)} ms", inline=False)
        embed.add_field(name=f"Discord API latency :", value=f"{str(end_time - start_time)[2:5]} ms", inline=False)
        embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url_as(format="png"))
        
        await message.edit(content="", embed=embed)
        await ctx.message.add_reaction("🏓")


    

def setup(bot: Bot):
    bot.add_cog(Bot_info(bot))