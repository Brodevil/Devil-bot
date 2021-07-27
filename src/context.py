import asyncio
import logging

from discord.ext.commands import Context
from discord import Embed
from discord.ext import commands

from src.exts.utils.exceptions import ActionCancle

from src.constants import Colours
from src.bot import bot


__all__ = ("NewContext", )

logger = logging.getLogger(__name__)

    
class NewContext(Context):
    """My New Coustum Context"""
    
    async def confirm_action(self):
        """Confirming the Action"""
        await self.message.add_reaction("✅") 
        await self.message.add_reaction("❌")

        def check(reaction, user):
            if user == self.message.author:
                if str(reaction.emoji) == '✅' or str(reaction.emoji) == "❌":
                    return True

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            embed = Embed(title="🚫 Action Cancled!", color=Colours.soft_red)
            await self.send(embed=embed)
            raise ActionCancle("Time Out! So Action Cancled!")

        if str(reaction) == "❌":
            embed = Embed(title="🚫 Action Cancled!", color=Colours.soft_red)
            await self.send(embed=embed)
            raise ActionCancle("Action Cancle by the user!")

