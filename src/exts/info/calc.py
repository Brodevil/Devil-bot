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
        """
        Calculate Mathemacial Experssions :
        ```
        !calc <experssion>
        ```
        Can also use : `calculate`

        This command Basically calculate the Basic Mathemacial Experssions
        Know more about the Arithmetics Operators [here](http://www2.hawaii.edu/~takebaya/cent110/selection/arithmetic_operators.png), 
        which you can use in command! 
        """
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
            message = self.calculator.__doc__
        else:
            ctx.send(message)
        
        embed = discord.Embed(description=message,)
        await ctx.send(embed=embed)

    
def setup(bot: commands.Bot):
    bot.add_cog(Calculation(bot))
