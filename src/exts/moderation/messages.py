import logging
from turtle import color

from discord.ext import commands
import discord
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Embed

import asyncio

from src.constants import Colours


log = logging.getLogger(__name__)


class Messaging(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="clear", aliases=("del", "delete", ))
    @commands.guild_only()
    @has_permissions(manage_messages=True, read_message_history=True)
    async def clear(self, ctx: commands.Context, num):
        """Deleting messages"""
        await ctx.confirm_action()
        
        num = int(num)
        deleted = await ctx.channel.purge(limit=num)

        await ctx.send('🗑️ Deleted {} message(s)'.format(len(deleted)), delete_after=5)


    @commands.command(name="msg", aliases=("msg_channel", "send_msg"))
    @has_permissions(administrator=True)
    @commands.guild_only()
    async def server_msg(self, ctx: commands.Context, channel: discord.TextChannel, *, msg: str):
        """Messaging in Server channel using  bot"""
        if channel.guild != ctx.guild:
            ctx.reply("Command to Message in the same Server's Channels!")
            return
        await ctx.confirm_action()

        embed = Embed(description=msg, color=Colours.soft_red)
        await channel.send(embed=embed)
        await ctx.message.add_reaction("👍")


def setup(bot: commands.Bot):
    bot.add_cog(Messaging(bot))
