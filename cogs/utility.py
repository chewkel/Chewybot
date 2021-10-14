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

class utility(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.guild_only()
    @commands.command()
    async def ping(self, ctx):
        msg = await ctx.send("`Pinging bot latency...`")
        times = []
        counter = 0
        embed = discord.Embed(title="More information:", description="Pinged 4 times and calculated the average.", colour=discord.Colour(value=0x36393e))
        for _ in range(3):
            counter += 1
            start = time.perf_counter()
            await msg.edit(content=f"Pinging... {counter}/3")
            end = time.perf_counter()
            speed = round((end - start) * 1000)
            times.append(speed)
            embed.add_field(name=f"Ping {counter}:", value=f"{speed}ms", inline=True)

        embed.set_author(name="Pong!")
        embed.add_field(name="Bot latency", value=f"{round(self.client.latency * 1000)}ms", inline=True)
        embed.add_field(name="Average speed", value=f"{round((round(sum(times)) + round(self.client.latency * 1000))/4)}ms")
        embed.set_footer(text=f"Estimated total time elapsed: {round(sum(times))}ms")
        await msg.edit(content=f":ping_pong: **{round((round(sum(times)) + round(self.client.latency * 1000))/4)}ms**", embed=embed)

    @commands.guild_only()
    @commands.command(aliases=["si"])
    async def serverinfo(self,ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(title=name + " Server Information",
                            description=description,
                            color=discord.Color.blue())
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)

        await ctx.send(embed=embed)
            
    @commands.guild_only()
    @commands.command(name='userinfo')
    async def userinfo(self,ctx,*, member: discord.Member = None):
        member = ctx.author if not member else member
        de = pytz.timezone('Europe/London')
        embed = discord.Embed(title=f' User info for {member} ',
                            description='',
                            color=0x4cd137,
                            timestamp=datetime.now().astimezone(tz=de))

        embed.add_field(name='Name',
                        value=f'` { member.name }#{ member.discriminator }  `',
                        inline=True)
        embed.add_field(name='Bot',
                        value=f'` { ( "Yes"  if  member.bot  else  "No" ) }  `',
                        inline=True)
        embed.add_field(
            name='Nickname',
            value=f'` { ( member.nick  if  member.nick  else  "Not set" ) }  `',
            inline=True)
        embed.add_field(name='Server joined',
                        value=f'` {member.joined_at.strftime("%d/%m/%Y")} {member.joined_at.strftime("%H:%M:%S")}  `',
                        inline=True)
        embed.add_field(name='Discord joined',
                        value=f'` {member.created_at.strftime("%m/%d/%Y")} {member.created_at.strftime("%H:%M:%S")}  `',
                        inline=True)
        embed.add_field(name='roles',
                        value=f'` { len ( member.roles ) }  `',
                        inline=True)
        embed.add_field(name='Highest Role',
                        value=f'` { member.top_role.name }  `',
                        inline=True)
        embed.add_field(name='color', value=f'` { member.color }  `', inline=True)
        embed.add_field(
            name='Booster',
            value=f'` { ( "Yes"  if  member.premium_since  else  "No" ) }  `',
            inline=True)
        embed.set_footer(
            text=f'Required from { ctx.author.name } • { ctx.author.id } ',
            icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command()
    async def invite(self,ctx):
        embed3 = discord.Embed(
            title="Invite",
            description=
            "[Click me to invite](https://discord.com/api/oauth2/authorize?client_id=857350808466227221&permissions=8&redirect_uri=https%3A%2F%2Flocalhost%3A3000%2Fauth%2Fredirect&scope=bot%20applications.commands)",
            colour=discord.Colour.blue())
        await ctx.send(embed=embed3)


    @commands.guild_only()
    @commands.command()
    async def members(self,ctx):
            embed = discord.Embed(title="", description="", color=0x00FFFF)
            embed.add_field(name="Member Count:", value=f"There are currently **{ctx.guild.member_count}** in **{ctx.guild.name}**!", inline=False)
            await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command()
    async def prefix(self,ctx):
        await ctx.send(f'{ctx.author.mention} the prefix is: !! or just ping me')


def setup(client):
    client.add_cog(utility(client))