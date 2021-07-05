import logging

from discord.ext import commands
from discord import Embed

from src.constants import Channels


log = logging.getLogger(__name__)


class Logging(commands.Cog):
    """Debug logging module."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        

    @self.bot.event()
    async def startup_log(self):
        log.info("Bot connected!")

        embed = Embed(description="Connected!")
        embed.set_author(
            name=self.bot.user.name,
            icon_url=self.bot.user.avatar_url
        )

        log_channel = self.bot.get_channel(Channels.LOG_CHANNEL)
        await log_channel.send(embed=embed)


def setup(bot: commands.Bot):
    """Load the Logging cog."""
    bot.add_cog(Logging(bot))