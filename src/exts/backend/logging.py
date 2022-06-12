import logging
from pickle import NONE

from discord.ext import commands
from discord import Embed

from src.constants import Channels
from src.constants import Colours


log = logging.getLogger(__name__)


class Logging(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.bot.loop.create_task(self.startup_log())
        self.bot.loop.create_task(self.join_voice_channel())

    async def startup_log(self) -> None:
        await self.bot.wait_until_ready()
        log.info("Bot connected!")

        embed = Embed(description="Connected!", color=Colours.soft_red)
        embed.set_author(
            name=self.bot.user.name,
            icon_url=self.bot.user.avatar_url
        )

        log_channel = self.bot.get_channel(Channels.LOG_CHANNEL)
        await log_channel.send(embed=embed)

    async def join_voice_channel(self) -> None:
        await self.bot.wait_until_ready()

        voice_channel = self.bot.get_channel(Channels.VOICE_CHAT_CHANNEL)
        await voice_channel.connect()


def setup(bot: commands.Bot) -> None:
    bot.add_cog(Logging(bot))
