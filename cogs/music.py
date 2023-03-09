import discord
from discord.ext import commands
import wavelink
import datetime

class BotPlayer(wavelink.Player):
    
    def __init__(self):
        super().__init__()
        self.queue = wavelink.Queue()

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

    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player, track: wavelink.Track, reason):

        if not player.queue.is_empty:

            next_track = player.queue.get()
            await player.play(next_track)

    @commands.command()
    async def play(self, ctx: commands.Context, *, search: wavelink.YouTubeTrack = None):
        vc = ctx.voice_client
        
        if not ctx.voice_client:
            botplayer = BotPlayer()
            vc: BotPlayer = await ctx.author.voice.channel.connect(cls=botplayer)

        if vc.is_paused():
            await vc.resume()

        elif vc.is_playing():

            vc.queue.put(item=search)
            track_duration = str(datetime.timedelta(seconds=search.duration))
            await ctx.send(embed=discord.Embed(
                title=search.title,
                url=search.uri,
                description = f"Queued {search.title} in {vc.channel}. \nDuration: {track_duration}"
            ))
        

        else:
            try:
                await vc.play(search)
                track_duration = str(datetime.timedelta(seconds=search.duration))
                await ctx.send(embed=discord.Embed(
                title=search.title,
                url=search.uri,
                description = f"Now playing {search.title} in {vc.channel}. \nDuration: {track_duration}"
                ))
            except TypeError:
                pass

    @commands.command()
    async def pause(self, ctx: commands.Context):  
        vc: BotPlayer = ctx.voice_client
        if vc:
            if not vc.is_paused():
                await vc.pause()

    @commands.command()
    async def skip(self, ctx: commands.Context):
        vc: BotPlayer = ctx.voice_client
        if vc:
            if vc.is_paused():
                return
            if vc.queue.is_empty:
                await vc.stop()
                return
            await vc.seek(vc.track.length * 1000)

    @commands.command()
    async def stop(self, ctx: commands.Context):
        vc: BotPlayer = ctx.voice_client
        await vc.stop()


async def setup(bot):
    await bot.add_cog(Music(bot))