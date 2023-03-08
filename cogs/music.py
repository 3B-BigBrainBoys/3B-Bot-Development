import discord
from discord.ext import commands
import wavelink

class Music(commands.Cog):
    """Music cog to hold Wavelink related commands and listeners."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

        bot.loop.create_task(self.connect_nodes())

    async def connect_nodes(self):
        """Connect to our Lavalink nodes."""
        await self.bot.wait_until_ready()

        await wavelink.NodePool.create_node(bot=self.bot,
                                            host='LavaLink-ALB-603820264.us-east-2.elb.amazonaws.com',
                                            port=2033,
                                            password='youtube3B')

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        """Event fired when a node has finished connecting."""
        print(f'Node: <{node.identifier}> is ready!')

    @commands.command()
    async def play(self, ctx: commands.Context, *, search: wavelink.YouTubeTrack = None):
        """Play a song with the given search query.
        If not connected, connect to our voice channel.
        """
        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client
        if vc.is_playing():
            await vc.resume()
        else:
            try:
                await ctx.send(f'Now playing: '+search.info['uri'])
                await vc.play(search)
            except TypeError:
                await ctx.send("Something went wrong: Try a different song or try again")

    @commands.command()
    async def pause(self, ctx: commands.Context):
        vc: wavelink.Player = ctx.voice_client
        if vc.is_paused():
            pass
        else:
            await vc.pause()

async def setup(bot):
    await bot.add_cog(Music(bot))