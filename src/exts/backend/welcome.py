import logging

from discord.ext import commands
import discord


class Welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


