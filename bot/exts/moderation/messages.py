import logging

from discord.ext import commands
import discord

log = logging.getLogger(__name__)


class Messaging(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    

def setup(bot: commands.Bot):
    bot.add_cog(Messaging(bot))