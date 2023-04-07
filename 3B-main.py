# Main file for 3B
# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from isDeveloper import isDeveloper

load_dotenv()
TOKEN = os.getenv('EXPERIMENTAL_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)
guild = discord.Object(id=1077425297651159120)

# Bot startup
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Running on version: {discord.__version__}')
    [await bot.load_extension(f"cogs.{filename[:-3]}") for filename in os.listdir('./cogs') if filename.endswith('.py')]
    bot.tree.copy_global_to(guild=guild)
    synced = await bot.tree.sync(guild=guild)
    print(f"Commands Synced: {[command.name for command in synced]}")
    # For each cog in the /cog directory, load the cog

@bot.tree.command(name='sync', description='Owner only')
async def sync(interaction: discord.Interaction):
    if isDeveloper == True:
        synced = await bot.tree.sync()
        print('Synced the following commands:')
        print(synced)
    else:
        await interaction.response.send_message('You must be the owner to use this command!')

bot.run(TOKEN)
