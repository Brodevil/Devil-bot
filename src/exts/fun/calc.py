from discord.ext.commands import errors
from discord.ext import commands
import discord

from src.constants import Colours  # noqa


class Calculation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    
    @commands.command(name="calc", aliases=("calculate", ))
    async def calculator(self, ctx: commands.Context, *,  term : str):
        try:
            answer = eval(term)
        except Exception:
            pass

        else:
            embed = discord.Embed(description=f"**Your Answer is : **\n```\n{answer}```", color=Colours.yellow)
            await ctx.reply(embed=embed)


    @calculator.error 
    async def calculator_error(self, ctx: commands.Context, _error):
        if isinstance(_error, errors.MissingRequiredArgument):
            message = f"**You should also mention the Calculation term :**\n```\n!calc <expression>```\n\nCalculate the Mathematical basics experssions\n" \
                      f"Know more about the Arithmetics Operators [here](https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp), which you can Use in command! "

        else:
            return
        
        embed = discord.Embed(description=message,)
        await ctx.send(embed=embed)


    
def setup(bot: commands.Bot):
    bot.add_cog(Calculation(bot))
