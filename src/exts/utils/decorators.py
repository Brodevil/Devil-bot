import logging
import asyncio

import discord
from discord.ext import commands
from discord import Embed

from src.constants import Colours
from src.bot import bot

__all__ = ("confim_action")


async def confirm_action(ctx: commands.Context, bot_command: commands.Command):
    await ctx.message.add_reaction("✅") 
    await ctx.message.add_reaction("❌")
    
    def check(reaction, user):
        if user == ctx.message.author:
            if str(reaction.emoji) == '✅' or str(reaction.emoji) == "❌":
                return True
    
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)
    except asyncio.TimeoutError:
        embed = Embed(title="🚫 Action Cancled!", color=Colours.soft_red)
        await ctx.send(embed=embed)
        return 
    
    if str(reaction) == "❌":
        embed = Embed(title="🚫 Action Cancled!", color=Colours.soft_red)
        await ctx.send(embed=embed)
        return
    
    await bot_command()