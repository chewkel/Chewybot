from aiohttp import ClientSession
import discord
import requests
from discord.ext import commands
import random
import os
import keep_alive
import asyncio
import json
import io
import contextlib
import datetime
import pytz
from datetime import datetime
import time

class help(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.guild_only()
    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(title="Help",
                            description="Get some help",
                            color=0x36393F)
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/attachments/502516810730700800/863404891665727538/help.png"
        )
        embed.add_field(name="catbug", value="Sends a gif of the wonderful catbug", inline=False)
        embed.add_field(name="ping", value="Returns pong!", inline=False)
        embed.add_field(name="8ball", value="Gives you a response.", inline=False)
        embed.add_field(name="say", value="Says something back.", inline=False)
        embed.add_field(name="avatar",
                        value="Gets your or someone else's pfp.",
                        inline=False)
        embed.add_field(name="lesrate",
                        value="Guesses how lesbian you are.",
                        inline=False)
        embed.add_field(name="gayrate",
                        value="Guesses how gay you are.",
                        inline=False)
        embed.add_field(name="calculate",
                        value="Does maths for you.",
                        inline=False)
        embed.add_field(
            name="snipe",
            value=
            "Snipes the most recently deleted message.",
            inline=False)
        embed.add_field(name="userinfo",
                        value="Shows information about your discord user.",
                        inline=False)
        embed.add_field(name="serverinfo",
                        value="Shows some information about the discord server.",
                        inline=False)
        embed.add_field(name="hug",
                        value="Hug yourself or another user.",
                        inline=False)
        embed.add_field(name="pat",
                        value="Pat yourself or another user.",
                        inline=False)
        embed.add_field(name="kiss",
                        value="Kiss yourself or another user.",
                        inline=False)
        embed.add_field(name="invite",
                        value="Invites chewybug into your server pls. :(",
                        inline=False)
        embed.add_field(name="gif",
                        value="Sends a gif of what you are searching for. SFW btw",
                        inline=False)
        embed.add_field(name="meme",
                        value="Sends a meme from r/memes top.",
                        inline=False)
        embed.set_footer(text="Made by Geeky™#9900 || Do !!help2 for more commands")
        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command()
    async def help2(self,ctx):
        embed = discord.Embed(title="Help",
                            description="Get some help",
                            color=0x36393F)
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/attachments/502516810730700800/863404891665727538/help.png"
        )
        embed.add_field(name="qr",
                        value="Makes a qrcode of any message you send.",
                        inline=False)
        embed.add_field(name="kill", value="Fun kill commannd", inline=False)
        embed.add_field(name="water", value="Mmmm water", inline=False)
        embed.add_field(name="dead", value="Chat do be dead", inline=False)
        embed.add_field(name="members", value="Shows the total membercount of the server", inline=False)
        embed.add_field(name="simp", value="Simp spotted", inline=False)
        embed.add_field(name="drama", value="We do a little trolling and drama", inline=False)
        embed.add_field(name="coinflip", value="Flip a coin", inline=False)
        embed.add_field(name="cool", value="You think that person is cool", inline=False)
        embed.add_field(name="jokes", value="Random lame jokes", inline=False)
        embed.add_field(name="prefix", value="Shows the bot's prefix", inline=False)
        embed.add_field(name="musichelp", value="Lists out all the music commands available.", inline=False)
        embed.add_field(name="tictactoe or ttt",value="ping yourself and someone to play tic tac toe.",
    inline=False)
        embed.add_field(name="place",value="When playing tic tac toe when it is your turn, do !!place (number) between 1-9 to choose your tile.",
    inline=False)
        embed.set_footer(text="Made by Geeky™#9900")
        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command()
    async def musichelp(self,ctx):
        embed = discord.Embed(title="Help",
                            description="Get some help",
                            color=0x36393F)
        embed.add_field(name="Under Construction",value = "Currently remaking a library that won't bonk the bot :(")
    #     embed.add_field(name="join",value="Joins the Current voice channel you are in.",
    # inline=False)
    #     embed.add_field(name="leave",value="Leaves the Current voice channel you are in.",
    # inline=False)
    #     embed.add_field(name="nowplay",value="Shows the current song playing",
    # inline=False)
    #     embed.add_field(name="play",value="Shows your playlist.",
    # inline=True)
    #     embed.add_field(name="queue",value="Shows your playlist.",
    # inline=True)
    #     embed.add_field(name="skip",value="Shows your playlist.",
    # inline=True)
    #     embed.add_field(name="remove",value="Removes a song from your playlist. Must use numbers such as !!remove 1",
    # inline=False)
    #     embed.add_field(name="loop",value="Loops the current song.",
    # inline=False)
    #     embed.add_field(name="volume",value="Sets the volume of the current song.",
    # inline=False)
    #     embed.add_field(name="pause",value="Pauses the current song playing.",
    # inline=False)
    #     embed.add_field(name="resume",value="Resumes the current song playing.",
    # inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(help(client))