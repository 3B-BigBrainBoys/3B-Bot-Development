# Cog for commands that are entertainment based
import discord
from discord.ext import commands
from getgif import get_gif
import random
from discord import app_commands

###### NOT WORKING YET ######

class Entertainment(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @app_commands.command(name='gif')
    async def gif(self, interaction: discord.Interaction, arg: str, limit: int=50):
        await interaction.response.send_message(get_gif(arg, limit))

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

    # @commands.command(name='rolldice')
    # async def dice(self, ctx, sides=6, amount=1):
    #     if sides < 4:
    #         await ctx.send(
    #         '''Please enter 4 or more sides (default = 6).
    # Command syntax: $dice [sides] [dice]''')
    #     elif amount < 1:
    #         await ctx.send(
    #             '''Please enter 1 or more dice (default 1).'''
    #         )
    #     else:
    #         await ctx.send('Rolling a %s sided die %d time(s)...' % (sides, amount))
    #         s = ""
    #         for i in range(amount):
    #             newNum = (random.randrange(1, sides + 1))
    #             s += str(newNum) + " "
    #         await ctx.send(s)

    # @dice.error
    # async def dice_error(self, ctx, error):
    #     await ctx.send("Please use smaller numbers and keep entries as integers.")

    #Rock paper scissors game

    @app_commands.command(name='rps')
    async def rps(self, interaction: discord.Interaction):
        
        msg = await interaction.response.send_message(embed = discord.Embed(title='Rock, Paper, Scissors...'))
        reactions = ['🪨','📰','✂️']
        for emoji in reactions: 
            await msg.add_reaction(emoji)

        botmove = random.choice(reactions)

        def check(reaction, user):
            return user == interaction.user and str(reaction.emoji) in reactions
        reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

        # Tie
        if str(reaction.emoji) == botmove:
            return await msg.edit(embed = discord.Embed(title=f"Bot chose: {botmove}\nIt's a tie!"))
        
        # Bot wins:
        elif str(reaction.emoji) == '🪨' and botmove == '📰':
            return await msg.edit(embed = discord.Embed(title=f"Bot chose: {botmove}\nYou lose!"))
        elif str(reaction.emoji) == '📰' and botmove == '✂️':
            return  await msg.edit(embed = discord.Embed(title=f"Bot chose: {botmove}\nYou lose!"))
        elif str(reaction.emoji) == '✂️' and botmove == '🪨':
            return await msg.edit(embed = discord.Embed(title=f"Bot chose: {botmove}\nYou lose!"))
        
        # Player wins:
        elif str(reaction.emoji) == '📰' and botmove == '🪨':
            return await msg.edit(embed = discord.Embed(title=f"Bot chose: {botmove}\nYou win!"))
        elif str(reaction.emoji) == '✂️' and botmove == '📰':
            return  await msg.edit(embed = discord.Embed(title=f"Bot chose: {botmove}\nYou win!"))
        elif str(reaction.emoji) == '🪨' and botmove == '✂️':
            return await msg.edit(embed = discord.Embed(title=f"Bot chose: {botmove}\nYou win!"))
        
async def setup(bot):
    await bot.add_cog(Entertainment(bot))