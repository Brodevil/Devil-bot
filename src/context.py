import asyncio
import logging

from discord.ext.commands import Context
from discord.ext.commands import Bot

from src.exts.utils.exceptions import ActionCancle


__all__ = ("NewContext", )
logger = logging.getLogger(__name__)

    
class NewContext(Context):
    """My New Coustum Context"""
    def __init__(self, bot: Bot, **attrs):
        self.bot = bot
        super().__init__(**attrs)
    

    async def confirm_action(self):
        """Confirming the Action"""
        await self.message.add_reaction("✅") 
        await self.message.add_reaction("❌")

        def check(reaction, user):
            if user == self.message.author:
                if str(reaction.emoji) == '✅' or str(reaction.emoji) == "❌":
                    return True

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            raise ActionCancle("Time Out! So Action Cancled!")

        if str(reaction) == "❌":
            raise ActionCancle("Action Cancle by the user!")

