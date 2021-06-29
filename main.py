import logging

from discord.ext import commands
import discord

from bot.commands import setup
from bot.constants import Client


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



intents = discord.Intents.default()
intents.members = True
activity = discord.Game(name="The Bot is Currently under the Development by Brodevil#0001")
bot = commands.Bot(command_prefix="!", activity=activity, status=discord.Status.online)


@bot.event
async def on_ready():
    print('Bot had Logged in as :- {0} ({0.id})'.format(bot.user))
    print('------'*10)
    bot_owner = discord.Client.get_user(id=780449492620935168)
    # icon = bot.(format="png")
    #
    # embed = discord.Embed(description="Connected!")
    # embed.set_author(name="Mr. Devil", icon_url=icon)

    await bot_owner.send("hello")

setup(bot)
bot.run(Client.TOKEN)
