import logging
import sys

from discord.ext import commands 
import discord
import asyncio

from bot.exts.commands.commands import setup
from bot.constants import Client


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



intents = discord.Intents.default()
intents.members = True
activity = discord.Activity(type=discord.Game(name="The Bot is Currently under the Development by Brodevil#0001"))
bot = commands.Bot(command_prefix="!", activity=activity, status=discord.Status.online)


@bot.event
async def on_ready():
    int('Bot had Logged in as :- {0} ({0.id})'.format(bot.user))
    print('------'*10)
    user = await bot.get_user(Client.OWNER_ID)
    icon = bot.avatar_url_as(format="png")

    embed = discord.Embed(description="Connected!")
    embed.set_author(name="Mr. Devil", icon_url=icon)

    await user.send(embed=embed)



setup(bot)
bot.run(Client.TOKEN)
