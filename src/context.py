import logging

from discord.ext.commands import Context

from src.exts.utils.exceptions import ActionCancle
from src.exts.utils.checkers import confirm_action
from src.bot import bot


__all__ = ("NewContext", )
logger = logging.getLogger(__name__)


class NewContext(Context):
    """My New Coustum Context"""  

    async def confirm_action(self):
        action = confirm_action(self)

        if action == False:
            raise ActionCancle("Action Cancled by the user")
        

bot.get_context("Confirm actions", NewContext)
