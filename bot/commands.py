import logging
import sys
import time

import discord
from discord.ext import commands
from discord import Embed

from bot import constants
from bot import functions


log = logging.getLogger(__name__)


class Commands(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command(name="hello", aliases=("hey", "hlo",))
    async def hello_world(self, ctx: commands.Context):
        await ctx.message.add_reaction("👋")


    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        embed = Embed(
            title="Pong!",
            color=constants.Colours.blue)
        embed.add_field(name=f"Gateway Latency : ", value=f"{round(self.bot.latency * 1000)} ms", inline=False)
        embed.add_field(name=f"Discord API latency :", value=f"{str(end_time - start_time)[2:5]} ms", inline=False)

        await message.edit(content="", embed=embed)


    @commands.command(name="quit", aliases=("close", "bye", "logout", ))
    async def quit(self, ctx: commands.Context):
        is_owner = await ctx.bot.is_owner(ctx.author)
        if is_owner:
            await ctx.message.add_reaction("👋")
            await self.bot.close()
            log.exception(f"{self.bot.user} had logged out by the bot author")
            sys.exit(0)


    @commands.command(name="dm")
    async def send_dm(self, ctx, member: discord.Member, *, content):
        channel = await member.create_dm()
        
        icon = ctx.message.author.avatar_url_as(format="png")
        embed = Embed(description=content, color=constants.Colours.orange)
        embed.set_author(name=ctx.message.author, icon_url=icon,  url=(f"https://discordapp.com/users/{ctx.message.author.id}"))
        
        await channel.send(embed=embed)


    @commands.command(name="setstatus", aliases=("status", "ss",))
    async def setstatus(self, ctx: commands.Context, *, text: str):
        is_owner = await ctx.bot.is_owner(ctx.author)
        if is_owner:
            await self.bot.change_presence(activity=discord.Game(name=text))


    @commands.command(pass_context=True, name="nick", aliases=("chnick", "nickname"))
    async def chnick(self, ctx, member: discord.Member, *, nick):
        await member.edit(nick=nick)


    @commands.command(name="user", aliases=("u", ))
    async def user(self, ctx: commands.Context, user: discord.Member = None):
        if user is None:
            user = ctx.message.author

        name = str(user)
        if user.nick:
            name = f"{user.nick} ({name})"
        
        roles = ", ".join(role.mention for role in user.roles[1:])
    
        created = functions.time_since(user.created_at, max_units=3)
        joined = functions.time_since(user.joined_at, max_units=3)
        
        embed = Embed(title =name, color=constants.Colours.blue, inline=False)
        embed.add_field(name="User Information \n", 
        value=f"Created : {created}  \nProfile : <@{user.id}>  \nID : {user.id}", 
        inline=False)

        embed.add_field(name="Member Information", 
        value=f"Joined : {joined}  \nRoles : {roles}", 
        inline=False)
        
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)
        
    

    @commands.command(name="server")
    async def server_info(self, ctx: commands.Context):
        server = ctx.guild

        created = functions.time_since(server.created_at, max_units=3)
        

        # member info
        online = sum(member.status!=discord.Status.offline and not member.bot for member in server.members)
        print(discord.Status.offline)
        print(discord.Status.online)

        description = server.description
        server_roles = len(ctx.guild.roles) - 1     # leaving @everyone

        server_info = [f"Created : {created}", f"ID : {server.id}", f"Voice Region : {server.region}", f"Roles : {server_roles}", 
                        f"Members Status : <:online_status:859727593872031794> {online} |  <:offline_status:859727545157943316> {offline}"]

        if description is not None:
            server_info.insert(0, f"Description : {description}\n")

        embed = Embed(title=server.name, color=discord.Color.blue(), description='\n'.join(server_info))
        embed.set_thumbnail(url=server.icon_url)

       
       # Channesl
        total_channels = len(ctx.guild.channels)
        channel_counts = self.get_channel_type_counts(server)
        channel_info = "\n".join(
            f"{channel.title()}: {count}" for channel, count in sorted(channel_counts.items())
        )
        embed.add_field(name=f"Channels: {total_channels}", value=channel_info)
        

        await ctx.send(embed=embed)


    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            embed = Embed(title="{}'s info".format(member.name), description="Welcome too {}".format(member.guild.name), color=constants.Colours.blue)
            embed.add_field(name="Name", value=member.name, inline=True)
            embed.add_field(name="ID", value=member.id, inline=True)
            embed.add_field(name="Status", value=member.status, inline=True)
            embed.add_field(name="Roles", value=member.top_role)
            embed.add_field(name="Joined", value=member.joined_at)
            embed.add_field(name="Created", value=member.created_at)
            embed.set_thumbnail(url=member.avatar_url)
            new_member = self.bot.get_user(member.id)
            channel = member.guild.system_channel
            if channel is not None:
                await channel.send(embed=embed)
            await new_member.send(embed=embed)
        
    

    @commands.command(name="mute", pass_context = True)
    async def mute(self, ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == constants.Client.OWNER_ID:
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await ctx.say(embed=embed)



def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot))
