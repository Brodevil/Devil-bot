import logging
import sys

import traceback

import discord 
from discord.ext import commands
from discord.ext import tasks

from src.constants import Channels      # noqa
from src.exts.backend.logging import Logging           # noqa


log = logging.getLogger(__name__)

__all__ = ("Bot", "bot")



class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        
    async def on_ready(self):
        print('Bot had Logged in as :- {0} (ID : {0.id})'.format(self.user))
        print('------' * 11)
    

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



_intents = discord.Intents.default()
_intents.reactions = False
_intents.members = True
_intents.typing = False
_intents.presences = True

activity = discord.Game(name="The Bot is Currently under the Development by Brodevil#0001")
bot = Bot(command_prefix="!", activity=activity, status=discord.Status.dnd, intents=_intents)
