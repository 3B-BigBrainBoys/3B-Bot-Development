# Cog for commands that are entertainment based
import discord
from discord.ext import commands
from getgif import get_gif
import random
from discord import app_commands

###### NOT WORKING YET ######
# RPS AND DICE ROLL ARE BROKEN WITH SLASH COMMANDS

class Entertainment(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @app_commands.command(name='gif')
    async def gif(self, interaction: discord.Interaction, arg: str, limit: int=10):
        await interaction.response.send_message(get_gif(arg, limit))

    @commands.Cog.listener()
    async def on_message(self,message):
        if '69' in message.content and message.author.id !=1077964909318508564:
            await message.channel.send(get_gif('69 nice', 20))
            await message.channel.send("Nice.")

    # @app_commands.command(name='rolldice',description="Rolls a dice based on specified size and amount of dice")
    # async def dice(self, interaction: discord.Interaction, sides: int = 6, amount: int = 1):
    #     if sides < 4:
    #         await interaction.response.send_message(
    #         '''Please enter 4 or more sides (default = 6).
    # Command syntax: /rolldice [sides] [dice]''')
    #     elif amount < 1:
    #         await interaction.response.send_message(
    #             '''Please enter 1 or more dice (default 1).'''
    #         )
    #     else:
    #         await interaction.response.send_message('Rolling a %s sided die %d time(s)...' % (sides, amount))
    #         s = ""
    #         for i in range(amount):
    #             newNum = (random.randrange(1, sides + 1))
    #             s += str(newNum) + " "
    #         await interaction.response.send_message(s)

    # @dice.error
    # async def dice_error(self, interaction: discord.Interaction, error):
    #     await interaction.response.send_message("Please use smaller numbers and keep entries as integers.")

    # Rock paper scissors game

    # @commands.command(name='RPS')
    # async def rps(self, interaction: discord.Interaction):
        
    #     msg = await interaction.response.send_message(embed = discord.Embed(title='Rock, Paper, Scissors...'))
    #     reactions = ['🪨','📰','✂️']
    #     for emoji in reactions: 
    #         await msg.add_reaction(emoji)
    # @app_commands.command(name='rps')
    # async def rps(self, interaction: discord.Interaction):
        
    #     msg = await interaction.response.send_message(embed = discord.Embed(title='Rock, Paper, Scissors...'))
    #     reactions = ['🪨','📰','✂️']
    #     for emoji in reactions: 
    #         await msg.add_reaction(emoji)

    #     botmove = random.choice(reactions)

    # #     def check(reaction, user):
    # #         return user == interaction: discord.Interaction.author and str(reaction.emoji) in reactions
    # #     reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
    #     def check(reaction, user):
    #         return user == interaction.user and str(reaction.emoji) in reactions
    #     reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

    #     # Tie
    #     if str(reaction.emoji) == botmove:
    #         return await msg.edit(embed = discord.Embed(title=f"Bot chose: {botmove}\nIt's a tie!"))
        
    #     # Bot wins:
    #     elif str(reaction.emoji) == '🪨' and botmove == '📰':
    #         return await msg.edit(embed = discord.Embed(title=f"Bot chose: {botmove}\nYou lose!"))
    #     elif str(reaction.emoji) == '📰' and botmove == '✂️':
    #         return  await msg.edit(embed = discord.Embed(title=f"Bot chose: {botmove}\nYou lose!"))
    #     elif str(reaction.emoji) == '✂️' and botmove == '🪨':
    #         return await msg.edit(embed = discord.Embed(title=f"Bot chose: {botmove}\nYou lose!"))
        
    #     # Player wins:
    #     elif str(reaction.emoji) == '📰' and botmove == '🪨':
    #         return await msg.edit(embed = discord.Embed(title=f"Bot chose: {botmove}\nYou win!"))
    #     elif str(reaction.emoji) == '✂️' and botmove == '📰':
    #         return  await msg.edit(embed = discord.Embed(title=f"Bot chose: {botmove}\nYou win!"))
    #     elif str(reaction.emoji) == '🪨' and botmove == '✂️':
    #         return await msg.edit(embed = discord.Embed(title=f"Bot chose: {botmove}\nYou win!"))
        
async def setup(bot):
    await bot.add_cog(Entertainment(bot))