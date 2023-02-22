# Main file for bot
# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands.errors import BadArgument
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def dosomething(ctx):
    await ctx.send("I did something")

@bot.command(name='rolldice')
async def dice(ctx, sides=6, amount=1):
    if sides < 4:
        await ctx.send(
        '''Please enter 4 or more sides (default = 6).
Command syntax: $dice [sides] [dice]''')
    elif amount < 1:
        await ctx.send(
            '''Please enter 1 or more dice (default 1).'''
        )
    else:
        await ctx.send('Rolling a %s sided die %d time(s)...' % (sides, amount))
        s = ""
        for i in range(amount):
            newNum = (random.randrange(1, sides + 1))
            s += str(newNum) + " "
        await ctx.send(s)

@dice.error
async def dice_error(ctx, error):
    await ctx.send("Please use smaller numbers and keep entries as integers.")

@bot.command(name='shutdown')
@commands.is_owner()
async def stop(ctx):
    await ctx.send('Bot is now going offline...')
    await ctx.bot.logout()
    quit()

bot.run(TOKEN)


# Testing version #
# These
# are
# my
# line
# Testing merge conflict
