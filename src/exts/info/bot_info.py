import logging
from time import time
from datetime import timedelta
from platform import python_version, system

from discord import Embed, __version__
from discord.ext.commands import Bot, Cog, Context, command

from src.constants import Colours, Emojis, Client
from src.utils.time import define_time


logging.getLogger(__name__)


class Bot_info(Cog):
    """Few Commands for Bot informations"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @staticmethod
    def add_acture(text: str) -> str:
        """Add acture to make text beautify"""
        text = list(text)
        text.insert(0, "```")
        text.append("```")
        return ''.join(text)

    @staticmethod
    def get_uptime() -> str:
        """Get the bot's running uptime"""
        bot_uptime = int(time() - Client.UP_TIME)
        bot_uptime = timedelta(seconds=bot_uptime)
        bot_uptime = define_time(str(bot_uptime))
        return bot_uptime

    @command(name="ping")
    async def ping(self, ctx: Context):
        """Ping of Bot in miliseconds"""
        start_time = time()
        message = await ctx.send("Testing Ping...")
        end_time = time()

        embed = Embed(title="Pong!", color=Colours.soft_red)
        embed.add_field(name=f"Gateway Latency : ", value=f"{round(self.bot.latency * 1000)} ms", inline=False)
        embed.add_field(name=f"Discord API latency :", value=f"{str(end_time - start_time)[2:5]} ms", inline=False)
        embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url_as(format="png"))
        await message.edit(content="", embed=embed)
        
        await ctx.message.add_reaction("🏓")

    @command(name="uptime")
    async def uptime(self, ctx: Context):
        """Bot run's Uptime"""
        bot_uptime = self.get_uptime()
        embed = Embed(title=f"{Emojis.status_online} Bot UpTime!", color=Colours.soft_red, description=f"I Started up `{bot_uptime}` ago!")
        await ctx.send(embed=embed)

    @command(name="invite", aliases=("inv", "invitation", "invite_link"))
    async def invite(self, ctx: Context):
        """Invite the bot to your server"""
        invitation = f"**[Click Here to Invite me!](https://discordapp.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot&permissions=238401607)**"
        embed = Embed(title=f"{Emojis.status_online} Invite me!", color=Colours.soft_red, description=invitation)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url_as(format="png"))
        await ctx.send(embed=embed)

    @command(name="info", alaises=("bot_info", "about", "information"))
    async def info(self, ctx: Context):
        """A basic information to user about the bot"""
        embed = Embed(color=Colours.soft_red)
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url_as(format="png"))
        embed.set_thumbnail(url=self.bot.user.avatar_url_as(format="png"))
        
        embed.add_field(name=f"{Emojis.dev} Developer", value=self.add_acture("Brodevil#3667 (780449492620935168)"), inline=False)
        embed.add_field(name=f"{Emojis.status_online} Uptime", value=self.add_acture(self.get_uptime()), inline=False)
        embed.add_field(name="System", value=self.add_acture(system()), inline=False)
        embed.add_field(name=f"{Emojis.python} Python Version", value=self.add_acture(python_version()), inline=True)
        embed.add_field(name=f"{Emojis.dpy} discord.py Version", value=self.add_acture(__version__), inline=True)
        embed.add_field(name="Ping", value=self.add_acture(f"{round(self.bot.latency * 1000)} ms"), inline=False)
        embed.add_field(name="Commands Count", value=self.add_acture(f"{len(self.bot.commands)} Commands"), inline=False)
        embed.add_field(name="Guild Count", value=self.add_acture(str(len(self.bot.guilds))))
        embed.add_field(name="Users Count", value=self.add_acture(str(len(self.bot.users))))

        await ctx.send(embed=embed)
    

def setup(bot: Bot):
    """Add Cog Bot info"""
    bot.add_cog(Bot_info(bot))
