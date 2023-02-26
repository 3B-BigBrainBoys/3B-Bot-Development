# Cog for moderation commands

import os
import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    # DMs command author with guild member list
    async def memberlist(self, ctx, user:discord.Member=None):
        if user == None:
            user = ctx.author
        with open('memberlist.txt', 'w') as file:
            file.write(f'Member list for {ctx.guild} server:\n')
            for member in ctx.guild.members:
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
        await user.send(file=discord.File('./memberlist.txt'))
        if os.path.exists('./memberlist.txt'):
            os.remove('./memberlist.txt')
        else:
            await user.send("File not found")


async def setup(bot):
    await bot.add_cog(Moderation(bot))