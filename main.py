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
from typing import Optional
import aiohttp
import time
import asyncio
import pytz
from discord.ext.commands import clean_content
import giphy_client
from giphy_client.rest import ApiException
import praw
import qrcode

guidl = guild_ids = [
    371390722751856640, 843089655976165387, 792426133157183490
]

client = commands.AutoShardedBot(commands.when_mentioned_or('!!'),
                                 help_command=None,
                                 intents=discord.Intents.all(),
                                 cape_insensitive=True)

slash = SlashCommand(client, sync_commands=True)

reddit = praw.Reddit(client_id="sEt_NsT9HvHUkqRfIpTa7A",
                     client_secret="ohIXFGRUItFUR0z0dA34SP-IuCWGfw",
                     username="chewkel",
                     password="mento3384@TATS",
                     user_agent="chewy")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You can't do that. :(")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing arguement")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Command does not exist sorry.")


@client.event
async def on_ready():
    print('Chewybug is online :D')

    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1

    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name=f'{servers} servers and {members} members | !!help'))


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


@commands.guild_only()
@client.command()
async def ping(ctx):
    await ctx.send(
        f'Ping! Pong! You got a latency of {round  (client.latency * 1000)} ms'
    )


@commands.guild_only()
@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = [
        'It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes most definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply hazy, try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        "Don't count on it.",
        'My reply is a no.',
        'My sources say no.',
        'Outlook not so good.',
        'Very doubtful.',
        'I will respond later when im less busy with your mom.',
        "sure, I literally couldn't care less.",
        'Yes, idiot.',
        'Can you not?',
        'Yes, No, Maybe... I dont know, could you repeat the question?',
        'No... I mean yes... Well... Ask again later.',
    ]
    await ctx.send(
        f'```Question: {question}\nAnswer: {random.choice(responses)}```')


@commands.guild_only()
@client.command()
async def say(ctx, *, content: str):
    await ctx.send(content)


@commands.guild_only()
@client.command(pass_context=True)
async def hmm(ctx):
    if ctx.message.author.id == 212160821990522881:
        await ctx.send("hmm")


@commands.guild_only()
@client.command(aliases=['av', 'avatar'])
async def getpfp(ctx, member: Member = None):
    if not member:
        member = ctx.author
    await ctx.send(member.avatar_url)


@commands.guild_only()
@client.command()
async def gayrate(ctx):
    await ctx.send(f"{ctx.author.mention} is {random.randint(0,100)}% gay")


@commands.guild_only()
@client.command(aliases=['lesbianrate', 'lrate'])
async def lesrate(ctx):
    await ctx.send(f"{ctx.author.mention} is {random.randint(0,100)}% lesbian")


@commands.guild_only()
@client.command(aliases=['calc'])
async def calculate(ctx, operation, *nums):
    if operation not in ['+', '-', '*', '/', '*', '%', '&']:
        await ctx.send('Please type a valid operation type.')
    var = f' {operation} '.join(nums)
    await ctx.send(f'{var} = {eval(var)}')


@commands.guild_only()
@client.command(name="eval", aliases=["exec"])
@commands.is_owner()
async def _eval(ctx, *, code):
    code = clean_code(code)

    local_variables = {
        "discord": discord,
        "commands": commands,
        "bot": client,
        "ctx": ctx,
        "channel": ctx.channel,
        "author": ctx.author,
        "guild": ctx.guild,
        "message": ctx.message
    }

    stdout = io.StringIO()

    try:
        with contextlib.redirect_stdout(stdout):
            exec(
                f"async def func():\n{textwrap.indent(code, '    ')}",
                local_variables,
            )

            obj = await local_variables["func"]()
            result = f"{stdout.getvalue()}\n-- {obj}\n"
    except Exception as e:
        result = "".join(format_exception(e, e, e.__traceback__))

    pager = Pag(
        timeout=100,
        entries=[result[i:i + 2000] for i in range(0, len(result), 2000)],
        length=1,
        prefix="```py\n",
        suffix="```")

    await pager.start(ctx)


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

#@slash.slash(name = 'Guess' , description = 'Guesses a number', guild_ids = guidl , options = options)
#async def guess(ctx : SlashContext , start = 0, stop = 10):
#  randomnumber = random.randint(start, stop)
#  await ctx.send(content = f"Your random number is {randomnumber}")


