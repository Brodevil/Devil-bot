from logging import getLogger
from random import choice

import discord
from discord.ext import commands
from discord.ext.commands import  Context, command, Cog


from src.constants import Colours
from src.bot import Bot
from src.exts.utils.exceptions import UnableToReach


log = getLogger(__name__)

laughing = [
    "😆",
    "😂",
    "😹",
    "🤣"
]


class Memes(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.cooldown(rate=1, per=10)
    @command(name="memes", aliases=("meme", "meme_joke", "img_memes", ))
    async def memes(self, ctx: Context):
        """Memes"""
        async with ctx.typing():
            url = "https://meme-api.herokuapp.com/gimme"
            async with self.bot.http_session.get(url) as resp:
                if resp.status != 200:
                    error = f"Unexpected status code {resp.status} from genderize.io"
                    log.error(error)
                    raise UnableToReach(error)

                data = await resp.json()
                embed = discord.Embed(color=Colours.soft_red)
                embed.set_image(url=data["url"])
                embed.set_footer(text=f"{data['title']}")

                msg = await ctx.send(embed=embed)
                await msg.add_reaction(choice(laughing))


def setup(bot: Bot) -> None:
    """Add memes cog"""
    bot.add_cog(Memes(bot))
