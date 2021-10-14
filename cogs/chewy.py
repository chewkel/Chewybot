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
from traceback import format_exception

class chewy(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.guild_only()
    @commands.command(pass_context=True)
    async def hmm(self,ctx):
        if ctx.message.author.id == 212160821990522881:
            await ctx.send("hmm")

    @commands.guild_only()
    @commands.command(pass_context=True)
    async def boom(self,ctx):
        if ctx.message.author.id == 212160821990522881:
            await ctx.send(
                "Nuking server and deleting all channels and roles. ||This really does nothing||"
            )

    @commands.guild_only()
    @commands.command()
    async def warn(self,ctx, member: discord.Member, *, reason):
        yourID = 212160821990522881
        friendID = 669690598508199936
        if ctx.message.author.id == yourID:  #"or ctx.message.author.id == friendID"
            embed = discord.Embed(color=discord.Colour.green())
            embed = discord.Embed(
                title=(f"Succesfully warned {member} for {reason}"))

            embed.set_image(
                url="https://media.giphy.com/media/BvkQAgMABTiLX3A190/giphy.gif")

            await ctx.send(embed=embed)
        else:
            await ctx.send("Bonk no funny warn command for you.")

def setup(client):
    client.add_cog(chewy(client))