
import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import app_commands


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

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        vc = member.guild.voice_client
        if not vc:
            return
        
        if len(vc.channel.members) == 1:
            await vc.disconnect()




async def setup(bot):
    await bot.add_cog(voice(bot))