import asyncio
from logging import getLogger

import discord
from discord.ext.commands import Context, Bot, Cog, command
from discord.ext import commands

from random import choice
import pyjokes

from src.constants import Colours
from src.resource.APIs.plant_text import get_quote
from src.resource.APIs.filter_request import short_google_search

log = getLogger(__name__)

laughing = [
    "😆",
    "😂",
    "😹",
    "🤣"
]

class Laugh(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
    
    @command(name="joke", aliases=("text_joke", "small_joke", ))
    async def shortJokes(self, ctx: Context):
        """Text Short Jokes"""
        async with ctx.typing():
            joke = pyjokes.get_joke()
            title = "Text Joke!\n"
            embed = discord.Embed(color=Colours.soft_red)
            embed.add_field(name=title, value=joke)
            
            msg = await ctx.send(embed=embed)
            await msg.add_reaction(choice(laughing))
    

    @command(name="jokeimg", aliases=("joke_img", "qjoke"))
    async def qna_joke(self, ctx: Context):
        async with ctx.typing():
            pass


    @command(name="inspire", aliases=("quotes", "thoughts", "quote", ))
    async def inspire(self, ctx: Context):
        async with ctx.typing():
            quote, author = await get_quote()
            embed = discord.Embed(title="Quotes!", color=Colours.soft_red)
            embed.add_field(name=quote, value=f"- {author}")
            await ctx.send(embed=embed)
    


def setup(bot: Bot) -> None:
    bot.add_cog(Laugh(bot))
