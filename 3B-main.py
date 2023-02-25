# Main file for 3B
# bot.py
import os
import sys
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands.errors import BadArgument
import random

#param intents; 
intents = discord.Intents.all()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='$', intents=intents)

def isDeveloper(name):
    if str(name) in ["neuby#9514", "NiteLite#2686"]:
        return True
    return False

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def echo(ctx, *msg):
    msg = ' '.join(msg)
    await ctx.send(msg)

@bot.command(name='whoami')
async def whoami(ctx):
    await ctx.send(f"You are: {ctx.author}")

@bot.event
async def on_message(message):
    if '69' in message.content:
        await message.channel.send("Nice.")
    if 'Good morning Experimental Bot' in message.content:
        await message.channel.send("Good morning.")
    if 'rawr' in message.content:
        await message.channel.send("x3 *nuzzles*")
    await bot.process_commands(message)




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


def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.command(name= 'restart')
async def restart(ctx):
    if isDeveloper(ctx.author):
        await ctx.send("Restarting bot...")
        restart_bot()
    await ctx.send("You shall not pass!")
    await ctx.send(ctx.author)

@bot.command(name='shutdown')
async def stop(ctx):
    if isDeveloper(ctx.author):
        await ctx.send('Bot is now going offline...')
        await ctx.bot.close()
        quit()
    await ctx.send("You shall not pass!")
    await ctx.send(ctx.author)

bot.run(TOKEN)
