import random
import logging

import asyncio

from discord.ext import commands
from discord import Embed


from src.constants import Colours
from src.exts.utils import checkers


class Random_fun(commands.Cog):
    """ Fun commands from random module """
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="guess", aliases=("guess_num",), pass_context=True)
    async def guess_num(self, ctx: commands.Context):

        num1, num2 = 1, 15
        embed = Embed(description=f"**Guess a number from {num1} to {num2}, You had 5 chances to Guess number 😈!**", color=Colours.soft_red)

        await ctx.send(embed=embed)
        answer = random.randint(num1, num2)
        guess = 4

        while guess != 0:
            try:
                user_guess = await self.bot.wait_for('message', check=checkers.random_num_check(ctx.author), timeout=10)
            except asyncio.TimeoutError:
                await ctx.send(f"**Time out!, {guess} Guesses Left now!**")
                continue

            user_guess = int(user_guess.content)

            if user_guess == answer:
                embed = Embed(description=f"**Congratulation!\nYou had used {guess} Guesses.\nGood job!**", color=Colours.blue)
                await ctx.send(embed=embed)
                break

            elif user_guess > answer:
                await ctx.send(f"**Try to go lower! {guess} Guesses left.**")

            elif user_guess < answer:
                await ctx.send(f"**Try to go higher! {guess} Guesses left.**")

            guess -= 1

        else:
            embed = Embed(description="**You loss! Please Try again**", colour=Colours.soft_red)
            await ctx.send(embed=embed)



def setup(bot: commands.Bot):
    bot.add_cog(Random_fun(bot))
