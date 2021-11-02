from typing import Optional

from discord import VoiceChannel
from discord.ext.commands import Cog, Context, command
from discord import Embed

from dcactivity import DCApplication

from src.bot import Bot
from src.constants import Colours


APPLICATION = {
    "YOUTUBE" : 1,
    "CHESS" : 2,
    "FISHING" : 3,
    "POKER" : 4,
    "BETRAYAL" : 5
}

APPLICATION_EMBED = Embed(
    title="Application no.",
    description="",
    colour=Colours.soft_red
)

for app, index in APPLICATION.items():
    APPLICATION_EMBED.add_field(name=app, value=f"`{index}`", inline=False)


class ActivityCog(Cog):
    """Custom DCactivity Cog"""
    def __init__(self, bot):
        self.bot = bot


    @command(name="app", aliase=["app_activity", "application"])
    async def youtube_video(self, ctx: Context, *, application: Optional[int] = None, channel: Optional[VoiceChannel] = None):
        """Command used to Play & Watch together"""
        if not channel:
            if not ctx.author.voice:
                return await ctx.send('You need to connect to a voice channel first')

            if not isinstance(ctx.author.voice.channel, VoiceChannel):
                return await ctx.send('This feature is not supported in Stage Channels.')

            _channel = ctx.author.voice.channel

        else:
            _channel = channel

        if not application:
            if application == 1:
                image = "https://shorturl.at/gGQS2"
                application = DCApplication.youtube

            elif application == 2:
                image = "https://i.pinimg.com/736x/3c/4f/18/3c4f1886e5b1d47f3126703fd20f56b7.jpg"
                application = DCApplication.chess

            elif application == 3:
                image = "https://files.brightestgames.com/games/image_large/2021/03/19/fishington-io-315x237.jpg"
                application = DCApplication.fishing

            elif application == 4:
                image = ""
                application = DCApplication.poker

            elif application == 5:
                application = DCApplication.betrayal

            else:
                await ctx.send('Invalid Application No.')



        invite = await self.bot.dcactivity.create_invite(
            _channel, application, max_age=86400, max_uses=20)

        embed = Embed(title="Let's Watch YouTube Together!",
                      color=Colours.soft_red)
        embed.add_field(name="Invitation Link :", value=invite)
        embed.set_image(url="")
        embed.set_footer(text="This link will expire in 24 hours")
        await ctx.send(embed=embed)



def setup(bot: Bot) -> None:
    """Loads the Cog"""
    bot.add_cog(ActivityCog(bot))
