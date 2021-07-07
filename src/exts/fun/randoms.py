import random
import logging

import asyncio

from discord.ext import commands
from discord import Embed
import discord


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
                await ctx.send(f"**{ctx.message.author.mention} Time out!, Please try again**")
                break

            guess_num = int(user_guess.content)

            if guess_num == answer:
                embed = Embed(description=f"**🥳 Congratulation!\nYou had Correctly answered in {5-guess} Guess <a:Tick:808218568457715742>.**", color=Colours.blue)
                await user_guess.reply(embed=embed)
                break

            elif guess_num > answer:
                await ctx.send(f"**{ctx.message.author.name}, Try to go lower! {guess} Guesses left.**")

            elif guess_num < answer:
                await ctx.send(f"**{ctx.message.author.name}, Try to go higher! {guess} Guesses left.**")

            guess -= 1

        else:
            embed = Embed(description="**You loss! Please Try again**", colour=Colours.soft_red)
            await ctx.send(embed=embed)


    @commands.command(name="thief", aliases=("hold", "caught", ))
    async def caught_user(self, ctx: commands.Context, member: discord.Role, *, reason: str):
        pass



def setup(bot: commands.Bot):
    bot.add_cog(Random_fun(bot))
