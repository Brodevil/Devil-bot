import logging

from discord.ext import commands
import discord

from src.constants import Colours


log = logging.getLogger(__name__)


class Commands(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="hello", aliases=("hey", "hlo", "test"))
    async def hello_world(self, ctx: commands.Context):
        await ctx.message.add_reaction("👋")
        embed = discord.Embed(color=Colours.soft_red)
        embed.set_image(url="https://media.tenor.com/images/7e6a7b73faa414e321811e0ecb34519e/tenor.gif")
        await ctx.send(embed=embed)




def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot))

