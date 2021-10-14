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


class social(commands.Cog):
    def __init__(self,client):
        self.client = client

def setup(client):
    client.add_cog(social(client))