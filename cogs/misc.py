# Cog for misc commands

import discord
from discord.ext import commands
from discord import app_commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='echo')
    @app_commands.describe(msg = 'User message to echo')
    async def echo(self, interaction: discord.Interaction, msg: str):
        msg = ' '.join(msg)
        await interaction.response.send_message(msg)

    @app_commands.command(name = 'whoami',description="Just in case you forgot your name")
    async def whoami(self, interaction:discord.Interaction):
        await interaction.response.send_message(f"You are: {interaction.user}")

async def setup(bot):
    await bot.add_cog(Misc(bot))
    