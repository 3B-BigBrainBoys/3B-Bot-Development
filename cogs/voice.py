
import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio


class voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()    
    async def join(self, ctx):
        if ctx.voice_client != None:
            await ctx.voice_client.move_to(ctx.author.voice.channel)
        else:
            channel = ctx.author.voice.channel
            await channel.connect()

    @commands.command()
    async def isoccupied(self, ctx):
        if ctx.voice_client != None:
            await ctx.send("Bot is in a channel")
        else:
            await ctx.send("Bot is not connected to a channel")

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client != None:
            await ctx.voice_client.disconnect()
        else:
            await ctx.send("Bot is not in a channel...")
"""
    @commands.command(brief="Plays an mp3")
    async def play(self, ctx):
        source = FFmpegPCMAudio('song.mp3')
        player = ctx.voice_client.play(source)
"""
async def setup(bot):
    await bot.add_cog(voice(bot))