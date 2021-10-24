import logging

import discord
from discord.ext.commands import Cog, command, cooldown, Context
from discord.ext import commands

from src.bot import bot
from src.constants import Colours


logger = logging.getLogger(__name__)
API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

ERROR = discord.Embed(
    title="Error while searching Word",
    description="Got an error while trying to find word's meaning from Dictionary",
    color=Colours.soft_red
)

STATUS_NOT_200 = discord.Embed(
    title="No Definitions Found",
    description="Unable to find definitions for the word you were looking for. \nYou can try the search again at later time or head to the web instead.",
    color=Colours.soft_red
)


class Define(Cog):
    """user initiated command to search the meaning of any new word"""

    def __init__(self, bot: bot) -> None:
        self.bot = bot

    @command(name="define", aliases=["meaning", "dictionary"])
    @cooldown(1, 7, commands.cooldowns.BucketType.user)
    async def define_word(self, ctx: Context, *, word: str) -> None:
        """Get the defination of any new word in English"""
        async with ctx.typing():
            async with self.bot.http_session.get(API_URL.format(word=word), ssl=False) as resp:
                if resp.status != 200:
                    logger.error(
                        f"Unexpected status code {resp.status} from dictionaryAPI.dev"
                    )
                    await ctx.send(embed=STATUS_NOT_200)
                    return

                data = await resp.json()
                data = data[0]
        
        if data.get("title") is not None:
            ctx.send(embed=ERROR)
            return
        
        defination = data["meanings"][0]["definitions"][0]["definition"]

        embed = discord.Embed(
            title="{0} Defination :".format(word.capitalize()),
            description=defination.capitalize(),
            color=Colours.soft_red
        )
        await ctx.send(embed=embed)


def setup(bot: bot) -> None:
    """Loads the dictionary Cog"""
    bot.add_cog(Define(bot))
