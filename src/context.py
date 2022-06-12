import logging
import asyncio

from discord.ext.commands import Context

from src.exts.utils.exceptions import ActionCancelled

__all__ = ("NewContext", )
logger = logging.getLogger(__name__)


class NewContext(Context):
    """My New Coustum Context"""  

    async def confirm_action(self):
        await self.message.add_reaction("✅") 
        await self.message.add_reaction("❌")

        def check(reaction, user):
            if user == self.message.author:
                if str(reaction.emoji) == '✅' or str(reaction.emoji) == "❌":
                    return True

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            raise ActionCancelled("Time Out! Action Canceled")

        if str(reaction) == "❌":
            raise ActionCancelled("Action Cancled by the user!")

