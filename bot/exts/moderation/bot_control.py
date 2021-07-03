import logging 
import sys

from discord.ext import commands
import discord 



log = logging.getLogger(__name__)
__all__ = ("Bot_Controls")


class Bot_Controls(commands.Cog):
    """Bot Control by owner of the Bot"""
    
    def __init__(self, bot: commands.Bot):
        super().__init__(bot)
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
        

def setup(bot: commands.Bot):
    bot.add_cog(Bot_Controls(bot))