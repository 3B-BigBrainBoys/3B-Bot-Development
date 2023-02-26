
import discord
from discord.ext import commands


class voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()    
    async def join(self, ctx):
        if ctx.voice_client != None:
            await ctx.move_to(ctx.voice.author.voice.channel)
        else:
            channel = ctx.author.voice.channel
            await channel.connect()

    @commands.command()
    async def isoccupied(self, ctx):
        if ctx.voice_client.is_connected():
            await ctx.send("Bot is occupied")

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client != None:
            await ctx.voice_client.disconnect()
        else:
            await ctx.send("Bot is not in a channel...")

async def setup(bot):
    await bot.add_cog(voice(bot))