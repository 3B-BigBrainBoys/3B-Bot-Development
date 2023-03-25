# Main file for 3B
# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.all()

load_dotenv()
TOKEN = os.getenv('EXPERIMENTAL_TOKEN')
bot = commands.Bot(command_prefix='$', intents=intents)

# Bot startup
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Running on version: {discord.__version__}')
    # For each cog in the /cog directory, load the cog
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(TOKEN)