#@slash.slash(name="Ping",description = 'Shows bot latency', guild_ids=guidl)
#async def _ping(ctx):
#  await ctx.send(f'Ping! Pong! You got a latency of {round  (client.latency * 1000)} ms')
@commands.guild_only()
@client.command(pass_context=True)
async def boom(ctx):
    if ctx.message.author.id == 212160821990522881:
        await ctx.send(
            "Nuking server and deleting all channels and roles. ||This really does nothing||"
        )


@commands.guild_only()
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help",
                          description="Get some help",
                          color=0x34ffcc)
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
@client.command()
async def help2(ctx):
    embed = discord.Embed(title="Help",
                          description="Get some help",
                          color=0x34ffcc)
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
    embed.set_footer(text="Made by Geeky™#9900")
    await ctx.send(embed=embed)

#outdated snipe thing

#snipe_message_author = {}
#snipe_message_content = {}

#@commands.guild_only()
#@client.event
#async def on_message_delete(message):
#     snipe_message_author[message.channel.id] = message.author
#     snipe_message_content[message.channel.id] = message.content
#     await asyncio.sleep(60)
#     del snipe_message_author[message.channel.id]
#     del snipe_message_content[message.channel.id]

#@commands.guild_only()
#@client.command(name = 'snipe')
#async def snipe(ctx):
#    channel = ctx.channel
#    try:
#        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
#        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
#        await ctx.send(embed = em)
#    except:
#        await ctx.send(f"There are no recently deleted messages in #{channel.name}")


@commands.guild_only()
@client.command()
async def warn(ctx, member: discord.Member, *, reason):
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


@commands.guild_only()
@client.command(aliases=["si"])
async def serverinfo(ctx):
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
@client.command(name='userinfo')
async def userinfo(ctx, member: discord.Member):
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
                    value=f'` { member.joined_at }  `',
                    inline=True)
    embed.add_field(name='Discord joined',
                    value=f'` { member.created_at }  `',
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
@client.command()
async def invite(ctx):
    embed3 = discord.Embed(
        title="Invite",
        description=
        "[Click me to invite](https://discord.com/api/oauth2/authorize?client_id=857350808466227221&permissions=8&redirect_uri=https%3A%2F%2Flocalhost%3A3000%2Fauth%2Fredirect&scope=bot%20applications.commands)",
        colour=discord.Colour.blue())
    await ctx.send(embed=embed3)


@commands.guild_only()
@client.command(pass_context=True)
async def hug(ctx, member: discord.Member):
    """Hug someone."""
    embed4 = discord.Embed(title="Huggies!",
                           description="**{1}** hugs **{0}**!".format(
                               member.name, ctx.message.author.name),
                           color=0x176cd5)
    embed4.set_image(
        url="https://media.giphy.com/media/MuElm1oRGb3OPlY4Fx/giphy.gif"
    )
    await ctx.send(embed=embed4)
#https://media1.tenor.com/images/0be55a868e05bd369606f3684d95bf1e/tenor.gif?itemid=7939558

@commands.guild_only()
@client.command(pass_content=True)
async def pat(ctx, member: discord.Member):
    embed5 = discord.Embed(title="Pat! Pat!",
                           description="**{1}** pats **{0}**!".format(
                               member.name, ctx.message.author.name),
                           color=0x42f5b9)
    embed5.set_image(
        url="https://media.giphy.com/media/kiblLDUFurYI0/giphy.gif")
    await ctx.send(embed=embed5)
#https://media.giphy.com/media/5tmRHwTlHAA9WkVxTU/giphy.gif
#https://tenor.com/view/how-dareyou-catbug-bravest-warriors-gif-11992274
@commands.guild_only()
@client.command(pass_content=True)
async def kiss(ctx, member: discord.Member):
    embed6 = discord.Embed(title="kiss",
                           description="**{1}** kisses **{0}**!".format(
                               member.name, ctx.message.author.name),
                           color=0xf7196a)
    embed6.set_image(
        url="https://media.giphy.com/media/X9j3XWxhLr1TWHJS7C/giphy.gif")
    await ctx.send(embed=embed6)
    
#https://tenor.com/view/bravest-warriors-kiss-beth-tezuya-kill-me-smack-gif-11992603
#https://media.giphy.com/media/Hht7xfbCiVZ0Q/giphy.gif
#https://media.giphy.com/media/Hht7xfbCiVZ0Q/giphy.gif
#https://tenor.com/view/lesbian-lesbians-kiss-gif-13045015


@commands.guild_only()
@client.command()
async def gif(ctx, *, q="random"):

    api_key = "l5W6oXOiiBDmrKEvxkD2ScZTmlBoQy8B"
    api_instance = giphy_client.DefaultApi()

    try:

        api_response = api_instance.gifs_search_get(api_key,
                                                    q,
                                                    limit=5,
                                                    rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        emb = discord.Embed(title=q)
        emb.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')

        await ctx.channel.send(embed=emb)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)


@commands.guild_only()
@client.command()
async def meme(ctx):
    subreddit = reddit.subreddit("dankmemes")
    all_subs = []
    top = subreddit.top(limit=50)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title=name)
    em.set_image(url=url)
    await ctx.send(embed=em)


