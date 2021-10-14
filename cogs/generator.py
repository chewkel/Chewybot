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
from giphy_client.rest import ApiException
import praw
import asyncpraw
import giphy_client

class generator(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.command()
    async def cat(self, ctx):
      response = requests.get('https://aws.random.cat/meow')
      data = response.json()
      embed = discord.Embed(
          title = 'Kitty Cat 🐈',
          description = 'Cats :star_struck:',
          colour = discord.Colour.purple()
          )
      embed.set_image(url=data['file'])            
      embed.set_footer(text="")
      await ctx.send(embed=embed)


    @commands.guild_only()
    @commands.command()
    async def gif(self,ctx, *, q="random"):

        api_key = "l5W6oXOiiBDmrKEvxkD2ScZTmlBoQy8B"
        api_instance = giphy_client.DefaultApi()

        try:

            api_response = api_instance.gifs_search_get(api_key,
                                                        q,
                                                        limit=10,
                                                        rating='g')
            lst = list(api_response.data)
            giff = random.choice(lst)

            emb = discord.Embed(title=q)
            emb.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')

            await ctx.channel.send(embed=emb)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

def setup(client):
    client.add_cog(generator(client))