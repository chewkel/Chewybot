import os
import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext
import random
from discord import Member
from keep_alive import keep_alive
import contextlib
import io
import os
import logging
import textwrap
from traceback import format_exception
import discord
from pathlib import Path
import motor.motor_asyncio
from discord.ext import commands
import json_loader
from mongo import Document
from utils import clean_code, Pag
from datetime import datetime
import datetime
from typing import Optional
import aiohttp
import time
import asyncio
import pytz
from discord.ext.commands import clean_content
import giphy_client
from giphy_client.rest import ApiException
import praw
# import qrcode
#import levelsys
#import dns
from discord_components import *
#from discord_components import (
#    DiscordComponents,
#    Button,
#    ButtonStyle,
#    Select,
#    SelectOption,
#)
from asyncio import TimeoutError
from random import choice
import DiscordUtils
from traceback import format_exception
import asyncpraw
import traceback
from discordTogether import DiscordTogether
import discordTogether

client = commands.AutoShardedBot(commands.when_mentioned_or('!!'),
                                 help_command=None,
                                 intents=discord.Intents.all(),
                                 cape_insensitive=True)

client.load_extension('jishaku')
togetherControl = DiscordTogether(client)

@client.event
async def on_ready():
    print('Chewybug is online :D')
    DiscordComponents(client)
    await gen_memes() 
    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1

    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name=f'{servers} servers and {members} members | !!help'))

#cogs = [levelsys]

@commands.guild_only()
@commands.is_owner()
@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

@commands.guild_only()
@commands.is_owner()
@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

@commands.guild_only()
@commands.is_owner()
@client.command()
async def reload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

guidl = guild_ids = [
    371390722751856640, 843089655976165387, 792426133157183490
]

slash = SlashCommand(client, sync_commands=True)

c_id = os.environ['client_id']
c_secret = os.environ['client_secret']
rpass = os.environ['rpass']

reddit = asyncpraw.Reddit(client_id=c_id,
                     client_secret=c_secret,
                     username="chewkel",
                     password=rpass,
                     user_agent="chewy")

music = DiscordUtils.Music()

# @client.event
# async def on_command_error(ctx, error):
    # if isinstance(error, commands.MissingPermissions):
        # await ctx.send("You can't do that. :(")
    # elif isinstance(error, commands.MissingRequiredArgument):
        # await ctx.send("Missing arguement")
    # elif isinstance(error, commands.CommandNotFound):
        # await ctx.send("Command does not exist sorry.")

@client.event
async def on_disconnect():
    print('offline...')

#@client.event
#async def on_member_join(member):
#  print(f'{member}has joined the server.')
#  channel = client.get_channel(303484815917842444)
#  await channel.send(f'{member}has joined the server.')

#@commands.guild_only()
#@client.event
#async def on_member_remove(member):
#  print(f'{member}has left the server.')

#@commands.guild_only()
#@client.command(aliases=['calc'])
#async def calculate(ctx, operation, *nums):
#    if operation not in ['+', '-', '*', '/', '*', '%', '&']:
#        await ctx.send('Please type a valid operation type.')
#    var = f' {operation} '.join(nums)
#    await ctx.send(f'{var} = {eval(var)}')

options = [{
    "name": "start",
    "description": "The starting limit of the guess",
    "required": False,
    "type": 4
}, {
    "name": "stop",
    "description": "The stopping limit of the guess",
    "required": False,
    "type": 4
}]

@slash.slash(name = 'Guess' , description = 'Guesses a number', guild_ids = guidl , options = options)
async def guess(ctx : SlashContext , start = 0, stop = 10):
 randomnumber = random.randint(start, stop)
 await ctx.send(content = f"Your random number is {randomnumber}")


@slash.slash(name="Ping",description = 'Shows bot latency', guild_ids=guidl)
async def _ping(ctx):
 await ctx.send(f'Ping! Pong! You got a latency of {round  (client.latency * 1000)} ms')