@commands.guild_only()
@client.command()
async def qr(ctx, *, message):
    img = qrcode.make(message)
    img.save("./qrcode.png")
    qrcodefile = discord.File("./qrcode.png")
    filename = "qrcode"
    await ctx.send(message)
    await ctx.send(file=qrcodefile)


client.sniped_messages = {}


@client.event
async def on_message_delete(message):
    client.sniped_messages[message.guild.id] = (message.content,
                                                message.author,
                                                message.channel.name,
                                                message.created_at)


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

@client.command(pass_context = True)
async def kill(ctx, member: discord.Member):
    kill_messages = [
        f'{ctx.message.author.mention} killed {member.mention} with a baseball bat!', 
        f'{ctx.message.author.mention} killed {member.mention} with a frying pan!',
        f'{ctx.message.author.mention} tried to kill {member.mention} by burning his hands off, but {member.mention} pulled a tricky-trick and burnt {ctx.author.mention}\'s hands off instead ;)',
        f'{ctx.message.author.mention} attempted to murder {member.mention} but .. NAH!'
    ] 
    await ctx.send(random.choice(kill_messages))
    await ctx.message.delete()

@client.command()
async def water(ctx):
 await ctx.send('Water is yummy :D I order everyone to drink water RIGHT NOW! xD')

@client.command(aliases = ["dc"])
async def deadchat(ctx):
 await ctx.send('https://tenor.com/view/rip-chat-chat-dead-dead-chat-inactive-gif-18754855')
 await ctx.message.delete()

@client.command()
async def members(ctx):
        embed = discord.Embed(title="", description="", color=0x00FFFF)
        embed.add_field(name="Member Count:", value=f"There are currently **{ctx.guild.member_count}** in **{ctx.guild.name}**!", inline=False)
        await ctx.send(embed=embed)

@client.command()
async def simp(ctx):
  await ctx.send('SIMP!! WE FOUND AN SIMP LMAO xD')
  await ctx.message.delete()

@client.command()
async def drama(ctx):
  await ctx.send('*Grabs popcorn and pop* Nice Drama! I like watching drama! :D')
  await ctx.message.delete()

@client.command(pass_context = True,aliases = ["cf"])
async def coinflip(ctx):
    coin = [
        f'Head', 
        f'Tails',f'oops it fell']
        
   
    await ctx.send(random.choice(coin))


@client.command()
async def cool(ctx, member: discord.Member):
  await ctx.send(f'{member.mention} {ctx.author.mention} thinks your cool')
  await ctx.message.delete()  


@client.command(pass_context = True,aliases = ["joke"])
async def jokes(ctx):
    joke = [
        f'What do dentists call their x-rays? Tooth pics!', 
        f'Did you hear about the first restaurant to open on the moon? It had great food, but no atmosphere.',
        f'What did one ocean say to the other ocean? Nothing, it just waved.',
        f'Do you want to hear a construction joke? Sorry, I’m still working on it.',
        f'Did you hear about the fire at the circus? It was in tents',
        f'What does a nosey pepper do? It gets jalapeño business. ',
        f'Why was the math teacher late to work? She took the rhombus.',
        f"I'm really excited for the next autopsy club. It's open Mike night!",
        f'Where do spiders seek health advice? WebMD.',
        f'What did Yoda say when he saw himself in 4K? "HDMI."',
        f"My daughter thinks I don't give her enough privacy. At least that's what she wrote in her diary.",
        f'A friend of mine got into photographing salmon in different clothing. He said he liked shooting fish in apparel.',
        f"Why can't you trust an atom? Because they make up everything.",
        f"I'd like to go to Holland someday. Wooden shoe?",
        f'The guy that invented the umbrella was gonna call it the brella. But he hesitated.']
        
   
    await ctx.send(random.choice(joke))

