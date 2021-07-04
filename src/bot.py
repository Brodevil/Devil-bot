import logging

from discord.ext import commands
import discord 

from src.constants import Channels


log = logging.getLogger(__name__)

__all__ = ("Bot", "bot")



class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)


    async def on_ready(self):
        print('Bot had Logged in as :- {0} ({0.id})'.format(self.user))
        print('------' * 10)
        


_intents = discord.Intents(messages=True, guilds=True)
_intents.reactions = True
_intents.members = True

activity = discord.Game(name="The Bot is Currently under the Development by Brodevil#0001")
bot = Bot(command_prefix="!", activity=activity, status=discord.Status.dnd, intents=_intents)
