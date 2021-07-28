import logging

from discord.ext.commands import Cog
from discord.ext.commands import Bot
import discord

log = logging.getLogger(__name__)


class Welcome(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot




def setup(bot: Bot):
    bot.add_cog(Welcome(bot))
