import logging
import time

from discord.ext import commands
import discord
from discord import Embed

from src import constants
from src.utils.time import time_since

log = logging.getLogger(__name__)



class Information(commands.Cog):
    """A cog with commands for generating embeds with server info, such as server stats, user info and role info"""

    def __init__(self, bot: commands.bot):
        self.bot = bot
    

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """ping of Bot"""
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        embed = Embed(
            title="Pong!",
            color=constants.Colours.blue)
        embed.add_field(name=f"Gateway Latency : ", value=f"{round(self.bot.latency * 1000)} ms", inline=False)
        embed.add_field(name=f"Discord API latency :", value=f"{str(end_time - start_time)[2:5]} ms", inline=False)

        await message.edit(content="", embed=embed)


    @commands.command(name="user", aliases=("u",))
    @commands.guild_only()
    async def user(self, ctx: commands.Context, user: discord.Member = None):
        """ user informations """
        if user is None:
            user = ctx.author

        name = str(user)
        if user.nick:
            name = f"{user.nick} ({name})"

        roles = ", ".join(role.mention for role in user.roles[1:])

        created = time_since(user.created_at, max_units=3)
        joined = time_since(user.joined_at, max_units=3)

        embed = Embed(title=name, color=constants.Colours.blue, inline=False)
        embed.add_field(name="User Information \n",
                        value=f"Created : {created}  \nProfile : <@{user.id}>  \nID : {user.id}",
                        inline=False)

        embed.add_field(name="Member Information",
                        value=f"Joined : {joined}  \nRoles : {roles}",
                        inline=False)

        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)


        @commands.command(name="server", aliases=("server_info", ))
        async def server_info(self, ctx: commands.Context):
            """ Server infomations """


            # server info
            server = ctx.guild
            description = server.description
            created = time_since(server.created_at, max_units=3)
            server_roles = len(ctx.guild.roles) - 1  # leaving @everyone

            server_info = [f"Created : {created}", f"ID : {server.id}", f"Voice Region : {server.region}",
                           f"Roles : {server_roles}", f"Server Boosts :  **{server.premium_subscription_count}** {constants.Emojis.nitro_boost}"]

            if description is not None:
                server_info.insert(0, f"Description : {description}\n")
        

            # member info
            total_members = server.member_count
            online = sum(member.status != discord.Status.offline and not member.bot for member in server.members)
            bots = sum(member.bot is True for member in server.members)
            offline = server.member_count - (online + bots)

            member_info = [f"{constants.Emojis.status_online}  {online}", f"{constants.Emojis.status_offline}  {offline} ", f"{constants.Emojis.bots}  {bots}"]


            # Channel
            total_channels = len(server.channels)
           
            channels_info = [f"Stage Channels : {len(server.stage_channels)}", f"Text Channels : {len(server.text_channels)}", 
                             f"Voice Channels : {len(server.voice_channels)}", f"Categories : {len(server.categories)}"]

            # embed
            embed = Embed(title=server.name, color=discord.Color.blue(), description='\n'.join(server_info))
            embed.set_thumbnail(url=server.icon_url)
            embed.add_field(name=f'Channels : {total_channels}', value="\n".join(channels_info))
            embed.add_field(name=f"Members : {total_members}", value="\n".join(member_info))

            await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    """Load the Logging cog."""
    bot.add_cog(Information(bot))