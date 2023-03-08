# Cog for moderation commands

import os
import discord
from discord.ext import commands
from isDeveloper import isDeveloper


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    # DMs command author with guild member list
    async def memberlist(self, ctx, user:discord.Member=None):
        filename = str(ctx.guild)+'.txt'
        if user == None:
            user = ctx.author
        with open(filename, 'w') as file:
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
        await user.send(file=discord.File('./'+filename))
        if os.path.exists('./'+filename):
            os.remove('./'+filename)
        else:
            await user.send("File not found")

    @commands.command(name='Ban')
    async def Ban(self,ctx,member: discord.member,reason = None):
        if isDeveloper(ctx.author.id):
            await member.ban(reason = reason)
            await ctx.send(f"{member.name} has been banned from this server due to: {reason}")
        else:
            await ctx.send(f"YOU SHALL NOT PASS {ctx.author}")
            



async def setup(bot):
    await bot.add_cog(Moderation(bot))