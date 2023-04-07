# Cog for moderation commands

import os
import discord
from discord.ext import commands
from isDeveloper import isDeveloper
from datetime import timedelta
from random import randint
from getgif import get_gif
from discord import app_commands

###### NOT WORKING YET ######

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    # @commands.command()
    # # DMs command author with guild member list
    # async def memberlist(self, ctx, user:discord.Member=None):
    #     filename = str(ctx.guild)+'.txt'
    #     if user == None:
    #         user = ctx.author
    #     with open(filename, 'w') as file:
    #         file.write(f'Member list for {ctx.guild} server:\n')
    #         for member in ctx.guild.members:
    #             try:
    #                 file.write(f'{member}\n')
    #             except UnicodeEncodeError:
    #                 file.write(f'UnknownChar{str(member)[-5:]}\n')
    #                 """ 
    #                 Needed to add an error handling for this
    #                 This is just a temporary fix
    #                 Command throws an error when encoding/decoding unknown ASCII chars in
    #                 member discord tags
    #                 """
    #     file.close()
    #     await user.send(file=discord.File('./'+filename))
    #     if os.path.exists('./'+filename):
    #         os.remove('./'+filename)
    #     else:
    #         await user.send("File not found")

    # @commands.command(name='ban')
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

    # @commands.command(name='mute')
    # async def mute(self,ctx, member: discord.Member,reason = None,tmptime = None):
    #     time = int(tmptime)
    #     if isDeveloper(ctx.author.id):
    #         await member.timeout(timedelta(seconds=time,hours=0,days= 0,minutes= 0,weeks=0,microseconds=0,milliseconds=0),reason=reason)
    #         await ctx.send(embed = discord.Embed(
    #             title=f"{member.name} has been muted for",
    #             description=f"{time} seconds\nReason: {reason}"
    #         ))
    #         await member.send(embed=discord.Embed(
    #             title="You have been temporily muted",
    #             description=f"Duration: {time}\nReason: {reason}"
                
    #         ))


async def setup(bot):
    await bot.add_cog(Moderation(bot))
