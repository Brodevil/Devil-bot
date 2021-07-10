import random
import logging

import asyncio

from discord.ext import commands
from discord import Embed
import discord

import typing 

from src.constants import Colours           # noqa
from src.exts.utils import checkers         # noqa


class Random_fun(commands.Cog):
    """ Fun commands from random module """
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="guess", aliases=("guess_num",), pass_context=True)
    async def guess_num(self, ctx: commands.Context, num1: int = 1, num2: int = 10):

        num1, num2 = int(num1), int(num2)

        await ctx.send(f"**Guess a number from {num1} to {num2},\nYou had 5 chances to Guess the Correct number 😈!**")

        answer = random.randint(num1, num2)
        guess = 5

        while guess != 0:
            try:
                user_guess = await self.bot.wait_for('message', check=checkers.random_num_check(ctx.author), timeout=10)
            except asyncio.TimeoutError:
                await ctx.send(f"**{ctx.message.author.mention}\n⏰ Time out!, Please try again**")
                break

            guess_num = int(user_guess.content)

            if guess_num == answer:
                embed = Embed(description=f"**🥳 Congratulation!\n<a:Tick:808218568457715742> You had Correctly answered in {5-guess+1} Guess.**", color=Colours.blue)
                await user_guess.reply(embed=embed)
                break

            elif guess_num > answer:
                await ctx.send(f"**{ctx.message.author.name}, Try to go ⬇️ lower! {guess} Guesses left.**")

            elif guess_num < answer:
                await ctx.send(f"**{ctx.message.author.name}, Try to go ⬆️ higher! {guess} Guesses left.**")

            guess -= 1

        else:
            embed = Embed(description="**I am Sorry 😔\nYou loss! Please Try again**", colour=Colours.soft_red)
            await ctx.send(embed=embed)


    @commands.command(name="thief", aliases=("hold", "caught", ))
    async def caught_user(self, ctx: commands.Context, role: typing.Optional[discord.Role]=None, *, reason: str):
        if role is None:
            role = ctx.message.guild.default_role
        
        thief = random.choice(role.members)

        embed = Embed(description=f"**{thief.mention} is the Thief!**\n\n{thief.name} been caught due to the reason :\n```\n{reason}```")
        embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url_as(format="png"))

        await ctx.send(embed=embed)
        
    
    @commands.command(name="dice", aliases=("dice_throw", "roll_dice")
    async def roll_dice(self, ctx: commands.Context):
        pass

def setup(bot: commands.Bot):
    bot.add_cog(Random_fun(bot))
