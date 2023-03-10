# Cog for commands that are entertainment based
import discord
from discord.ext import commands
from getgif import get_gif
import random

class Entertainment(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(name='gif')
    async def gif(self, ctx, arg, limit=50):
        await ctx.send(get_gif(arg, limit))

    @commands.Cog.listener()
    async def on_message(self,message):
        if '69' in message.content and message.author.id !=1077964909318508564:
            await message.channel.send(get_gif('69 nice', 20))
            await message.channel.send("Nice.")
        if 'Good morning Experimental Bot' in message.content and message.author.id !=1077964909318508564:
            await message.channel.send("Good morning.")
        if 'rawr' in message.content and message.author.id !=1077964909318508564:
            await message.channel.send(get_gif('uwu anime', 20))
            await message.channel.send("x3 *nuzzles*")

    @commands.command(name='rolldice')
    async def dice(self, ctx, sides=6, amount=1):
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
    async def dice_error(self, ctx, error):
        await ctx.send("Please use smaller numbers and keep entries as integers.")

    #Garbage fake rock paper scissors game to test for chained input from a single user

    @commands.command(name='RPS')
    async def dice(self, ctx):
        await ctx.send('Rock, Paper, Scissors...')

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and \
            msg.content.lower() in ["rock", "paper", "scissors"]

        msg = await self.bot.wait_for("message", check=check)

        if msg.content.lower() == "rock":
            await ctx.send("Paper, you lose!")
        elif msg.content.lower() == "paper":
            await ctx.send("Scissors, you lose!")
        else :
            await ctx.send("Rock, you lose!")

async def setup(bot):
    await bot.add_cog(Entertainment(bot))