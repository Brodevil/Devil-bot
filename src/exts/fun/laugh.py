from logging import getLogger

import discord
from discord.ext.commands import Context, Cog, command
from discord.ext import commands

from random import choice
import pyjokes
from bs4 import BeautifulSoup

from src.bot import Bot
from src.constants import Colours
from src.exts.utils.exceptions import UnableToReach


log = getLogger(__name__)
URL = r"https://readme-jokes.vercel.app/api?bgColor=%23696969&text"

laughing = [
    "😆",
    "😂",
    "😹",
    "🤣"
]


class Laugh(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.cooldown(rate=1, per=9.0)
    @command(name="joke", aliases=("text_joke", "small_joke", ))
    async def shortJokes(self, ctx: Context):
        """Text Short Jokes"""
        async with ctx.typing():
            joke = pyjokes.get_joke()
            title = "Joke!\n"
            embed = discord.Embed(color=Colours.soft_red)
            embed.add_field(name=title, value=joke)

            msg = await ctx.send(embed=embed)
            await msg.add_reaction(choice(laughing))

def setup(bot: Bot) -> None:
    bot.add_cog(Laugh(bot))