@client.command()
async def prefix(ctx):
  await ctx.send(f'{ctx.author.mention} the prefix is: !! or just ping me')

@client.command(pass_context = True,aliases = ["cb"])
async def catbug(ctx):
    bug = [
      f'https://tenor.com/view/catbug-bravest-warriors-love-cute-heart-gif-3457120',
      f'https://tenor.com/view/loveyou-catbug-bravest-warriors-gif-11992208',
      f'https://tenor.com/view/yippie-yay-catbug-bravest-warriors-gif-11992784',
      f'https://tenor.com/view/bravest-warriors-catbug-salute-im-catbug-gif-11992601',
      f'https://tenor.com/view/catbug-catbug-eating-catbug-eating-cereal-catbug-eating-food-eating-food-gif-21947681',
      f'https://tenor.com/view/how-dareyou-catbug-bravest-warriors-gif-11992274',
      f'https://tenor.com/view/sips-tea-drinking-catbug-bravest-warriors-gif-11992251',
      f'https://tenor.com/view/sad-upset-catbug-bravest-warriors-gif-11992279',
      f'https://tenor.com/view/sherrif-catbug-bravest-warriors-gif-11992284',
      f'https://tenor.com/view/heart-eye-catbug-in-love-mermerized-fascinated-gif-12855794',
      f'https://tenor.com/view/catbug-gif-10835276',
      f'https://tenor.com/view/catbug-happy-excited-amazed-smile-gif-5294129',
      f'https://tenor.com/view/catbug-catbug-hug-catbug-cuddle-catbug-hugging-catbug-cuddling-gif-21242363',
      f'https://tenor.com/view/catbug-cute-cutie-cutie-catbug-catbug-drawing-gif-21232872',
      f'https://tenor.com/view/peanutbuttersquare-cooldown-catbug-bravestwarriors-gif-5301902',
      f'https://tenor.com/view/everything-is-okay-cat-bug-gif-4852806',
      f'https://tenor.com/view/bugcat-capoo-drop-cute-sugar-peas-drop-them-gif-16639572',
      f'https://tenor.com/view/catbug-rebecca-love-always-gif-5294058',
      f'https://tenor.com/view/cat-bug-bravest-warriors-why-would-you-do-that-why-gif-4040974',
      f'https://tenor.com/view/catbug-bravest-warriors-gif-11992204',
      f'https://tenor.com/view/catbug-bravest-warriors-gif-11992204',
      f'https://tenor.com/view/catbug-screaming-catbug-love-catbug-electrocuted-gif-7315184',
      f'https://tenor.com/view/catbug-rebecca-bravestwarriors-who-gif-5294057',
      f'https://tenor.com/view/catbug-rebecca-shout-twig-gif-9580597',
      f'https://tenor.com/view/catbug-poke-bravest-warriors-gif-19299751',
      f'https://tenor.com/view/bravest-warriors-cat-bug-king-cat-bug-reading-read-gif-11992602',
      f'https://tenor.com/view/catbug-cute-cat-bug-adorable-gif-3420753',
      f'https://tenor.com/view/rebecca-catbug-marry-cartoon-cartoonhangover-gif-5272230',
      f'https://tenor.com/view/catbut-gif-10835268',
      f'https://tenor.com/view/detective-searcking-looking-catbug-bravest-warriors-gif-11992268',
      f'https://tenor.com/view/gurglies-catbug-bravest-warriors-gif-11992750',
      f'https://tenor.com/view/clap-clapping-love-it-catbug-cute-gif-3420764',
      f'https://tenor.com/view/clap-clapping-love-it-catbug-cute-gif-3420764',
      f'https://tenor.com/view/bravest-warriors-cat-bug-laughing-lol-lmao-gif-7963694',
      f'https://tenor.com/view/hugs-catbug-bravest-warriors-gif-11992432'
    ]
    await ctx.send(random.choice(bug))

@commands.guild_only()
@client.command(alises = ["gcreaate"])
async def gstart(ctx, time=None,*,prize=None):
    yourID = 212160821990522881
    friendID = 719587928501649449
    if ctx.message.author.id == yourID or ctx.message.author.id == friendID:
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
        
keep_alive()
my_secret = os.environ['bot_token']
client.run(my_secret)

#Bot invite link below

#https://discord.com/api/oauth2/authorize?client_id=857350808466227221&permissions=8&redirect_uri=https%3A%2F%2Flocalhost%3A3000%2Fauth%2Fredirect&scope=bot%20applications.commands
