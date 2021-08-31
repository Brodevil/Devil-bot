from logging import getLogger

from discord.ext.commands import Bot, Context, command, Cog
from discord.ext import commands
from discord import Embed
import discord

from src.constants import Colours


log = getLogger(__name__)


class VolientAction(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
    
    @commands.has_permissions()
    @command(name="ban", aliases=("ban_user", ))
    async def ban(self, ctx: Context, user: discord.User, time: ):
        pass


def setup(bot: Bot) -> None:
    bot.add_cog(VolientAction(bot))