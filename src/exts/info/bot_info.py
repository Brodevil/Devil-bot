from curses.ascii import EM
import logging
import time
from datetime import timedelta

import discord
from discord import Embed
from discord.ext.commands import Bot, Cog, Context, command

from src.constants import Colours, Emojis


start_time = time.time()
logging.getLogger(__name__)


class Bot_info(Cog):
    """Few Commands for Bot informations"""

    def __init__(self, bot: Bot):
        self.bot = bot
    

    @command(name="ping")
    async def ping(self, ctx: Context):
        """Ping of Bot in miliseconds"""
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        embed = Embed(title="Pong!", color=Colours.soft_red)
        
        embed.add_field(name=f"Gateway Latency : ", value=f"{round(self.bot.latency * 1000)} ms", inline=False)
        embed.add_field(name=f"Discord API latency :", value=f"{str(end_time - start_time)[2:5]} ms", inline=False)
        embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url_as(format="png"))
        
        await message.edit(content="", embed=embed)
        await ctx.message.add_reaction("🏓")


    @command(name="uptime")
    async def uptime(self, ctx: Context):
        bot_uptime = int(time.time() - start_time)
        bot_uptime = timedelta(seconds=bot_uptime)
        embed = Embed(title=f"{Emojis.status_online} Bot UpTime!", color=Colours.soft_red
                    description=f"I Started up {bot_uptime} ago!")
        await ctx.send(embed=embed)


def setup(bot: Bot):
    bot.add_cog(Bot_info(bot))
