
import discord
from discord.ext import commands
from discord.utils import get
from discord import app_commands


class voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="join")    
    async def join(self, interaction: discord.Interaction):
        guild = interaction.guild
        if guild.voice_client != None:
            await guild.voice_client.move_to(interaction.user.voice.channel)
        else:
            channel = interaction.user.voice.channel
            await channel.connect()
        await interaction.response.send_message(f'Joining channel: {channel}', delete_after=3.0)

    @app_commands.command(name='isoccupied')
    async def isoccupied(self, interaction: discord.Interaction):
        if interaction.guild.voice_client != None:
            await interaction.response.send_message("Bot is in a channel")
        else:
            await interaction.response.send_message("Bot is not connected to a channel")

    @app_commands.command(name='leave')
    async def leave(self, interaction: discord.Interaction):
        guild = interaction.guild
        if guild.voice_client != None:
            await guild.voice_client.disconnect()
            await interaction.response.send_message('Goodbye!', delete_after=1.0)
        else:
            await interaction.response.send_message("Bot is not in a channel...")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        vc = member.guild.voice_client
        if not vc:
            return
        
        if len(vc.channel.members) == 1:
            await vc.disconnect()




async def setup(bot):
    await bot.add_cog(voice(bot))