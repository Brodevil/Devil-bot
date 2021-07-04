import logging 
import sys

from discord.ext import commands
import discord 


log = logging.getLogger(__name__)
__all__ = ("Bot_Controls")


class Bot_Controls(commands.Cog):
    """Bot Control by owner of the Bot"""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    
    @commands.command(name="quit", aliases=("close", "bye", "logout",))
    async def quit(self, ctx: commands.Context):
        is_owner = await ctx.bot.is_owner(ctx.author)
        if is_owner:
            await ctx.message.add_reaction("👋")
            await self.bot.close()
            log.exception(f"{self.bot.user} had logged out by the bot author")
            sys.exit(0)
        
    
    @commands.command(name="status", aliases=("set_status", ))
    async def setstatus(self, ctx: commands.Context, *, text: str):
        is_owner = await ctx.bot.is_owner(ctx.author)
        if is_owner:
            await self.bot.change_presence(activity=discord.Game(name=text))
            await ctx.message.add_reaction("👍")

            log.info(f"Bot's status changed to  :- {text}")
        

    @commands.command(name="dm")
    async def send_dm(self, ctx, member: discord.Member, *, content, show_name:bool = True):
        is_owner = await ctx.bot.is_owner(ctx.author)
        
        if is_owner:
            channel = await member.create_dm()
                   
            if show_name:
                name = ctx.message.author.name
                url = f"https://discordapp.com/users/{ctx.message.author.id}"
                icon = ctx.message.author.avatar_url_as(format="png")

            else:
                name = self.bot.user.name
                url = f"https://discordapp.com/users/{self.bot.user.id}"
                icon = self.bot.user.avatar_url_as(format="png")
            

            embed = discord.Embed(description=content, color=discord.Color.orange)
            embed.set_author(name=name, icon_url=icon, url=url)

            await channel.send(embed=embed)
            await ctx.message.add_reaction("👌")

        

def setup(bot: commands.Bot):
    bot.add_cog(Bot_Controls(bot))