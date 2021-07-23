import logging
import sys

import traceback
import asyncio
import json 

import discord 
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands.core import command

from src.constants import Channels      
from src.exts.backend.logging import Logging           

log = logging.getLogger(__name__)

__all__ = ("Bot", "bot")



class Bot(commands.Bot):
    """Base bot instance."""

    def __init__(self, activies, status, **kwargs):
        super().__init__(**kwargs)
        self.activies = activies
        self.status = status
        self.change_status.start()


    async def on_ready(self):
        print('Bot had Logged in as :- {0} (ID : {0.id})'.format(self.user))
        print('------' * 11)
    

    @tasks.loop(seconds=30.0)
    async def change_status(self):
        """Changing the status on loop yee!"""
        await super().wait_until_ready()
        
        for _ in self.activies:
            await super().change_presence(status=self.status, activity=discord.Game(_), )   
            await asyncio.sleep(30.0)


    def loading_extensions(self,  extensions : list = None, reload=False, single_cog=None):
        if single_cog is None and extensions is not None:
            for extension in extensions:
                if reload:
                    self.reload_extension(extension)
                else:
                    self.load_extension(extension)
        else:   
            self.reload_extension(single_cog)
        
    
    async def confirm_command(self, ctx: commands.Context, bot_command: commands.Command):
        await ctx.message.add_reaction("✅")
        await ctx.message.add_reaction("❌")
        
        def check(reaction, user):
            if user == ctx.message.author:
                if str(reaction.emoji) == '✅' or str(reaction.emoji) == "❌":
                    return True
        
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            embed = Embed(title="🚫 Action Cancled!", color=constants.Colours.soft_red)
            await ctx.send(embed=embed)
            return 
        
        if str(reaction) == "❌":
            embed = Embed(title="🚫 Action Cancled!", color=constants.Colours.soft_red)
            await ctx.send(embed=embed)
            return
        
        await bot_command()



with open("src\\resource\\extensions\\status.json") as _activies:
    _activies = json.load(_activies)
    _activies = list(_activies["Bot_Status"])

_intents = discord.Intents.default()
_intents.reactions = True
_intents.members = True
_intents.typing = True
_intents.presences = True

status=discord.Status.online
prefix = ("d!", "md!", "~")

bot = Bot(
    activies=_activies,
    command_prefix=prefix, 
    status=status, 
    intents=_intents
    )
