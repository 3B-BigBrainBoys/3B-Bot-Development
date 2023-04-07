# Cog for moderation commands

import os
import discord
from discord.ext import commands
from isDeveloper import isDeveloper
from datetime import timedelta
from random import randint
from getgif import get_gif
from discord import app_commands
import time

###### NOT WORKING YET ######

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @app_commands.command(name='memberlist',description='Sends a list of the current members')
    # DMs command author with guild member list
    async def memberlist(self, interaction: discord.Interaction, user:discord.Member=None):
        filename = str(interaction.guild)+'.txt'
        if user == None:
            user = interaction.user
        with open(filename, 'w') as file:
            file.write(f'Member list for {interaction.guild} server:\n')
            for member in interaction.guild.members:
                try:
                    file.write(f'{member}\n')
                except UnicodeEncodeError:
                    file.write(f'UnknownChar{str(member)[-5:]}\n')
                    """ 
                    Needed to add an error handling for this
                    This is just a temporary fix
                    Command throws an error when encoding/decoding unknown ASCII chars in
                    member discord tags
                    """
        file.close()
        await user.send(file=discord.File('./'+filename))
        if os.path.exists('./'+filename):
            os.remove('./'+filename)
        else:
            await user.send("File not found")

    # @app_commands.command(name='ban',)
    # async def ban(self,ctx, member: discord.Member,reason = None):
    #     if isDeveloper(ctx.author.id):
    #         await member.send(embed=discord.Embed(
    #             title="You have been banned",
    #             description=f"Reason: {reason}"
    #         ))
    #         await member.ban()
    #         await ctx.send(embed=discord.Embed(
    #             title=f"{member.name} has been banned",
    #             description=f"Reason: {reason}"))
    #     else:
    #         await ctx.send(f"YOU SHALL NOT PASS {ctx.author}")

    @app_commands.command(name='mute')
    async def mute(self,interaction: discord.Interaction, member: discord.Member = None,
                   reason: str = None,duration:float = None):
        if isDeveloper(interaction.user):   
            await discord.InteractionResponse.defer(
                member.timeout(timedelta(seconds=duration),reason=reason),
                ephemeral=False,thinking=True)
            await interaction.followup.send(embed = discord.Embed(
                title=f"{member.name} has been muted for",
                description=f"{duration} seconds\nReason: {reason}"
            ))
            await member.send(embed=discord.Embed(
                title="You have been temporily muted",
                description=f"Duration: {time}\nReason: {reason}" 
            ))


async def setup(bot):
    await bot.add_cog(Moderation(bot))