all_subs = []


async def gen_memes():
    subreddit = await reddit.subreddit("memes")
    top = subreddit.top(limit = 200)
    async for submission in top:
      all_subs.append(submission)

@client.command(aliases=['memes'])
async def meme(ctx):
    random_sub = random.choice(all_subs)
    all_subs.remove(random_sub)
    name = random_sub.title
    url = random_sub.url
    ups = random_sub.score
    link = random_sub.permalink
    comments = random_sub.num_comments
    embed = discord.Embed(title=name,url=f"https://reddit.com{link}", color=ctx.author.color)
    embed.set_image(url=url)
    embed.set_footer(text = f"👍{ups} 💬{comments}")
    await ctx.send(embed=embed)
    
    if len(all_subs) <= 20:  # meme collection running out owo
        await gen_memes()

# @commands.guild_only()
# @client.command()
# async def meme(ctx):
#     subreddit = reddit.subreddit("dankmemes")
#     all_subs = []
#     top = subreddit.top(limit=10)
#     for submission in top:
#         all_subs.append(submission)
#     random_sub = random.choice(all_subs)
#     name = random_sub.title
#     url = random_sub.url
#     em = discord.Embed(title=name)
#     em.set_image(url=url)
#     await ctx.send(embed=em)

client.sniped_messages = {}


@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (message.content,
                                                message.author,
                                                message.channel.name,
                                                message.created_at)

@commands.guild_only()
@client.command()
async def snipe(ctx):
        try:
            contents, author, channel_name, time = client.sniped_messages[
                ctx.guild.id]

        except:
            await ctx.channel.send("Couldn't find a message to snipe!")
            return

        embed = discord.Embed(description=contents,
                              color=discord.Color.blue(),
                              timestamp=time)
        embed.set_author(name=f"{author.name}#{author.discriminator}",
                         icon_url=author.avatar_url)
        embed.set_footer(text=f"Deleted in : #{channel_name}")

        await ctx.channel.send(embed=embed)
        
@commands.guild_only()
@client.command(aliases = ["gcreate"])
async def gstart(ctx, time=None,*,prize=None):
    yourID = 212160821990522881
    friendID = 719587928501649449
    friendID2 = 573664306626035732
    if ctx.message.author.id == yourID or ctx.message.author.id == friendID or ctx.message.author.id == friendID2:
        if time == None:
            return await ctx.send("Please include a time.")
        if prize == None:
            return await ctx.send("Please include a prize.")
        embed = discord.Embed(title = "New Giveaway!", description=f'{ctx.author.mention} is giving away **{prize}**!!')
        time_convert = {"s":1,"m":60,"h":3600,"d":86400}
        gawtime = int(time[0]) * time_convert[time[-1]]
        embed.set_footer(text=f'Giveaway ends in {time}')
        gaw_msg = await ctx.send(embed=embed)

        await gaw_msg.add_reaction("🎉")
        await asyncio.sleep(gawtime)

        new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)

        users = await new_gaw_msg.reactions[0].users().flatten()
        users.pop(users.index(client.user))

        winner = random.choice(users)

        await ctx.send(f'YAYYY!! {winner.mention} has won the giveaway for **{prize}**!!')

#for i in range(len(cogs)):
#    cogs[i].setup(client)
buttons = [
    [
        Button(style=ButtonStyle.grey,label="1"),
        Button(style=ButtonStyle.grey,label="2"),
        Button(style=ButtonStyle.grey,label="3"),
        Button(style=ButtonStyle.blue,label="x"),
        Button(style=ButtonStyle.red,label="Exit")
    ],
    [
        Button(style=ButtonStyle.grey,label="4"),
        Button(style=ButtonStyle.grey,label="5"),
        Button(style=ButtonStyle.grey,label="6"),
        Button(style=ButtonStyle.blue,label="÷"),
        Button(style=ButtonStyle.red,label="←")
    ],
    [
        Button(style=ButtonStyle.grey,label="7"),
        Button(style=ButtonStyle.grey,label="8"),
        Button(style=ButtonStyle.grey,label="9"),
        Button(style=ButtonStyle.blue,label="+"),
        Button(style=ButtonStyle.red,label="Clear")
    ],
    [
        Button(style=ButtonStyle.grey,label="00"),
        Button(style=ButtonStyle.grey,label="0"),
        Button(style=ButtonStyle.grey,label="."),
        Button(style=ButtonStyle.blue,label="-"),
        Button(style=ButtonStyle.green,label="=")
    ],
]

