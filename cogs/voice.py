
import discord
from discord.ext import commands


class voice():
    def __init__(self,bot):
        self.bot = bot
    async def joinVC(self,ctx):
        channel = ctx.author.voice_channel
        await self.bot.join_voice_channel(channel)

async def setup(bot):
    await bot.add_cog(voice(bot))