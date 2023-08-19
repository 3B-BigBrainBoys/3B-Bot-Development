# Cog for commands that are entertainment based
import discord
from discord.ext import commands
from getgif import get_gif
import random
from discord import app_commands

class Entertainment(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @app_commands.command(name='gif')
    async def gif(self, interaction: discord.Interaction, arg: str, limit: int=10):
        await interaction.response.send_message(get_gif(arg, limit))
        
async def setup(bot):
    await bot.add_cog(Entertainment(bot))