import os
import discord
from discord.ext import commands, tasks
import random
from discord import Member
from keep_alive import keep_alive
import contextlib
import io
import logging
import textwrap
from traceback import format_exception
from discord.ext import commands
# import json_loader
# from mongo import Document
# from utils import clean_code, Pag
from datetime import datetime
import datetime
from typing import Optional
import aiohttp
import time
import asyncio
import pytz
from discord.ext.commands import clean_content
# import giphy_client
# from giphy_client.rest import ApiException
# import praw
# import qrcode
from asyncio import TimeoutError
from random import choice
import asyncpraw
import sys
from io import BytesIO
from tkinter import font
import threading
from random import choice
from copy import deepcopy
from dataIO import fileIO
import asyncio
import pickle
import sys
from PIL import Image, ImageDraw, ImageFont
import pytz

config_location = fileIO("config/config.env", "load")
Shards = config_location["Shards"]
Prefix = config_location["Prefix"]

client = commands.AutoShardedBot(commands.when_mentioned_or(Prefix),
                                 help_command=None,
                                 intents=discord.Intents.all(),
                                 cape_insensitive=True)

client.load_extension('jishaku')
@client.event
async def on_ready():
    print('Chewybug is online :D')
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

# config_location = fileIO("config/config.json", "load")
c_id = os.environ['client_id']
c_secret = os.environ['client_secret']
rpass = os.environ['rpass']

reddit = asyncpraw.Reddit(client_id=c_id,
                     client_secret=c_secret,
                     username="chewkel",
                     password=rpass,
                     user_agent="chewy")


@commands.is_owner()
@client.command(aliases=["r"])
async def restart(ctx):
  embed=discord.Embed(title=":white_check_mark:",desc="Successfully Restarted")
  await ctx.send(embed=embed)
  os.system("clear")
  os.execv(sys.executable, ['python'] + sys.argv)
  await ctx.send("succesfully restarted")

@client.event
async def on_command(command):
	info = fileIO("config/config.json", "load")
	info["Commands_used"] = info["Commands_used"] + 1
	fileIO("config/config.json", "save", info)
    
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

# @slash.slash(name = 'Guess' , description = 'Guesses a number', guild_ids = guidl , options = options)
# async def guess(ctx : SlashContext , start = 0, stop = 10):
#  randomnumber = random.randint(start, stop)
#  await ctx.send(content = f"Your random number is {randomnumber}")


# @slash.slash(name="Ping",description = 'Shows bot latency', guild_ids=guidl)
# async def _ping(ctx):
#  await ctx.send(f'Ping! Pong! You got a latency of {round  (client.latency * 1000)} ms')

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

keep_alive()
my_secret = os.environ['bot_token']
client.run(my_secret)


#Bot invite link below

#https://discord.com/api/oauth2/authorize?client_id=857350808466227221&permissions=8&redirect_uri=https%3A%2F%2Flocalhost%3A3000%2Fauth%2Fredirect&scope=bot%20applications.commands
