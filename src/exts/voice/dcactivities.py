from typing import Optional

from discord import VoiceChannel
from discord.ext import commands

from dcactivity import DCApplication
from dcactivity.errors import InvalidChannel


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
            _channel, DCApplication.youtube, max_age=0, max_uses=10)
        
        await ctx.send(invite)


def setup(bot):
    bot.add_cog(MyAdvancedCog(bot))
