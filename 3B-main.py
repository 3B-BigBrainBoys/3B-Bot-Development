# Main file for bot
# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)


# Testing version #
# These
# are
# my
# line
# Testing merge conflict
