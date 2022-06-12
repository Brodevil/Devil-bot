from logging import getLogger
from typing import Optional
from datetime import datetime, timedelta

import discord
from discord.ext.commands import Bot, Context, command, Cog
from discord.ext import commands


log = getLogger(__name__)

ADD_BAN = """
INSERT INTO `bans`
VALUES (DEFAULT, {0}, {1}, "{2}")
"""
RM_BAN = """
DELETE FROM `bans`
WHERE `user_id` = {0} AND `guild_id` = {1}
"""


class VolientAction(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @staticmethod
    def ban_duration(duration: str) -> datetime:
        """Converting duration to unix timestamp"""
        duration = duration.split("-")
        ban_till = {}
        for _ in duration:
            if "m" in _:
                ban_till["minutes"] = int(_.replace("m", ""))
            elif "h" in _:
                ban_till["hours"] = int(_.replace("h", ""))
            elif "d" in _:
                ban_till["days"] = int(_.replace("d", ""))
            elif "w" in _:
                ban_till["weeks"] = int(_.replace("w", ""))
            elif "y" in _:
                ban_till["years"] = int(_.replace("y", ""))

        duration = datetime.now() + timedelta(**ban_till)
        return duration

    async def banned_user(
        self, user: int, server: int,
        unban_on: Optional[int], to_ban: bool = True
    ) -> None:
        """Updating database's bans Table"""
        if to_ban:
            queary = ADD_BAN.format(user, server, unban_on)
            self.bot.database.run(queary, commit=True)

        else:
            queary = RM_BAN.format(user, server)
            self.bot.database.run(queary, commit=True)

    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @command(name="ban", aliases=("ban_user", "BAN", "tempban"))
    async def ban(
        self, ctx: Context,
        user: discord.Member,
        duration: Optional[str] = None,
        *, reason: Optional[str] = None
    ):
        """Ban a user from the server
        param: user: The user to ban
        param: duration: The duration of the ban in the format of like '1d-2h-3m'
        param: reason: The reason for the ban
        """
        await ctx.confirm_action()

        if user.id == ctx.author.id:
            await ctx.send("You can't ban yourself")
            return
        if user.top_role.position >= ctx.author.top_role.position:
            await ctx.send("You can't ban this user")
            return
        if user.id == self.bot.user.id:
            await ctx.send("I can't ban myself")
            return
        if user.id == self.bot.owner_id:
            await ctx.send("I can't ban my owner")
            return

        if duration is not None:
            duration = self.ban_duration(duration)
            msg = f'**👌 ||<@{user.id}>|| has been temprarily banned till <t:{int(round(duration.timestamp()))}:t>, from {ctx.guild} Server!**'
            user_msg = f"You have been banned from {ctx.guild} Server till <t:{int(round(duration.timestamp()))}:t>"
            duration = duration.strftime("%Y-%m-%d %H:%M:%S")
            await self.banned_user(user.id, ctx.guild.id, duration, to_ban=True)

        else:
            msg = f'**👌 ||<@{user.id}>|| has been permanently banned from Server!**'
            user_msg = f"You have permanently banned from {ctx.guild} Server"

        await user.ban(reason=reason)
        if not user.bot:
            await user.send(user_msg)

        await ctx.send(msg)
        await ctx.message.delete()

    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @command(name="unban", aliases=("unban_user", "remove_ban", "UNBAN"))
    async def unban(self, ctx: Context, user: discord.User):
        """Unban a user from the server"""
        await ctx.confirm_action()

        await self.banned_user(user.id, ctx.guild.id, None, to_ban=False)
        user = await self.bot.fetch_user(user.id)
        await ctx.guild.unban(user)
        if not user.bot:
            await user.send(f"**You has Unbanned from {ctx.guild} Server!**")

        await ctx.send(f"**👌 ||<@{user.id}>|| has Unbanned from {ctx.guild} Server!**")

    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @command(name="kick", aliases=("kick_user", "KICK"))
    async def kick(self, ctx: Context, user: discord.Member, *, reason: Optional[str] = "No reason"):
        """Kick a user from the server"""
        await ctx.confirm_action()

        await ctx.guild.kick(user)
        await ctx.message.delete()
        await ctx.send(f"**👌 ||<@{user.id}>|| had kicked form the Server!**", delete_after=60)


def setup(bot: Bot) -> None:
    """Add cog Volient Action to bot"""
    bot.add_cog(VolientAction(bot))
