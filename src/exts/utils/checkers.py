import discord
import asyncio

from src.bot import bot

__all__ = ("confirm_action", "random_num_check")


async def confirm_action(ctx):
    """Confirming the Action"""
    await ctx.message.add_reaction("✅") 
    await ctx.message.add_reaction("❌")

    def check(reaction, user):
        if user == ctx.message.author:
            if str(reaction.emoji) == '✅' or str(reaction.emoji) == "❌":
                return True

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)
    except asyncio.TimeoutError:
        return False

    if str(reaction) == "❌":
        return False
    
    else:
        return True


def random_num_check(author: discord.User):
    def inner_check(message):
        if message.author != author:
            return False
        try:
            int(message.content)
            return True
        except ValueError:
            return False

    return inner_check

