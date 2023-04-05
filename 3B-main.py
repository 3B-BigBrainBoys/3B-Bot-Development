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
bot = discord.Bot(intents=intents)
tree = app_commands.CommandTree(bot)

# Bot startup
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Running on version: {discord.__version__}')
    # For each cog in the /cog directory, load the cog

async def setup_hook(self):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f"cogs.{filename[:-3]}")
    await bot.tree.sync(guild = discord.Object(id = 456))

bot.run(TOKEN)

