
import discord
from discord.ext import commands

async def joinVC(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)

