import logging
import sys

import asyncio
from json import load
import traceback

import discord
from discord.ext import commands
from discord.ext import tasks
from aiohttp import ClientSession

from src.context import NewContext
from src.constants import Client
from src.exts.backend.database import Database
from dcactivity import DCActivity


log = logging.getLogger(__name__)

__all__ = ("Bot", "bot")


class Bot(commands.Bot):
    """Base bot instance."""

    def __init__(self, activies, status, **kwargs):
        super().__init__(**kwargs)
        self.database = Database()
        self.activies = activies
        self.status = status
        self.change_status.start()
        self.unban_loop.start()
        self.dcactivity = DCActivity(self)
        self.http_session = ClientSession()

    async def on_ready(self):
        print('Bot had Logged in as :- {0} (ID : {0.id})'.format(self.user))
        print('------' * 11)

    @tasks.loop(seconds=30.0)
    async def change_status(self):
        """Changing the status on loop yee!"""
        for _ in self.activies:
            await super().change_presence(status=self.status, activity=discord.Game(_), )
            await asyncio.sleep(30.0)

    @tasks.loop(minutes=1.0)
    async def unban_loop(self):
        """Unban the users"""
        SCRIPTS = """{0} FROM bans WHERE unban_on < NOW();"""
        self.database.run(SCRIPTS.format(
            "SELECT user_id, guild_id"), commit=False)

        for user_id, guild_id in self.database.cursor.fetchall():
            try:
                guild = self.get_guild(int(guild_id))
                user = self.get_user(int(user_id))
                await guild.unban(user)
                if not user.bot:
                    await user.send(f"**You have been unbanned from {guild.name} Server**")
            except Exception as error:
                error = f"Could not unban user {user_id} from guild {guild_id} due to : {error}"
                log.error(error)
                print(error, file=sys.stderr)

        self.database.run(SCRIPTS.format("DELETE"), commit=True)

    @unban_loop.before_loop
    @change_status.before_loop
    async def before_loops(self):
        """Work to be done before the loops get started!"""
        await super().wait_until_ready()

    async def get_context(self, message, *, cls=None):
        """Get the custem context"""
        return await super().get_context(message=message, cls=cls or NewContext)

    def load_extensions(self,  extensions: list):
        """fucntion to loads the Extension/Cogs"""
        for extension in extensions:
            try:
                self.load_extension(extension)
            except Exception as error:
                error = f'Could not load extension {extension} due to \
                    {error.__class__.__name__}: {error}'
                print(error, file=sys.stderr)
                traceback.print_exc()
                log.error(error)

        # self.load_extension('jishaku')
        self.total_cogs = list(self.cogs)


with open("src/resource/status.json", "rb") as _activies:
    _activies = load(_activies)
    _activies = list(_activies["Bot_Status"])

_intents = discord.Intents.default()
_intents.reactions = True
_intents.members = True
_intents.typing = True
_intents.presences = True

STATUS = discord.Status.online

bot = Bot(
    activies=_activies,
    command_prefix=commands.when_mentioned_or(*Client.PREFIX),
    status=STATUS,
    intents=_intents
)
