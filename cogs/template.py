import os
import sys
import discord
from discord.ext import commands
from isDeveloper import isDeveloper



class Template(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    # @commands.command(name='createtemplate')
    # async def template():
        
        

    #     pass
    



async def setup(bot):
    await bot.add_cog(Template(bot))