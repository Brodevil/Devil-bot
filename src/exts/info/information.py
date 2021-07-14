import logging

from discord.ext import commands
import discord
from discord import Embed

from src import constants                   # noqa
from src.utils.time import time_since       # noqa

log = logging.getLogger(__name__)



class Information(commands.Cog):
    """A cog with commands for generating embeds with server info, such as server stats, user info and role info"""

    def __init__(self, bot: commands.bot):
        self.bot = bot


    @commands.guild_only()
    @commands.command(name="server", aliases=("server_info", "guild"))
    async def server_info(self, ctx: commands.Context):
        """ Server information """

        # server info
        server = ctx.guild
        description = server.description
        created = time_since(server.created_at, max_units=3)
        server_roles = len(ctx.guild.roles) - 1  # leaving @everyone

        server_info = [f"📆 **Created** : {created}", f"🆔 **ID** : {server.id}", f"<:3581_voice_emoji:840975836781477938> **Voice Region** : {server.region}",
                        f"🔐 **Roles** : {server_roles}", f"**{constants.Emojis.nitro_boost} Server Boosts :  {server.premium_subscription_count}**"]

        if description is not None:
            server_info.insert(0, f"**Description** : {description}\n")
    

        # member info
        total_members = server.member_count
        online = sum(member.status != discord.Status.offline and not member.bot for member in server.members)
        bots = sum(member.bot is True for member in server.members)
        offline = server.member_count - (online + bots)

        member_info = [f"{constants.Emojis.status_online} **Online** : {online}", f"{constants.Emojis.status_offline} **Offline** : {offline} ", f"{constants.Emojis.bots} **Bots** : {bots}"]

        # Channel
        total_channels = len(server.channels)
        
        channels_info = [f"**Stage Channels** : {len(server.stage_channels)}", f"**Text Channels** : {len(server.text_channels)}", 
                            f"**Voice Channels** : {len(server.voice_channels)}", f"**Categories** : {len(server.categories)}"]

        # embed
        embed = Embed(title=server.name, color=discord.Color.blue(), description='\n'.join(server_info), icon=server.icon_url)
        embed.set_thumbnail(url=server.icon_url)
        embed.add_field(name=f'<:3410_Channel_fluffys:840975836832071710> Channels : {total_channels}', value="\n".join(channels_info))
        embed.add_field(name=f"👥 Members : {total_members}", value="\n".join(member_info))
        embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url_as(format="png"))
        await ctx.send(embed=embed)


    @commands.guild_only()
    @commands.command(name="user", aliases=("u", "member"))
    async def user(self, ctx: commands.Context, user: discord.Member = None):
        """ user informations """
        if user is None:
            user = ctx.author

        name = str(user)
        roles = ", ".join(role.mention for role in user.roles[1:])

        created = time_since(user.created_at, max_units=3)
        joined = time_since(user.joined_at, max_units=3)

        user_info = [f"📆 **Created** : {created}", f"🆔 **ID** : {user.id}", f"👤 **Profile** : <@{user.id}>"]
        member_info = [f"**<:member_joined:861573073873141781> Joined** : {joined}", f"**👷 Roles** : {roles}"]

        if user.nick:
            name = f"{user.nick} ({name})"
            member_info.insert(1, f"**📛 Nick Name** : {user.nick}")

        embed = Embed(title=name, color=constants.Colours.blue, inline=False)
        embed.add_field(name="User Information \n", value="\n".join(user_info), inline=False)
        embed.add_field(name="Member Information", value="\n".join(member_info), inline=False)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url_as(format="png"))
        
        await ctx.send(embed=embed)


    async def cog_command_error(self, ctx, error):
        """ Simply just send the error """
        await ctx.send(error)
    

def setup(bot: commands.Bot):
    """Load the Logging cog."""
    bot.add_cog(Information(bot))