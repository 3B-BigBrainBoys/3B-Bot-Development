# Cog for misc commands

import discord
from discord.ext import commands
from discord import app_commands

###### NOT WORKING YET ######

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='echo')
    @app_commands.describe(msg = 'User message to echo')
    async def echo(self, interaction: discord.Interaction, msg: str):
        msg = ' '.join(msg)
        await interaction.response.send_message(msg)

    # @app_commands.command()
    # async def whoami(self, ctx):
    #     await ctx.send(f"You are: {ctx.author}")

async def setup(bot):
    await bot.add_cog(Misc(bot))
    