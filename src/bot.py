import logging
import sys

import traceback

import discord 
from discord.ext import commands
from discord.ext import tasks

from  itertools import cycle

from src.constants import Channels      # noqa
from src.exts.backend.logging import Logging           # noqa


log = logging.getLogger(__name__)

__all__ = ("Bot", "bot")



class Bot(commands.Bot):
    """Base bot instance."""

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.statuses = ["The Bot is Currently under the Development by Brodevil#0001", "Hey!", "To kese hain aap log", "RONIT#8477 is Best", 
                        "Nothing special, Just under Development :)", "PLAYGING A GAME", "Author : Brodevil#0001", f'Over {len(set(super().get_all_members()))} users!', 
                        f'Over {len(super().guilds)} guilds!','Forgot your prefix? @mention me!', 'over your mind']
        
        self.change_status.start()


    async def on_ready(self):
        print('Bot had Logged in as :- {0} (ID : {0.id})'.format(self.user))
        print('------' * 11)
    

    @tasks.loop(seconds=10.0)
    async def change_status(self):
        super().wait_until_ready()
        for _ in self.statuses:

            await super().change_presence(status=discord.Status.idle, activity=discord.Game(_), )
            
        


    async def on_mention(self, message):
        pass


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
_intents.reactions = True
_intents.members = True
_intents.typing = True
_intents.presences = True

status=discord.Status.online
activity = discord.Game(name="The Bot is Currently under the Development by Brodevil#0001")
bot = Bot(command_prefix="!", activity=activity, status=status, intents=_intents)
