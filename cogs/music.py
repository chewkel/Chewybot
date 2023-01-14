import discord
from discord.ext import commands
import wavelink

# from youtube_dl import YoutubeDL

class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #     self.bot.loop.create_task(self.node_connect())
    
    # async def node_connect(self):
    #     await self.client.wait_until_ready()
    #     await wavelink.NodePool.create_node(bot = self.client, host='lava.link',port = 80, password = 'dismusic')
        
    # @commands.Cog.listener()
    # async def on_wavelink_node_ready(self,node: wavelink.Node):
    #     print(f"Node {node.identifier} is ready!")

    
    # @commands.command()
    # async def play(self,ctx: commands.Context, *, search: wavelink.YouTubeTrack):
    #     if not ctx.voice_client:
    #         vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
    #     elif not getattr(ctx.author.voice, "channel", None):
    #         return await ctx.send("You be in a vc")
    #     else:
    #         vc: wavelink.Player = ctx.voice_client
    
    #     await vc.play(search)
    #     await ctx.send(f"Now playing {search.title}")
        
    # @commands.command()
    # async def pause(self,ctx: commands.Context):
    #     if not ctx.voice_client:
    #         return await ctx.send("You are not playing anything so I can't pause anything")
    #     elif not getattr(ctx.author.voice, "channel", None):
    #         return await ctx.send("You be in a vc")
    #     else:
    #         vc: wavelink.Player = ctx.voice_client

    #     await vc.pause()
    #     await ctx.send("Current song has been paused")
        
    # @commands.command()
    # async def resume(self,ctx: commands.Context):
    #     if not ctx.voice_client:
    #         return await ctx.send("You are not playing anything so I can't pause anything")
    #     elif not getattr(ctx.author.voice, "channel", None):
    #         return await ctx.send("You be in a vc")
    #     else:
    #         vc: wavelink.Player = ctx.voice_client

    #     await vc.resume()
    #     await ctx.send("Current song has been resumed")

    # @commands.command()
    # async def stop(self,ctx: commands.Context):
    #     if not ctx.voice_client:
    #         return await ctx.send("You are not playing anything so I can't pause anything")
    #     elif not getattr(ctx.author.voice, "channel", None):
    #         return await ctx.send("You be in a vc")
    #     else:
    #         vc: wavelink.Player = ctx.voice_client

    #     await vc.stop()
    #     await ctx.send("Stopped")
        
    # @commands.command()
    # async def disconnect(self,ctx: commands.Context):
    #     if not ctx.voice_client:
    #         return await ctx.send("You are not playing anything so I can't pause anything")
    #     elif not getattr(ctx.author.voice, "channel", None):
    #         return await ctx.send("You be in a vc")
    #     else:
    #         vc: wavelink.Player = ctx.voice_client

    #     await vc.disconnect()
    #     await ctx.send("I left the vc")
        
    #     #all the music related stuff
    #     self.is_playing = False

    #     # 2d array containing [song, channel]
    #     self.music_queue = []
    #     self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    #     self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    #     self.vc = ""

    #  #searching the item on youtube
    # def search_yt(self, item):
    #     with YoutubeDL(self.YDL_OPTIONS) as ydl:
    #         try: 
    #             info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
    #         except Exception: 
    #             return False

    #     return {'source': info['formats'][0]['url'], 'title': info['title']}

    # def play_next(self):
    #     if len(self.music_queue) > 0:
    #         self.is_playing = True

    #         #get the first url
    #         m_url = self.music_queue[0][0]['source']

    #         #remove the first element as you are currently playing it
    #         self.music_queue.pop(0)

    #         self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
    #     else:
    #         self.is_playing = False

    # # infinite loop checking 
    # async def play_music(self):
    #     if len(self.music_queue) > 0:
    #         self.is_playing = True

    #         m_url = self.music_queue[0][0]['source']
            
    #         #try to connect to voice channel if you are not already connected

    #         if self.vc == "" or not self.vc.is_connected() or self.vc == None:
    #             self.vc = await self.music_queue[0][1].connect()
    #         else:
    #             await self.vc.move_to(self.music_queue[0][1])
            
    #         print(self.music_queue)
    #         #remove the first element as you are currently playing it
    #         self.music_queue.pop(0)

    #         self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
    #     else:
    #         self.is_playing = False

    # @commands.command(name="play", help="Plays a selected song from youtube")
    # async def play(self, ctx, *args):
    #     query = " ".join(args)
        
    #     voice_channel = ctx.author.voice.channel
    #     if voice_channel is None:
    #         #you need to be connected so that the bot knows where to go
    #         await ctx.send("Connect to a voice channel!")
    #     else:
    #         song = self.search_yt(query)
    #         if type(song) == type(True):
    #             await ctx.send("Could not download the song. Incorrect format try another keyword. This could be due to playlist or a livestream format.")
    #         else:
    #             await ctx.send("Song added to the queue")
    #             self.music_queue.append([song, voice_channel])
                
    #             if self.is_playing == False:
    #                 await self.play_music()

    # @commands.command(name="queue", help="Displays the current songs in queue")
    # async def queue(self, ctx):
    #     retval = ""
    #     for i in range(0, len(self.music_queue)):
    #         retval += self.music_queue[i][0]['title'] + "\n"

    #     print(retval)
    #     if retval != "":
    #         await ctx.send(retval)
    #     else:
    #         await ctx.send("No music in queue")

    # @commands.command(name="skip", help="Skips the current song being played")
    # async def skip(self, ctx):
    #     if self.vc != "" and self.vc:
    #         self.vc.stop()
    #         #try to play next in the queue if it exists
    #         await self.play_music()
            
    # @commands.command()
    # async def leave(self,ctx):
    #     if (ctx.voice_client): # If the bot is in a voice channel 
    #         await ctx.guild.voice_client.disconnect() # Leave the channel
    #         await ctx.send('Bot left')
    #     else: # But if it isn't
    #         await ctx.send("I'm not in a voice channel, use the join command to make me join")
            
    # @commands.command()
    # async def join(self, ctx):
    #     channel = ctx.author.voice.channel
    #     await channel.connect()
    #     await ctx.channel.send('bot joined')

# @client.command()
# async def join(ctx):
#     await ctx.author.voice.channel.connect() #Joins author's voice channel
    
# @client.command()
# async def leave(ctx):
#     await ctx.voice_client.disconnect()
    

def setup(client):
    client.add_cog(music(client))