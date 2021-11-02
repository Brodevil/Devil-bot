from typing import Optional

from discord import VoiceChannel
from discord.ext.commands import Cog, Context, group, command, cooldown, cooldowns
from discord import Embed

from dcactivity import DCApplication

from src.bot import Bot
from src.constants import Colours


class ActivityCog(Cog):
    """Custom DCactivity Cog"""
    def __init__(self, bot):
        self.bot = bot

    @command(name="youtube", aliase=["yt"])
    async def youtube_video(self, ctx: Context, channel: Optional[VoiceChannel] = None):
        """Command used to watch Youtube together with Friends on Voice Channel"""
        if not channel:
            
            if not ctx.author.voice:
                return await ctx.send('You need to connect to a voice channel first')

            if not isinstance(ctx.author.voice.channel, VoiceChannel):
                return await ctx.send('This feature is not supported in Stage Channels.')

            _channel = ctx.author.voice.channel

        else:
            _channel = channel

        invite = await self.bot.dcactivity.create_invite(
            _channel, DCApplication.youtube, max_age=86400, max_uses=10)

        embed = Embed(title="Let's Watch YouTube Together!",
                      color=Colours.soft_red)
        embed.add_field(name="Invitation Link :", value=invite)
        embed.set_image(url="https://shorturl.at/gGQS2")
        embed.set_footer(text="This link will expire in 24 hours")
        await ctx.send(embed=embed)

    @command(name="poker", aliases=["poker_game"])
    @cooldown(1, 60, cooldowns.BucketType.user)
    async def poker_game(self, ctx: Context, channel: Optional[VoiceChannel] = None):
        """Command used to play poker game with other peoples on Voice Channel"""
        if not channel:
            
            if not ctx.author.voice:
                return await ctx.send('You need to connect to a voice channel first')

            if not isinstance(ctx.author.voice.channel, VoiceChannel):
                return await ctx.send('This feature is not supported in Stage Channels.')

            _channel = ctx.author.voice.channel

        else:
            _channel = channel

        invite = await self.bot.dcactivity.create_invite(
            _channel, DCApplication.poker, max_age=86400, max_uses=10)

        embed = Embed(title="Play Poker Together!", color=Colours.soft_red)
        embed.add_field(name="Invitation Link :", value=invite)
        embed.set_image(url="https://shorturl.at/gGQS2")
        embed.set_footer(text="This link will expire in 24 hours")

        await ctx.send(embed=embed)

    @command(name="chess", aliases=["chess_game"])
    @cooldown(1, 60, cooldowns.BucketType.user)
    async def chess_game(self, ctx: Context, channel: Optional[VoiceChannel] = None):
        """Command used to play chess within 2 players on Voice Channel"""
        if not channel:

            if not ctx.author.voice:
                return await ctx.send('You need to connect to a voice channel first')

            if not isinstance(ctx.author.voice.channel, VoiceChannel):
                return await ctx.send('This feature is not supported in Stage Channels.')

            _channel = ctx.author.voice.channel

        else:
            _channel = channel

        invite = await self.bot.dcactivity.create_invite(
            _channel, DCApplication.chess, max_age=86400, max_uses=10)

        embed = Embed(title="Play Chess Together!", color=Colours.soft_red)
        embed.add_field(name="Invitation Link :", value=invite)
        embed.set_image(url="https://shorturl.at/gGQS2")
        embed.set_footer(text="This link will expire in 24 hours")

        await ctx.send(embed=embed)


def setup(bot: Bot) -> None:
    """Loads the Cog"""
    bot.add_cog(ActivityCog(bot))
