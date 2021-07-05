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
    async def clear(self, ctx: commands.Context, *,number):
        """Deleting messages"""
        number = int(number)

        def is_me(m):
            return m.author == self.bot.user
        
        deleted = await ctx.channel.purge(limit=number, check=is_me)
        await ctx.send('Deleted {} message(s)'.format(len(deleted)))



def setup(bot: commands.Bot):
    bot.add_cog(Messaging(bot))