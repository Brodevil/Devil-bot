from re import L
from typing import Optional

from discord import VoiceChannel
from discord.ext.commands import Cog, Context, command
from discord import Embed

from dcactivity import DCApplication

from src.bot import Bot
from src.constants import Colours


APPLICATION = {
    "YOUTUBE": 1,
    "CHESS": 2,
    "FISHING": 3,
    "POKER": 4,
    "BETRAYAL": 5
}

APPLICATION_EMBED = Embed(
    title="Application no.",
    description="```d!app <application no.> [channel]``` \n\
    Following are the application no. of several Activity",
    colour=Colours.soft_red
)

for app, index in APPLICATION.items():
    APPLICATION_EMBED.add_field(name=app, value=f"`{index}`", inline=False)


class ActivityCog(Cog):
    """Custom DCactivity Cog"""

    def __init__(self, bot):
        self.bot = bot

    @command(name="app", aliase=["app_activity", "application"])
    async def youtube_video(self, ctx: Context, *,
                            application: Optional[int] = None,
                            channel: Optional[VoiceChannel] = None
                            ) -> None:
        """Command used to Play & Watch together"""
        if not channel:
            if not ctx.author.voice:
                return await ctx.send('You need to connect to a voice channel first')

            if not isinstance(ctx.author.voice.channel, VoiceChannel):
                return await ctx.send('This feature is not supported in Stage Channels.')
            _channel = ctx.author.voice.channel

        else:
            _channel = channel

        if application:
            if application == 1:
                statement = "Let's Watch YouTube Together (youtube)!"
                image = "https://cdn.dribbble.com/users/5481035/screenshots/15978603/yt_animation_dribble.gif"
                app = DCApplication.youtube

            elif application == 2:
                statement = "Let's CG 2 DEV (Chess) together!"
                image = "https://c.tenor.com/i4cgk6ejhBMAAAAC/chess.gif"
                app = DCApplication.chess

            elif application == 3:
                statement = "Let's Play Fishington.io (fishing) Game together!"
                image = "https://files.brightestgames.com/games/image_large/2021/03/19/fishington-io-315x237.jpg"
                app = DCApplication.fishing

            elif application == 4:
                statement = "Let's Play Poker Night (poker) together!"
                image = "https://upload.wikimedia.org/wikipedia/en/b/bb/Poker-night-at-the-inventory-cover.JPG"
                app = DCApplication.poker

            elif application == 5:
                statement = "Let's Play Betrayal.io (betrayal) together!"
                image = "https://i.ytimg.com/vi/Q8KbGO3UqZg/maxresdefault.jpg"
                app = DCApplication.betrayal

            else:
                await ctx.send('Invalid Application No.')
                await ctx.send(embed=APPLICATION_EMBED)
                return
        else:
            await ctx.send(embed=APPLICATION_EMBED)
            return

        invite = await self.bot.dcactivity.create_invite(
            voice_channel=_channel, application=app, max_age=86400, max_uses=20
        )

        embed = Embed(title=statement, color=Colours.soft_red)
        embed.add_field(name="Invitation Link :", value=invite)
        embed.set_image(url=image)
        embed.set_footer(text="This link will expire in 24 hours")
        await ctx.send(embed=embed)

    @command(name="youtube", aliases=["youtube_video", "yt"])
    async def youtube_video(self, ctx: Context, channel: Optional[VoiceChannel] = None) -> None:
        """Command used to Play & Watch together"""
        if not channel:
            if not ctx.author.voice:
                return await ctx.send('You need to connect to a voice channel first')

            if not isinstance(ctx.author.voice.channel, VoiceChannel):
                return await ctx.send('This feature is not supported in Stage Channels.')
            _channel = ctx.author.voice.channel

        else:
            _channel = channel

        invite = await self.bot.dcactivity.create_invite(
            voice_channel=_channel, application=DCApplication.youtube, max_age=86400, max_uses=20
        )
        image = "https://cdn.dribbble.com/users/5481035/screenshots/15978603/yt_animation_dribble.gif"

        embed = Embed(title="Let's Watch YouTube Together!",
                      color=Colours.soft_red)
        embed.add_field(name="Invitation Link :", value=invite)
        embed.set_image(url=image)
        embed.set_footer(text="This link will expire in 24 hours")
        await ctx.send(embed=embed)


def setup(bot: Bot) -> None:
    """Loads the Cog"""
    bot.add_cog(ActivityCog(bot))
