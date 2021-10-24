import logging
from typing import Optional

from discord import (
    VoiceChannel, 
    PCMVolumeTransformer, 
    FFmpegPCMAudio
)

from discord.ext import commands
from discord.ext.commands import Context

from src.bot import bot
from src.exts.voice.youtubeWork import YTDLSource


class Music(commands.Cog):
    def __init__(self, bot: bot):
        self.bot = bot

    @commands.command(name="connect", aliases=["join", ])
    async def join(self, ctx: Context, *, channel: Optional[VoiceChannel]):
        """Joins a voice channel"""
        
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()
    
    @commands.command(name="disconnect")
    async def disconnect(self, ctx):
        """Stops and disconnects the bot from voice"""
        await ctx.voice_client.disconnect()

    @commands.command(name="volume")
    async def volume(self, ctx: Context, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")
    

    @commands.is_owner()
    @commands.command(name="local_play", aliases=["lp", "play_file"])
    async def play_from_file(self, ctx, *, query: str):
        """Plays a file from the local filesystem"""

        source = PCMVolumeTransformer(FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {query}')


    @commands.command(name="play", aliases=("p", "play_song", "song"))
    async def play(self, ctx: Context, *, queary: str):
        """Play from a url / Song queary"""

        async with ctx.typing():
            player = await YTDLSource.from_url(queary, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {player.title}')


    @play.before_invoke
    @play_from_file.before_invoke
    async def ensure_voice(self, ctx: Context):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()


def setup(bot: bot) -> None:
    bot.add_cog(Music(bot))
