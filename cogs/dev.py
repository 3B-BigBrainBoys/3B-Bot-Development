# Cog for devloper commands

import os
import sys
import random
import discord
from discord.ext import commands
from getgif import get_gif

class Developer(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    def isDeveloper(self, name):
        if str(name) in ["neuby#9514", "NiteLite#2686"]:
            return True
        return False

    # Restart and shutdown functions for Developers
    def restart_bot(self): 
        os.execv(sys.executable, ['python'] + sys.argv)

    @commands.command(name='restart')
    async def restart(self, ctx):
        if self.isDeveloper(ctx.author):
            await ctx.send("Restarting bot...")
            self.restart_bot()
        await ctx.send(get_gif('you shall not pass', 25))
        await ctx.send("You shall not pass!")

    @commands.command(name='shutdown')
    async def stop(self, ctx):
        if self.isDeveloper(ctx.author):
            await ctx.send('Bot is now going offline...')
            await ctx.bot.close()
            quit()
        await ctx.send(get_gif('you shall not pass', 25))
        await ctx.send("You shall not pass!")

async def setup(bot):
    await bot.add_cog(Developer(bot))