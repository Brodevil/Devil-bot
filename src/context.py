import asyncio

from discord.ext.commands import Context
import discord

from src.bot import bot
from src.exts.utils.decorators import confirm_action
from src.exts.utils.exceptions import ActionCancle


class NewContext(Context):
    """My New Coustum Context"""
    
    async def confirm_action(self):
        """Confirming the Action"""
        if await confirm_action(ctx=self) is None:
            raise ActionCancle("Anction Cancled")
        
        else:
            pass

