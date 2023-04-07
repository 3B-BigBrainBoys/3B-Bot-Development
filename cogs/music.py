import discord
from discord.ext import commands, tasks
import wavelink
import datetime
from discord import app_commands

# ###### NOT WORKING YET ######

# class BotPlayer(wavelink.Player):
    
#     def __init__(self):
#         super().__init__()
#         self.queue = wavelink.Queue()

class Music(commands.Cog):

    pass
#     """Music cog to hold Wavelink related commands and listeners."""

#     def __init__(self, bot: commands.Bot):
#         self.bot = bot
#         self.connect_nodes.start()
#         self.node: wavelink.Node = None
#         self.player = None

#     @tasks.loop(count=1)
#     async def connect_nodes(self):
#         """Connect to our Lavalink nodes."""
#         await self.bot.wait_until_ready()
#         # Wavelink 2.0 has made connecting Nodes easier... Simply create each Node
#         # and pass it to NodePool.connect with the client/bot.
#         self.node: wavelink.Node = wavelink.Node(
#             uri='ec2-3-145-16-12.us-east-2.compute.amazonaws.com:2033', 
#             password='youtube3B'
#             )
#         await wavelink.NodePool.connect(client=self.bot, nodes=[self.node])
#         self.node = wavelink.NodePool.get_node()


#     @commands.Cog.listener()
#     async def on_wavelink_node_ready(self, node: wavelink.Node):
#         """Event fired when a node has finished connecting."""
#         print(f'Node: <{node.id}> is ready!')

#     @commands.Cog.listener()
#     async def on_wavelink_track_end(self, payload):

#         if not self.player.queue.is_empty:
#             next_track = self.player.queue.get()
#             await self.player.play(next_track)

#     @app_commands.command()
#     async def play(self, interaction: discord.Interaction, *, search: str = None):
#         search: wavelink.YouTubeTrack = search
#         guild = interaction.guild
#         vc = guild.voice_client
#         track_duration = str(datetime.timedelta(seconds=search.duration))
    @app_commands.command(name='play')
    async def play(self, interaction: discord.Interaction, track: str = None):
        YTtrack = wavelink.YouTubeTrack
        search = await YTtrack.convert(wavelink.YouTubeTrack, track)
        
        guild = interaction.guild
        vc = guild.voice_client
        track_duration = str(datetime.timedelta(seconds=search.duration))
        
#         if not guild.voice_client:
#             self.player=BotPlayer()
#             vc: BotPlayer = await interaction.user.voice.channel.connect(cls=self.player)

#         if vc.is_paused():
#             await vc.resume()

#         elif vc.is_playing():

#             vc.queue.put(item=search)
            
#             await interaction.response.send_message(embed=discord.Embed(
#                 title=search.title,
#                 url=search.uri,
#                 description = f"Queued {search.title} in {vc.channel}. \nDuration: {track_duration}"
#             ))

#         else:
#             await vc.play(search)
#             await interaction.response.send_message(embed=discord.Embed(
#                 title=search.title,
#                 url=search.uri,
#                 description = f"Now playing {search.title} in {vc.channel}. \nDuration: {track_duration}"
#             ))


#     @app_commands.command()
#     async def pause(self, interaction: discord.Interaction):  
#         guild = interaction.guild
#         vc: BotPlayer = guild.voice_client
#         if vc:
#             if not vc.is_paused():
#                 await vc.pause()

#     @app_commands.command()
#     async def skip(self, interaction: discord.Interaction):
#         guild = interaction.guild
#         vc: BotPlayer = guild.voice_client
#         await vc.stop()
    # @app_commands.command('pause')
    # async def pause(self, interaction: discord.Interaction):  
    #     guild = interaction.guild
    #     vc: BotPlayer = guild.voice_client
    #     if vc:
    #         if not vc.is_paused():
    #             await vc.pause()

    # @app_commands.command('skip')
    # async def skip(self, interaction: discord.Interaction):
    #     guild = interaction.guild
    #     vc: BotPlayer = guild.voice_client
    #     await vc.stop()


async def setup(bot):
    await bot.add_cog(Music(bot))
