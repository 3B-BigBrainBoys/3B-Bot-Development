# Cog for devloper commands

import os
import sys
import random
import discord
from discord.ext import commands
from getgif import get_gif
from isDeveloper import isDeveloper
from discord import app_commands

class Developer(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @app_commands.command(name='shutdown')
    async def shutdown(self, interaction: discord.Interaction):
        print(interaction.user.id)
        if isDeveloper(interaction.user.id):
            await interaction.response.send_message('Bot is now going offline...')
            await self.bot.close()
            quit()
        await interaction.response.send_message(get_gif('you shall not pass', 25))
        await interaction.response.send_message("You shall not pass!")

async def setup(bot):
    await bot.add_cog(Developer(bot))