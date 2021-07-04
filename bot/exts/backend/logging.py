import logging

from discord.ext.commands import Bot
from discord import Embed
from discord.ext.commands import Cog


from bot.constants import Channels


log = logging.getLogger(__name__)


class Logging(Cog):
    """Debug logging module."""

    def __init__(self, bot: Bot):
        self.bot = bot
        self.bot.loop.create_task(self.startup_log())


    async def startup_log(self) -> None:
        log.info("Bot connected!")

        embed = Embed(description="Connected!")
        embed.set_author(
            name=self.bot.user.name,
            url="https://github.com/Brodevil/Devil-bot",
            icon_url=self.bot.user.avatar_url
        )

        await self.bot.get_channel(Channels.LOG_CHANNEL).send(embed=embed)


def setup(bot: Bot) -> None:
    """Load the Logging cog."""
    bot.add_cog(Logging(bot))