import asyncio
from logging import getLogger

import discord
from discord.ext.commands import Context, Bot, Cog, command
from discord.ext import commands

from random import choice
import pyjokes

from src.constants import Colours


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
        async with ctx.typing():
            joke = pyjokes.get_joke()
            msg = await ctx.reply(f"**{joke}**")
            await msg.add_reaction(choice(laughing))


    @command(name="inspire", aliases=("quotes", "thoughts"))
    async def inspire(self, ctx: Context):
        pass


def setup(bot: Bot) -> None:
    bot.add_cog(Laugh(bot))
