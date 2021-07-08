from discord.ext.commands import errors
from discord.ext import commands
import discord

from src.constants import Colours  # noqa
from src.utils.maths import calc_expresion  # noqa
from src.utils.converter import acute_remover   # noqa


class Calculation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    
    @commands.command(name="calc", aliases=("calculate", ))
    async def calculator(self, ctx: commands.Context, *,  term : str):
        term = acute_remover(term)
        answer = calc_expresion(term)
        
        if answer is not None:
            embed = discord.Embed(description=f"**Your Answer is : **\n```\n{answer}```", color=Colours.yellow)
            await ctx.reply(embed=embed)    
        
        else:
            raise errors.MissingRequiredArgument
            

    @calculator.error 
    async def calculator_error(self, ctx: commands.Context, _error):
        if isinstance(_error, errors.MissingRequiredArgument):
            message = f"**You should also mention the Calculation term :**\n```\n!calc <expression>```\n\nCalculate the Mathematical basics experssions\n" \
                      f"Know more about the Arithmetics Operators [here](https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp), \nwhich you can use in command! "
        else:
            return
        
        embed = discord.Embed(description=message,)
        await ctx.send(embed=embed)

    
def setup(bot: commands.Bot):
    bot.add_cog(Calculation(bot))
