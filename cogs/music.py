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


class Music(commands.Cog):
    """Music cog to hold Wavelink related commands and listeners."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.connect_nodes.start()
        self.node: wavelink.Node = None
        self.player = None
        self.channels = []

    @tasks.loop(count=1)
    async def connect_nodes(self):
        """Connect to our Lavalink nodes."""
        await self.bot.wait_until_ready()
        nodes = [wavelink.Node(uri='http://localhost:2333', password='youtube3B')]
        await wavelink.Pool.connect(nodes=nodes, client=self.bot, cache_capacity=100)


    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        """Event fired when a node has finished connecting."""
        print(f'Node: <{node.session_id}> is ready!')

    async def connect_to_channel(self, interaction: discord.Interaction, channel: discord.VoiceChannel | None = None):
        if interaction.guild.voice_client != None:
            return await self.player.move_to(channel)
        try:
            channel = channel or interaction.user.voice.channel
        except:
            return await interaction.response.send_message('No voice channel to connect to. Please join a voice channel or name one then execute the command again.')
        
        self.player = Player()
        vc: Player = await channel.connect(cls=self.player)

        return vc

    
    async def format_queue(self, queue, title):
        count = 1
        message = ''
        for song in queue:
            message += f'{count}). {song}\n'
            count += 1
        embed=discord.Embed(title=title, description = message)
        return embed


    @app_commands.command(name='connect')
    async def connect(self, interaction: discord.Interaction, channel: discord.VoiceChannel | None = None):
        await self.connect_to_channel(interaction, channel)
        await interaction.response.send_message(f'Joined voice channel: {channel}', delete_after=3.0)

    @app_commands.command(name='disconnect')
    async def disconnect(self, interaction: discord.Interaction):
        guild = interaction.guild
        if guild.voice_client != None:
            await guild.voice_client.disconnect()
            await interaction.response.send_message('Goodbye!', delete_after=3.0)
        else:
            await interaction.response.send_message("Bot is not in a channel...", delete_after=3.0)
    
    @app_commands.command(name='play')
    async def play(self, interaction: discord.Interaction, searchterm: str):
            if interaction.guild.voice_client is None:
                await self.connect_to_channel(interaction)
            
            tracks: wavelink.Search = await wavelink.Playable.search(searchterm)

            if not tracks:
                interaction.response.send_message("Track not found")
                return
            
            if self.player.playing:

                if isinstance(tracks, wavelink.Playlist):
                    added: int = await self.player.queue.put_wait(tracks)
                    await interaction.response.send_message(embed=discord.Embed(
                        title="Playlist Added",
                        url="",
                        description=f"Queued playlist '{tracks.name}' ({added} songs) to the queue"
                    ))

                else:
                    song = tracks[0]
                    await self.player.queue.put_wait(song)
                    await interaction.response.send_message(embed=discord.Embed(
                    title=song.title,
                    url=song.uri,
                    description = f"Queued {song.title} in {self.player.channel}. \nDuration: {ms_to_hms(song.length)}"
                    ))
                    
            else:

                if isinstance(tracks, wavelink.Playlist):
                    song = tracks[0]
                    added: int = await self.player.queue.put_wait(tracks[1:])
                    await self.player.play(song)
                    await interaction.response.send_message(embed=discord.Embed(
                    title=song.title,
                    url=song.uri,
                    description = f"Playlist tracks queued ({added} songs).\nNow playing {song.title} in {self.player.channel}.\nDuration: {ms_to_hms(song.length)}"
                    ))

                else:
                    song = tracks[0]
                    await self.player.play(song)
                    await interaction.response.send_message(embed=discord.Embed(
                    title=song.title,
                    url=song.uri,
                    description = f"Now playing {song.title} in {self.player.channel}. \nDuration: {ms_to_hms(song.length)}"
                ))

    @app_commands.command(name='queue')
    async def queue(self, interaction: discord.Interaction):
        if self.player.queue.is_empty:
            return await interaction.response.send_message('The player queue is empty', delete_after=3.0)
        embed: discord.Embed = await self.format_queue(self.player.queue, title='Current Queue')
        await interaction.response.send_message(embed=embed, delete_after=20.0)

    @app_commands.command(name='cqueue')
    async def cqueue(self, interaction: discord.Interaction):
        self.player.queue.reset()
        await interaction.response.send_message("Queue has been cleared")

    @app_commands.command(name='next')
    async def next(self, interaction: discord.Interaction):
        if not self.player.queue.is_empty:
            await interaction.response.send_message(f'Next song in queue: {str(self.player.queue.get())}', delete_after=5.0)
        else:
            await interaction.response.send_message('Current queue is empty')

    @app_commands.command(name='shuffle')
    async def shuffle(self, interaction: discord.Interaction):
        self.player.queue.shuffle()
        embed: discord.Embed = await self.format_queue(self.player.queue, title='Shuffled Queue')
        await interaction.response.send_message(embed=embed, delete_after=20.0)
    
    @app_commands.command(name='skip')
    async def skip(self, interaction: discord.Interaction):
        guild = interaction.guild
        vc: Player = guild.voice_client
        await interaction.response.send_message('Playing next song', delete_after=3.0)
        await vc.stop()

    @app_commands.command(name='pause')
    async def pause(self, interaction: discord.Interaction):  
        if self.player.playing:
            await self.player.pause(True)
            await interaction.response.send_message('Track has been paused', delete_after=3.0)

    @app_commands.command(name='resume')
    async def resume(self, interaction: discord.Interaction):
        if self.player.paused:
            await self.player.pause(False)
            await interaction.response.send_message('Resumed current track', delete_after=3.0)
        else:
            await interaction.response.send_message('Track is already playing', delete_after=3.0)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, b, a):
        vc = member.guild.voice_client
        if not vc:
            return
        
        if len(vc.channel.members) == 1:
            await vc.disconnect()

    # Function listens for the bot's voice status to update
    # If the state is a channel disconnect, it sets the bots active channel to None
    # @commands.Cog.listener(name='Reset self.channel')
    # async def on_voice_state_update(self, member: discord.member, before, after):
    #     if member.id == 1077964909318508564:
    #         vc = member.guild.voice_client
    #         if vc is None:
    #             self.player = None

async def setup(bot):
    await bot.add_cog(Music(bot))
