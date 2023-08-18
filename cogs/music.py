import discord
from discord.ext import commands, tasks
import wavelink
import datetime
from discord import app_commands

def ms_to_hms(milliseconds):
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)


class Player(wavelink.Player):
    
    def __init__(self):
        super().__init__()
        self.queue = wavelink.Queue()


class Music(commands.Cog):
    """Music cog to hold Wavelink related commands and listeners."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.connect_nodes.start()
        self.node: wavelink.Node = None
        self.player = None
        self.channel = None
    

    # async def queued_track(self, interaction, track, vc, duration):
    #     await interaction.response.send_message(embed=discord.Embed(
    #             title=track.title,
    #             url=track.uri,
    #             description = f"Queued {track.title} in {vc.channel}. \nDuration: {duration}"
    #         ))


    @tasks.loop(count=1)
    async def connect_nodes(self):
        """Connect to our Lavalink nodes."""
        await self.bot.wait_until_ready()
        """
        Wavelink 2.0 has made connecting Nodes easier... Simply create each Node
        and pass it to NodePool.connect with the client/bot.
        """
        self.node: wavelink.Node = wavelink.Node(
            uri='localhost:2033', 
            password='youtube3B'
            )
        await wavelink.NodePool.connect(client=self.bot, nodes=[self.node])
        self.node = wavelink.NodePool.get_node()


    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        """Event fired when a node has finished connecting."""
        print(f'Node: <{node.id}> is ready!')

    async def connect_to_channel(self, interaction: discord.Interaction, channel: discord.VoiceChannel | None = None):
        try:
            self.channel = channel or interaction.user.voice.channel
        except:
            return await interaction.response.send_message('No voice channel to connect to. Please join a voice channel or name one then execute the command again.')
        
        self.player = Player()
        vc: Player = await self.channel.connect(cls=self.player)

        return vc
    
    async def create_track(self, searchterm):
        yttrack = wavelink.YouTubeTrack
        return await yttrack.convert(wavelink.YouTubeTrack, searchterm)

    @app_commands.command(name='connect')
    async def connect(self, interaction: discord.Interaction, channel: discord.VoiceChannel | None = None):
        await self.connect_to_channel(interaction, channel)
        await interaction.response.send_message(f'Joined voice channel: {self.channel}', delete_after=3.0)

    @app_commands.command(name='disconnect')
    async def disconnect(self, interaction: discord.Interaction):
        guild = interaction.guild
        if guild.voice_client != None:
            await guild.voice_client.disconnect()
            await interaction.response.send_message('Goodbye!', delete_after=3.0)
        else:
            await interaction.response.send_message("Bot is not in a channel...", delete_after=3.0)
    
    @app_commands.command(name='play')
    async def play(self, interaction: discord.Interaction, track: str):
            if self.channel is None:
                await self.connect_to_channel(interaction)
            song = await self.create_track(track)
            await self.player.play(song)
            await interaction.response.send_message('Success')
    
    @app_commands.command(name='skip')
    async def skip(self, interaction: discord.Interaction):
        guild = interaction.guild
        vc: Player = guild.voice_client
        await interaction.response.send_message('Playing next song')
        await vc.stop()

    @app_commands.command(name='pause')
    async def pause(self, interaction: discord.Interaction):  
        guild = interaction.guild
        vc: Player = guild.voice_client
        if vc:
            if not vc.is_paused():
                await vc.pause()

    # Function listens for the bot's voice status to update
    # If the state is a channel disconnect, it sets the bots active channel to None
    @commands.Cog.listener(name='Reset self.channel')
    async def on_voice_state_update(self, member: discord.member, before, after):
        if member.id == 1077964909318508564:
            vc = member.guild.voice_client
            if vc is None:
                self.channel = None
    


    # @commands.Cog.listener()
    # async def on_wavelink_track_end(self, payload):

    #     if not self.player.queue.is_empty:
    #         next_track = self.player.queue.get()
    #         await self.player.play(next_track)


    # @app_commands.command(name='play')
    # async def play(self, interaction: discord.Interaction, track: str = None):
    #     if track != None:
    #         YTtrack = wavelink.YouTubeTrack
    #         search = await YTtrack.convert(wavelink.YouTubeTrack, track)
        
    #     guild = interaction.guild
    #     vc = guild.voice_client
    #     track_duration = ms_to_hms(search.duration)
        
    #     if not guild.voice_client:
    #         self.player=BotPlayer()
    #         vc: BotPlayer = await interaction.user.voice.channel.connect(cls=self.player)

    #     if vc.is_paused():
    #         if track == None:
    #             await vc.resume()
    #         else:
    #             vc.queue.put(item=search)
    #             await vc.resume()

    #     elif vc.is_playing():

    #         vc.queue.put(item=search)
    #         self.queued_track(interaction, search, vc, track_duration)
            
    #         # await interaction.response.send_message(embed=discord.Embed(
    #         #     title=search.title,
    #         #     url=search.uri,
    #         #     description = f"Queued {search.title} in {vc.channel}. \nDuration: {track_duration}"
    #         # ))

    #     else:
    #         await vc.play(search)
    #         await interaction.response.send_message(embed=discord.Embed(
    #             title=search.title,
    #             url=search.uri,
    #             description = f"Now playing {search.title} in {vc.channel}. \nDuration: {track_duration}"
    #         ))



    


async def setup(bot):
    await bot.add_cog(Music(bot))
