# Main file for 3B
# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands

load_dotenv()
TOKEN = os.getenv('EXPERIMENTAL_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

# Bot startup
@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print(f'{bot.user} has connected to Discord!')
    print(f'Running on version: {discord.__version__}')
    print(f"Synced {synced}")
    [await bot.load_extension(f"cogs.{filename[:-3]}") for filename in os.listdir('./cogs') if filename.endswith('.py')]
    # For each cog in the /cog directory, load the cog

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello")

bot.run(TOKEN)

