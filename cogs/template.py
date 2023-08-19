import os
import sys
import discord
from discord.ext import commands
from isDeveloper import isDeveloper

# PLACEHOLDER FOR FUTURE IDEA


class Template(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

async def setup(bot):
    await bot.add_cog(Template(bot))