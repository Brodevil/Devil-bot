import logging
import sys

import traceback
import asyncio
import json 

import discord 
from discord.ext import commands
from discord.ext import tasks

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


    def loading_extensions(self,  extensions : list=None, reload=False, extension=None):
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

                    yield 'Could not load extension {0} due to {1.__class__.__name__}: {1}'.format(extension, error)
            
            else:
                return True

        else:   
            try:
                self.reload_extension(extension)
            except Exception as error:
                print('Could not load extension {0} due to {1.__class__.__name__}: {1}'.format(extension, error),  file=sys.stderr)
                traceback.print_exc()
                log.error('Could not load extension {0} due to {1.__class__.__name__}: {1}'.format(extension, error))

                return 'Could not load extension {0} due to {1.__class__.__name__}: {1}'.format(extension, error)
            else:
                return True 

with open("src\\resource\\extensions\\status.json") as _activies:
    _activies = json.load(_activies)
    _activies = list(_activies["Bot_Status"])

_intents = discord.Intents.default()
_intents.reactions = True
_intents.members = True
_intents.typing = True
_intents.presences = True

status=discord.Status.online

bot = Bot(
    activies=_activies,
    command_prefix="!", 
    status=status, 
    intents=_intents
    )