def calculator(exp):
    o = exp.replace('x','*')
    o = o.replace('÷','/')
    result = ''
    try:
        result=str(eval(o))
    except:
        result = 'An error occurred'
    return result

@commands.guild_only()
@client.command()
async def calc(ctx):
    m = await ctx.send(content="Loading Calculator")
    expression="None"
    delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    e = discord.Embed(title=f'{ctx.author.name}\'s | {ctx.author.id}',description=expression,timestamp=delta)
    await m.edit(components=buttons,embed=e)
    while m.created_at < delta:
        res = await client.wait_for('button_click')
        if res.author.id == int(res.message.embed[0].title.split('|')[1]) and res.message.embeds[0].timestamp < delta:
            expression = res.message.embeds[0].description
            if expression == 'None' or expression == 'An error orccured':
                expression = ''
            if res.component.label == 'Exit':
                await res.respond(content='Calculator Closed',type=7)
                break
            elif res.component.label == '←':
                expression = expression[:-1]
            elif res.component.label == 'Clear':
                expression=None
            elif res.component.label == '=':
                expression = calculator(expression)
            else:
                expression += res.component.label
            f=discord.Embed(title=f'{res.author.name}\'s calculator|{res.author.id}', descripion = expression,timestamp = delta)
            await res.respond(content='',embed=f,component=buttons,type=7)

ch = ["Rock","Paper","Scissors"]

@commands.guild_only()
@client.command()
async def rps(ctx):
    comp = random.choice(ch)
    yet = discord.Embed(title=f"{ctx.author.display_name}'s Rock Paper Scissors Game!",description=" You haven't clicked on any button yet.")
    win = discord.Embed(title=f"{ctx.author.display_name}, You **won**!!",description=f"You have **Won!** The bot had chosen {comp}")
    out = discord.Embed(title=f"{ctx.author.display_name}, you didn't click in time",description="**Timed Out!**")
    lost = discord.Embed(title=f"{ctx.author.display_name}, You **Lost**!!",description=f"You have **Lost!** The bot had chosen {comp}")
    tie = discord.Embed(title=f"{ctx.author.display_name}, It was a **tie**!!",description=f"**TIE!** The bot had chosen {comp}")
 
    m = await ctx.send(
        embed=yet,
        components=[[Button(style=1, label="rock"),Button(style=3, label="paper"),Button(style=ButtonStyle.red, label="scissors")]
        ]
    )

    def check(res):
        return ctx.author == res.user and res.channel == ctx.channel

    try:
        res = await client.wait_for("button_click", check=check, timeout=15)
        player = res.component.label
        if player==comp:
          await m.edit(embed=tie,components=[])
        if player=="Rock" and comp=="Paper":
          await m.edit(embed=lost,components=[])
        if player!="Rock" and comp=="Scissors":
          await m.edit(embed=win,components=[])
        if player=="Paper" and comp=="Rock":
          await m.edit(embed=win,components=[])
        if player=="Paper" and comp=="Scissors":
          await m.edit(embed=lost,components=[])
        if player=="Scissors" and comp!="Rock":
          await m.edit(embed=lost,components=[])
        if player=="Scissors" and comp=="Paper":
          await m.edit(embed=win,components=[])

    except TimeoutError:
        await m.edit(
            embed=out,
            components=[],
        )           

