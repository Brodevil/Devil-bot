from typing import Optional

from discord import VoiceChannel
from discord.ext import commands
from discord import Embed

from dcactivity import DCApplication

from src.bot import Bot
from src.constants import Colours


class MyAdvancedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="video", aliase=["vid", "v"])
    async def youtube_video(self, ctx: commands.Context, channel: Optional[VoiceChannel] = None):
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

        embed = Embed(title="Let's Watch YouTube Together!", color=Colours.soft_red)
        embed.set_image(url="https://shorturl.at/gGQS2")
        embed.set_footer(text=f"**Invitation Link :** {invite}")
        
        await ctx.send(embed=embed)


    @commands.command(name="twitch", aliases=["twitchtv"])
    async def twitch_video(self, ctx: commands.Context, channel: Optional[VoiceChannel] = None):
        if not channel:
            if not ctx.author.voice:
                return await ctx.send('You need to connect to a voice channel first')
            
            if not isinstance(ctx.author.voice.channel, VoiceChannel):
                return await ctx.send('This feature is not supported in Stage Channels.')
            
            _channel = ctx.author.voice.channel
        
        else:
            _channel = channel
        
        invite = await self.bot.dcactivity.create_invite(
            _channel, DCApplication.twitch, max_age=86400, max_uses=10)
        
        embed = Embed(title="Let's Watch Twitch Together!", color=Colours.soft_red)
        embed.set_image(url="https://shorturl.at/gGQS2")
        embed.set_footer(text=f"**Invitation Link : {invite}")
        
        await ctx.send(embed=embed)


def setup(bot: Bot) -> None:
    bot.add_cog(MyAdvancedCog(bot))
