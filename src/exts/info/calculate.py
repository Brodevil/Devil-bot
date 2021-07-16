from inspect import Parameter, _ParameterKind

from discord.ext import commands
import discord

from src.constants import Colours  
from src.utils.maths import calc_expresion  
from src.utils.converter import acute_remover   


class Calculation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    
    @commands.command(name="calculate", aliases=("calc", ))
    async def calculator(self, ctx: commands.Context, *,  term : str):
        """
        Calculate 
        """
        term = acute_remover(term)
        answer = calc_expresion(term)

        if answer is not None:
            embed = discord.Embed(description=f"**Your Answer is : **\n```\n{answer}```", color=Colours.soft_red)
            await ctx.reply(embed=embed)    
        
        else:
            raise commands.MissingRequiredArgument(
                        Parameter(name="prefix", kind=_ParameterKind.VAR_POSITIONAL))
            

    @calculator.error 
    async def calculator_error(self, ctx: commands.Context, _error):
        if isinstance(_error, commands.MissingRequiredArgument):
            message = """
            This command calculates the Basic Mathemacial Experssions
            Know more about the Arithmetics Operators [here](http://www2.hawaii.edu/~takebaya/cent110/selection/arithmetic_operators.png), 
            which you can use in command! 
            """
        
        else:
            await ctx.send(message)
        
        embed = discord.Embed(title="Calculate!", description="```!calculate <experssion>```",)
        embed.add_field(name=f"Can also use : `{', '.join(ctx.command.aliases)}`", value=message)
        await ctx.send(embed=embed)

    
def setup(bot: commands.Bot):
    bot.add_cog(Calculation(bot))
