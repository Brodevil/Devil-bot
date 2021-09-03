from logging import getLogger
from typing import Optional

from discord.ext.commands import Bot, Context, command, Cog
from discord.ext import commands
from discord import Embed
import discord

from src.constants import Colours


log = getLogger(__name__)


class VolientAction(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
    
    @commands.guild_only()
    @commands.has_permissions(ban_members = True)
    @command(name="ban", aliases=("ban_user", "BAN", ))
    async def ban(self, ctx: Context, user: discord.Member, *, reason : Optional[str]):
        if reason is None:
            reason = "Mischief Behavior"
        
        await user.ban(reason=reason)
        await ctx.message.delete()
        await ctx.send(f'>>> **👌 ||<{user.id}>|| has been banned from {ctx.guild} Server!** \nReason : ||{reason}||')
        await user.send(f">>> **You had Banned from {ctx.guild} Server!**")
    

    @commands.guild_only()
    @commands.has_permissions(administrator = True)
    @command(name="unban", aliases=("unban_user", "remove_ban", "UNBAN"))
    async def unban(self, ctx: Context, user: discord.Member, *, reason: Optional[str]):
        if reason is None:
            reason = "Forgiven"
        
        await user.unban(reason=reason)
        await ctx.message.delete()
        await ctx.send(f">>> **👌 ||<{user.id}>|| had unbanned from {ctx.guild} Server!**")
        await user.send(f">>> **You had Unbanned from {ctx.guild} Server!** \n Reason : {reason}")


    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @command(name="kick", aliases=("kick_user", "KICK"))
    async def kick(self, ctx: Context, user: discord.Member):
        await self.bot.kick(user)
        await ctx.message.delete()
        await ctx.send(f">>> **👌 ||<{user.id}>|| had kciked form the Server!**")


def setup(bot: Bot) -> None:
    bot.add_cog(VolientAction(bot))