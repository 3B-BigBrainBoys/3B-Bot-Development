# Cog for devloper commands

import os
import sys
import random
import discord
from discord.ext import commands
from getgif import get_gif
from isDeveloper import isDeveloper

###### NOT WORKING YET ######

class Developer(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    # # Restart and shutdown functions for Developers
    # def restart_bot(self): 
    #     os.execv(sys.executable, ['python'] + sys.argv)

    # @commands.command(name='restart')
    # async def restart(self, ctx):
    #     if isDeveloper(ctx.author.id):
    #         await ctx.send("Restarting bot...")
    #         self.bot.close()
    #         self.restart_bot()
    #     await ctx.send(get_gif('you shall not pass', 25))
    #     await ctx.send("You shall not pass!")

    # @commands.command(name='shutdown')
    # async def stop(self, ctx):
    #     if isDeveloper(ctx.author.id):
    #         await ctx.send('Bot is now going offline...')
    #         await ctx.bot.close()
    #         quit()
    #     await ctx.send(get_gif('you shall not pass', 25))
    #     await ctx.send("You shall not pass!")

async def setup(bot):
    await bot.add_cog(Developer(bot))