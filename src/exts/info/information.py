import imp
import logging
from typing import Optional

from discord.ext import commands
from discord.ext.commands import bot, Context, Cog
import discord
from discord import Embed

from src.constants import Colours, Emojis
from src.utils.time import time_since

log = logging.getLogger(__name__)


class Information(Cog):
    """A cog with commands for generating embeds with server info, such as server stats, user info and role info"""

    def __init__(self, bot: bot):
        self.bot = bot

    @commands.guild_only()
    @commands.command(name="server", aliases=("server_info", "guild"))
    async def server_info(self, ctx: Context):
        """ Server information """

        # server info
        server = ctx.guild
        description = server.description
        created = time_since(server.created_at, max_units=3)
        server_roles = len(ctx.guild.roles) - 1  # leaving @everyone

        server_info = [f"📆 **Created** : {created}", f"🆔 **ID** : {server.id}", f"<:voice_channel:868863984269414430> **Voice Region** : {server.region}",
                       f"🔐 **Roles** : {server_roles}", f"**{Emojis.nitro_boost} Server Boosts :  {server.premium_subscription_count}**"]

        if description is not None:
            server_info.insert(0, f"**Description** : {description}\n")

        # member info
        total_members = server.member_count
        online = sum(
            member.status != discord.Status.offline and not member.bot for member in server.members)
        bots = sum(member.bot is True for member in server.members)
        offline = server.member_count - (online + bots)

        member_info = [f"{Emojis.status_online} **Online** : {online}",
                       f"{Emojis.status_offline} **Offline** : {offline} ", f"{Emojis.bots} **Bots** : {bots}"]

        # Channel
        total_channels = len(server.channels)

        channels_info = [f"**Stage Channels** : {len(server.stage_channels)}", f"**Text Channels** : {len(server.text_channels)}",
                         f"**Voice Channels** : {len(server.voice_channels)}", f"**Categories** : {len(server.categories)}"]

        # embed
        embed = Embed(title=server.name, color=Colours.soft_red,
                      description='\n'.join(server_info), icon=server.icon_url)
        embed.set_thumbnail(url=server.icon_url)
        embed.add_field(
            name=f'<:channel:868863984185528450> Channels : {total_channels}', value="\n".join(channels_info))
        embed.add_field(
            name=f"👥 Members : {total_members}", value="\n".join(member_info))
        embed.set_footer(text=f"Requested by {ctx.message.author}",
                         icon_url=ctx.message.author.avatar_url_as(format="png"))

        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command(name="user", aliases=("u", "member"))
    async def user(self, ctx: Context, user: discord.Member = None):
        """ user informations """
        if user is None:
            user = ctx.author

        name = str(user)
        roles = ", ".join(role.mention for role in user.roles[1:])

        created = time_since(user.created_at, max_units=3)
        joined = time_since(user.joined_at, max_units=3)

        user_info = [
            f"📆 **Created** : {created}", f"🆔 **ID** : {user.id}", f"👤 **Profile** : <@{user.id}>"]
        member_info = [
            f"**<:member_joined:861573073873141781> Joined** : {joined}", f"**👷 Roles** : {roles}"]

        if user.nick:
            name = f"{user.nick} ({name})"
            member_info.insert(1, f"**📛 Nick Name** : {user.nick}")

        embed = Embed(title=name, color=Colours.soft_red, inline=False)
        embed.add_field(name="User Information \n",
                        value="\n".join(user_info), inline=False)
        embed.add_field(name="Member Information",
                        value="\n".join(member_info), inline=False)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.message.author}",
                         icon_url=ctx.message.author.avatar_url_as(format="png"))

        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command(name="role", aliases=("r", "role_info"))
    async def role_info(self, ctx: Context, role: Optional[discord.Role] = None):
        """Server Roles info!"""
        if role is None or role not in ctx.guild.roles:
            await self.total_roles(ctx=ctx)
            return

        role_name = f"{role.name} {'(Not-Mentionable)' if not role.mentionable else ''}"
        created = time_since(role.created_at, max_units=3)
        members = len(role.members)
        position = len(ctx.guild.roles) - role.position

        embed = Embed(title=f"{role.name} Info",
                      color=Colours.soft_red)

        embed.add_field(name="ID 🆔", value=role.id, inline=True)
        embed.add_field(name="Created 📆", value=created, inline=True)
        embed.add_field(name="Members Count 👥", value=members, inline=True)
        embed.add_field(name="Position 👷", value=position, inline=True)
        embed.add_field(name="Color (RGB) 🌈",
                        value=f"#{role.colour.value:0>6x}", inline=True)
        embed.add_field(name="Permissions Code 💪", value=(
            role.permissions.value), inline=True)
        embed.set_footer(
            text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command(name="roles", aliases=("total_roles", "all_roles", ))
    async def total_roles(self, ctx: Context):
        all_roles = str()
        for _, role in enumerate(ctx.guild.roles[::-1]):
            if role.name != "@everyone":
                all_roles += (f"{_+1}. {role.name}\n")

        embed = Embed(title=f"{ctx.guild.name} Roles!",
                      description=f"```{all_roles}```",
                      color=Colours.soft_red)

        embed.set_footer(
            text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    """Load the Logging cog."""
    bot.add_cog(Information(bot))
