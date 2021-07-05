import logging

from discord.ext import commands
import discord
from discord.ext.commands import has_permissions, MissingPermissions

import asyncio

from src import constants   # noqa
from src.constants import Channels              # noqa

log = logging.getLogger(__name__)


class Messaging(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command(name="clear", aliases=("del", "delete", ))
    @commands.guild_only()
    @has_permissions(manage_messages=True, read_message_history=True)
    async def clear(self, ctx: commands.Context, num):
        """Deleting messages"""
        num = int(num)
        deleted = await ctx.channel.purge(limit=num)

        msg = await ctx.send('Deleted {} message(s)'.format(len(deleted)))
        await asyncio.sleep(4.0)

        await msg.delete()



def setup(bot: commands.Bot):
    bot.add_cog(Messaging(bot))