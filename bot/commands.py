import logging
import sys
import time

import discord
from discord.ext import commands
from discord import Embed

from bot import constants

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
        embed.set_author(name=f"{ctx.message.author.name}", icon_url=icon,  url=(f"https://discordapp.com/users/{ctx.message.author.id}"))
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
        
        embed = Embed(title = user.name, color=constants.Colours.blue, url=(f"https://discordapp.com/users/{ctx.message.author.id}"))
        embed.add_field(name="User Information", value="")
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Roles", value=user.top_role)
        embed.add_field(name="Joined", value=user.joined_at)
        embed.add_field(name="Created", value=user.created_at)
        embed.set_thumbnail(url=user.avatar_url)

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



def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot))
