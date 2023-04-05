# Cog for misc commands

import discord
from discord.ext import commands
from discord import app_commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='echo')
    async def echo(self, ctx, *msg):
        msg = ' '.join(msg)
        await ctx.send(msg)

    @app_commands.command(name='whoami')
    async def whoami(self, ctx):
        await ctx.send(f"You are: {ctx.author}")

async def setup(bot):
    await bot.add_cog(Misc(bot))
    