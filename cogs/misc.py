# Cog for misc commands

import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, *msg):
        msg = ' '.join(msg)
        await ctx.send(msg)

    @commands.command(name='whoami')
    async def whoami(self, ctx):
        await ctx.send(f"You are: {ctx.author}")

async def setup(bot):
    await bot.add_cog(Misc(bot))
    