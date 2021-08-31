from logging import getLogger

from discord.ext.commands import Bot, Context, command, Cog
from discord import Embed


log = getLogger(__name__)


class VolientAction(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
    


def setup(bot: Bot) -> None:
    bot.add_cog(VolientAction(bot))