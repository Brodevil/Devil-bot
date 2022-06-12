from json import loads
from logging import getLogger

from discord.ext.commands import Cog, command, Context
from discord.ext import commands
import discord

from src.constants import Colours
from src.exts.utils.exceptions import UnableToReach
from src.bot import Bot

log = getLogger(__name__)


class Inspiration(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    async def get_quote(self) -> str:
        """Returns the quote and it's author as a string"""
        URL = "https://zenquotes.io/api/random"
        async with self.bot.http_session.get(URL) as quote:
            if quote.status != 200:
                error = f"Unexpected status code {quote.status} from genderize.io"
                log.error(error)
                raise UnableToReach(error)

            quote = await quote.text()
            quote = loads(quote)
            return quote[0]["q"], quote[0]["a"]

    @commands.cooldown(rate=1, per=9.0)
    @command(name="inspire", aliases=("quotes", "thoughts", "quote"))
    async def inspire(self, ctx: Context):
        async with ctx.typing():
            quote, author = await self.get_quote()
            embed = discord.Embed(title="Quotes!", color=Colours.soft_red)
            embed.add_field(name=quote, value=f"- {author}")
            await ctx.send(embed=embed)


def setup(bot: Bot) -> None:
    """Load's the Inspiration Cog"""
    bot.add_cog(Inspiration(bot))
