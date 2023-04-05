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
bot = commands.Bot(intents=intents, command_prefix='$')

# Bot startup
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Running on version: {discord.__version__}')
    [await bot.load_extension(f"cogs.{filename[:-3]}") for filename in os.listdir('./cogs') if filename.endswith('.py')]
    # For each cog in the /cog directory, load the cog



bot.run(TOKEN)

