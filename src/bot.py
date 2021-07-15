import logging
import sys

import traceback
import asyncio
import json 

import discord 
from discord.ext import commands
from discord.ext import tasks

from src.constants import Channels      # noqa
from src.exts.backend.logging import Logging           # noqa


log = logging.getLogger(__name__)

__all__ = ("Bot", "bot")



class Bot(commands.Bot):
    """Base bot instance."""

    def __init__(self, statuses, **kwargs):
        super().__init__(**kwargs)
        self.statuses = statuses
        self.change_status.start()


    async def on_ready(self):
        print('Bot had Logged in as :- {0} (ID : {0.id})'.format(self.user))
        print('------' * 11)
    

    @tasks.loop(seconds=30.0)
    async def change_status(self):
        """Changing the status on loop yee!"""
        await super().wait_until_ready()
        
        for _ in self.statuses:
            await super().change_presence(status=status, activity=discord.Game(_), )   
            await asyncio.sleep(30.0)


    def loading_extensions(self, extensions : list=None, reload=False, extension=None):
        if extension is None and extensions is not None:
            for extension in extensions:
                try:
                    if reload:
                        self.reload_extension(extension)
                    else:
                        self.load_extension(extension)
                except Exception as error:
                    print('Could not load extension {0} due to {1.__class__.__name__}: {1}'.format(extension, error),  file=sys.stderr)
                    traceback.print_exc()
                    log.error('Could not load extension {0} due to {1.__class__.__name__}: {1}'.format(extension, error))
        else:
            try:
                self.reload_extension(extension)
            except Exception as error:
                print('Could not load extension {0} due to {1.__class__.__name__}: {1}'.format(extension, error),  file=sys.stderr)
                traceback.print_exc()
                log.error('Could not load extension {0} due to {1.__class__.__name__}: {1}'.format(extension, error))



with open("src\\resource\\extensions\\status.json", "wt") as _status:
    _status = json.load(_status)
    _status = list(_status["Bot_Status"])

_intents = discord.Intents.default()
_intents.reactions = True
_intents.members = True
_intents.typing = True
_intents.presences = True

status=discord.Status.online
activity = discord.Game(name="The Bot is Currently under the Development by Brodevil#0001")

bot = Bot(
    statuses=_status,
    command_prefix="!", 
    activity=activity, 
    status=status, 
    intents=_intents
    )
