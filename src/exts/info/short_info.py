from logging import getLogger
from inspect import Parameter, _ParameterKind

import discord
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, command

from src.constants import Colours
from src.utils.maths import calc_expression
from src.exts.utils.converter import acute_remover
from src.exts.utils.exceptions import UnableToReach


log = getLogger(__name__)


class ShortInfo(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @command(name="calculate", aliases=("calc", ))
    async def calculator(self, ctx: Context, *,  term: str):
        """
        Calculate 
        """
        term = acute_remover(term)
        answer = calc_expression(term)

        if answer is not None:
            embed = discord.Embed(
                description=f"**Your Answer is : **\n```\n{answer}```", color=Colours.soft_red)
            await ctx.reply(embed=embed)

        else:
            raise commands.MissingRequiredArgument(
                Parameter(name="prefix", kind=_ParameterKind.VAR_POSITIONAL))

    @calculator.error
    async def calculator_error(self, ctx: Context, _error):
        if isinstance(_error, commands.MissingRequiredArgument):
            message = """
            This command calculates the Basic Mathematical Experssions
            Know more about the Arithmetics Operators [here](http://www2.hawaii.edu/~takebaya/cent110/selection/arithmetic_operators.png), 
            which you can use in command! 
            """

            embed = discord.Embed(title="Calculate!",
                                  description="```!calculate <experssion>```",)
            embed.add_field(
                name=f"Can also use : `{', '.join(ctx.command.aliases)}`", value=message)
            await ctx.send(embed=embed)


def setup(bot: Bot) -> None:
    bot.add_cog(ShortInfo(bot))
