import logging
from typing import Union

import discord
from discord.ext import commands

from src.bot import Bot
from src.constants import Colours

logger = logging.getLogger(__name__)

API_URL = "https://api.genderize.io/?name={0}"

ERROR_EMBED = discord.Embed(
    title="Error while searching Gender",
    description="There was an error while trying to reach `genderize.io`. Please try again shortly.",
    color=Colours.soft_red,
)

NAME_ERROR = discord.Embed(
    title="Unfamiliar Name",
    description="The name you entered is not familiar to me. Please try again.",
    colour=Colours.soft_red
)


class Gender(commands.Cog):
    def __init__(self, bot : Bot):
        self.bot = bot

    async def gender_info(self, name: str) -> Union[bool, None, int]:
        """Returns the Gender of Name """
        async with self.bot.http_session.get(url=API_URL.format(name), ssl=False) as response:
            if response.status != 200:
                logger.error(
                    f"Unexpected status code {response.status} from genderize.io"
                )
                return 200

            gender = await response.json()
            gender = gender["gender"]
            
            if gender == "null":
                return None
            elif gender == "male":
                return True
            elif gender == "female":
                return False


    @commands.command(aliases=["sex", "gender"])
    @commands.cooldown(1, 10, commands.cooldowns.BucketType.user)
    async def gender_of(self, ctx: commands.Context, name: str):
        """Get the Gender of name"""
        async with ctx.typing():
            name = name.capitalize()
            is_male = await self.gender_info(name)

            if is_male == 200:
                await ctx.send(embed=ERROR_EMBED)
            
            elif is_male is None:
                await ctx.send(embed=NAME_ERROR)
            
            elif is_male == True:
                embed = discord.Embed(
                    description=f"**Name : {name} \nGender : Male**",
                    color=Colours.blue
                )
                await ctx.send(embed=embed)
            
            elif is_male == False:
                embed = discord.Embed(
                    description=f"**Name : {name} \nGender : Female**",
                    color=Colours.pink
                )
                await ctx.send(embed=embed)



def setup(bot: Bot) -> None:
    """Load the Real Python Cog."""
    bot.add_cog(Gender(bot))