@commands.guild_only()
@client.command()

async def bt(ctx):

    await ctx.send(

        "Hello, World!",

        components = [

            Button(label = "WOW button!")

        ]

    )



    interaction = await client.wait_for("button_click", check = lambda i: i.component.label.startswith("WOW"))

    await interaction.respond(content = "Button clicked!")

@client.command(name="eval")
@commands.is_owner()
async def eval_fn(ctx, *, code):
    language_specifiers = ["python", "py", "javascript", "js", "html", "css", "php", "md", "markdown", "go", "golang", "c", "c++", "cpp", "c#", "cs", "csharp", "java", "ruby", "rb", "coffee-script", "coffeescript", "coffee", "bash", "shell", "sh", "json", "http", "pascal", "perl", "rust", "sql", "swift", "vim", "xml", "yaml" , "txt"]
    loops = 0
    while code.startswith("`"):
        code = "".join(list(code)[1:])
        loops += 1
        if loops == 3:
            loops = 0
            break
    for language_specifier in language_specifiers:
        if code.startswith(language_specifier):
            code = code.lstrip(language_specifier)
    while code.endswith("`"):
        code = "".join(list(code)[0:-1])
        loops += 1
        if loops == 3:
            break
    code = "\n".join(f"    {i}" for i in code.splitlines()) 
    code = f"async def eval_expr():\n{code}" 
    def send(text): 
        client.loop.create_task(ctx.send(text))
    env = {
        "bot": client,
        "client": client,
        "ctx": ctx,
        "print": send,
        "_author": ctx.author,
        "_message": ctx.message,
        "_channel": ctx.channel,
        "_guild": ctx.guild,
        "_me": ctx.me
    }
    env.update(globals())
    try:
        exec(code, env)
        eval_expr = env["eval_expr"]
        result = await eval_expr()
        if result:
            await ctx.send(result)
    except:
        await ctx.send(f"```{traceback.format_exc()}```")

@client.command()
async def servers(self, ctx):
    activeservers = client.guilds
    for guild in activeservers:
        await ctx.send(guild.name)
        print(guild.name)

embedOne = discord.Embed(
    title = "Page #1", #Any title will do
    description = "This is page one!" #Any description will be fine
)
embedTwo = discord.Embed(
    title = "Page #2",
    description = "This is page two!"
)
embedThree = discord.Embed(
    title = "Page #3",
    description = "This is page three!"
)
#Get all embeds into a list
paginationList = [embedOne, embedTwo, embedThree] #Just append all embed names in here, in the right order ofcourse

#Main command
@client.command(
    name = "pagination",
    aliases = ["pages"]
)
async def pagination(ctx):
    #Sets a default embed
    current = 0
    #Sending first message
    #I used ctx.reply, you can use simply send as well
    mainMessage = await ctx.reply(
        "**Pagination!**",
        embed = paginationList[current],
        components = [ #Use any button style you wish to :)
            [
                Button(
                    label = "Prev",
                    id = "back",
                    style = ButtonStyle.red
                ),
                Button(
                    label = f"Page {int(paginationList.index(paginationList[current])) + 1}/{len(paginationList)}",
                    id = "cur",
                    style = ButtonStyle.grey,
                    disabled = True
                ),
                Button(
                    label = "Next",
                    id = "front",
                    style = ButtonStyle.red
                )
            ]
        ]
    )
    #Infinite loop
    while True:
        #Try and except blocks to catch timeout and break
        try:
            interaction = await client.wait_for(
                "button_click",
                check = lambda i: i.component.id in ["back", "front"], #You can add more
                timeout = 10.0 #10 seconds of inactivity
            )
            #Getting the right list index
            if interaction.component.id == "back":
                current -= 1
            elif interaction.component.id == "front":
                current += 1
            #If its out of index, go back to start / end
            if current == len(paginationList):
                current = 0
            elif current < 0:
                current = len(paginationList) - 1

            await interaction.respond(
                type = InteractionType.UpdateMessage,
                embed = paginationList[current],
                components = [ #Use any button style you wish to :)
                    [
                        Button(
                            label = "Prev",
                            id = "back",
                            style = ButtonStyle.red
                        ),
                        Button(
                            label = f"Page {int(paginationList.index(paginationList[current])) + 1}/{len(paginationList)}",
                            id = "cur",
                            style = ButtonStyle.grey,
                            disabled = True
                        ),
                        Button(
                            label = "Next",
                            id = "front",
                            style = ButtonStyle.red
                        )
                    ]
                ]
            )
        except asyncio.TimeoutError:
            #Disable and get outta here
            await mainMessage.edit(
                components = [
                    [
                        Button(
                            label = "Prev",
                            id = "back",
                            style = ButtonStyle.red,
                            disabled = True
                        ),
                        Button(
                            label = f"Page {int(paginationList.index(paginationList[current])) + 1}/{len(paginationList)}",
                            id = "cur",
                            style = ButtonStyle.grey,
                            disabled = True
                        ),
                        Button(
                            label = "Next",
                            id = "front",
                            style = ButtonStyle.red,
                            disabled = True
                        )
                    ]
                ]
            )
            break

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command(aliases=["ttt"])
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

@client.command()
async def join(ctx):
    await ctx.author.voice.channel.connect() #Joins author's voice channel
    
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    
@client.command()
async def play(ctx, *, url):
    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await player.queue(url, search=True)
        song = await player.play()
        await ctx.send(f"Playing {song.name}")
    else:
        song = await player.queue(url, search=True)
        await ctx.send(f"Queued {song.name}")
        
@client.command()
async def pause(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.pause()
    await ctx.send(f"Paused {song.name}")
    
@client.command()
async def resume(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()
    await ctx.send(f"Resumed {song.name}")
    
@client.command()
async def stop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await player.stop()
    await ctx.send("Stopped")
    
@client.command()
async def loop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
        await ctx.send(f"Enabled loop for {song.name}")
    else:
        await ctx.send(f"Disabled loop for {song.name}")
    
@client.command()
async def queue(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await ctx.send(f"{', '.join([song.name for song in player.current_queue()])}")
    
@client.command()
async def np(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    await ctx.send(song.name)
    
@client.command()
async def skip(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
        await ctx.send(f"Skipped from {data[0].name} to {data[1].name}")
    else:
        await ctx.send(f"Skipped {data[0].name}")

@client.command()
async def volume(ctx, vol):
    player = music.get_player(guild_id=ctx.guild.id)
    song, volume = await player.change_volume(float(vol) / 100) # volume should be a float between 0 to 1
    await ctx.send(f"Changed volume for {song.name} to {volume*100}%")
    
@client.command()
async def remove(ctx, index):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))
    await ctx.send(f"Removed {song.name} from queue")

@client.command(aliases=["yt"])
async def startyt(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command(aliases=["poker","pk"])
async def startpoker(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'poker')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command(aliases=["chess"])
async def startchess(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'chess')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command(aliases=["bet"])
async def startbt(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'betrayal')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command(aliases=["fish"])
async def startfish(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'fishing')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command(aliases=["lt"])
async def startlt(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'letter-tile')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command(aliases=["ws"])
async def startws(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'word-snack')
    await ctx.send(f"Click the blue link!\n{link}")

@client.command(aliases=["dcr"])
async def startdcr(ctx):
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'doodle-crew')
    await ctx.send(f"Click the blue link!\n{link}")


keep_alive()
my_secret = os.environ['bot_token']
client.run(my_secret)

#Bot invite link below

#https://discord.com/api/oauth2/authorize?client_id=857350808466227221&permissions=8&redirect_uri=https%3A%2F%2Flocalhost%3A3000%2Fauth%2Fredirect&scope=bot%20applications.commands
