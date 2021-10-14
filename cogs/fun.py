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
from discord.ext.commands import clean_content
import asyncio
import unicodedata
import functools
import aiohttp
import qrcode

async def get(session: object, url: object) -> object:
    async with session.get(url) as response:
        return await response.text()

class fun(commands.Cog):
    def __init__(self,client):
        self.client = client
        self.session = aiohttp.ClientSession()

    @commands.command(aliases=['8ball', 'test'])
    async def _8ball(self,ctx, *, question):
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
            f'```Question: {question}\nAnswer: {random.choice(responses)}```', allowed_mentions=discord.AllowedMentions(everyone=False,roles=False,users=False))
    
    @commands.guild_only()
    @commands.command()
    #@commands.has_guild_permissions(administrator=True)
    async def say(self,ctx, *, message=None):
        message = message or "Please say something to use the say command!"
        message_components = message.split()
        await ctx.send(message,allowed_mentions=discord.AllowedMentions(everyone=False,roles=False,users=False))

        
    @commands.command(aliases=['profilepic','pfp',"av"])
    async def avatar(self,ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(color=0x40cc88, timestamp=ctx.message.created_at)
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command()
    async def gayrate(self,ctx):
        await ctx.send(f"{ctx.author.mention} is {random.randint(0,100)}% gay")


    @commands.guild_only()
    @commands.command(aliases=['lesbianrate', 'lrate'])
    async def lesrate(self,ctx):
        await ctx.send(f"{ctx.author.mention} is {random.randint(0,100)}% lesbian")

    @commands.guild_only()
    @commands.command(pass_context = True,aliases = ["cb"])
    async def catbug(self,ctx):
        bug = [
        'https://tenor.com/view/catbug-bravest-warriors-love-cute-heart-gif-3457120',
        'https://tenor.com/view/loveyou-catbug-bravest-warriors-gif-11992208',
        'https://tenor.com/view/yippie-yay-catbug-bravest-warriors-gif-11992784',
        'https://tenor.com/view/bravest-warriors-catbug-salute-im-catbug-gif-11992601',
        'https://tenor.com/view/catbug-catbug-eating-catbug-eating-cereal-catbug-eating-food-eating-food-gif-21947681',
        'https://tenor.com/view/how-dareyou-catbug-bravest-warriors-gif-11992274',
        'https://tenor.com/view/sips-tea-drinking-catbug-bravest-warriors-gif-11992251',
        'https://tenor.com/view/sad-upset-catbug-bravest-warriors-gif-11992279',
        'https://tenor.com/view/sherrif-catbug-bravest-warriors-gif-11992284',
        'https://tenor.com/view/heart-eye-catbug-in-love-mermerized-fascinated-gif-12855794',
        'https://tenor.com/view/catbug-gif-10835276',
        'https://tenor.com/view/catbug-happy-excited-amazed-smile-gif-5294129',
        'https://tenor.com/view/catbug-catbug-hug-catbug-cuddle-catbug-hugging-catbug-cuddling-gif-21242363',
        'https://tenor.com/view/catbug-cute-cutie-cutie-catbug-catbug-drawing-gif-21232872',
        'https://tenor.com/view/peanutbuttersquare-cooldown-catbug-bravestwarriors-gif-5301902',
        'https://tenor.com/view/everything-is-okay-cat-bug-gif-4852806',
        'https://tenor.com/view/bugcat-capoo-drop-cute-sugar-peas-drop-them-gif-16639572',
        'https://tenor.com/view/catbug-rebecca-love-always-gif-5294058',
        'https://tenor.com/view/cat-bug-bravest-warriors-why-would-you-do-that-why-gif-4040974',
        'https://tenor.com/view/catbug-bravest-warriors-gif-11992204',
        'https://tenor.com/view/catbug-bravest-warriors-gif-11992204',
        'https://tenor.com/view/catbug-screaming-catbug-love-catbug-electrocuted-gif-7315184',
        'https://tenor.com/view/catbug-rebecca-bravestwarriors-who-gif-5294057',
        'https://tenor.com/view/catbug-rebecca-shout-twig-gif-9580597',
        'https://tenor.com/view/catbug-poke-bravest-warriors-gif-19299751',
        'https://tenor.com/view/bravest-warriors-cat-bug-king-cat-bug-reading-read-gif-11992602',
        'https://tenor.com/view/catbug-cute-cat-bug-adorable-gif-3420753',
        'https://tenor.com/view/rebecca-catbug-marry-cartoon-cartoonhangover-gif-5272230',
        'https://tenor.com/view/catbut-gif-10835268',
        'https://tenor.com/view/detective-searcking-looking-catbug-bravest-warriors-gif-11992268',
        'https://tenor.com/view/gurglies-catbug-bravest-warriors-gif-11992750',
        'https://tenor.com/view/clap-clapping-love-it-catbug-cute-gif-3420764',
        'https://tenor.com/view/clap-clapping-love-it-catbug-cute-gif-3420764',
        'https://tenor.com/view/bravest-warriors-cat-bug-laughing-lol-lmao-gif-7963694',
        'https://tenor.com/view/hugs-catbug-bravest-warriors-gif-11992432'
        ]
        await ctx.send(random.choice(bug))

    @commands.command()
    async def combine(self, ctx, name1: clean_content, name2: clean_content):
        name1letters = name1[:round(len(name1) / 2)]
        name2letters = name2[round(len(name2) / 2):]
        ship = "".join([name1letters, name2letters])
        emb = (discord.Embed(color=0x36393e, description = f"{ship}"))
        emb.set_author(name=f"{name1} + {name2}")
        await ctx.send(embed=emb)

    @commands.command()
    async def rcombine(self, ctx, name1: clean_content, name2: clean_content):
        name1letters = name1[round(len(name1) / 2):]
        name2letters = name2[:round(len(name2) / 2)]
        ship = "".join([name2letters, name1letters])
        emb = (discord.Embed(color=0x36393e, description = f"{ship}"))
        emb.set_author(name=f"{name1} + {name2}")
        await ctx.send(embed=emb)


    @commands.command(pass_context=True, aliases=['bigemoji','big'])
    async def bigemote(self, ctx, emoji):
        """Make a certain emote bigger"""
        try:
            if emoji[0] == '<':
                name = emoji.split(':')[1]
                emoji_name = emoji.split(':')[2][:-1]
                anim = emoji.split(':')[0]
                if anim == '<a':
                    url = f'https://cdn.discordapp.com/emojis/{emoji_name}.gif'
                else:
                    url = f'https://cdn.discordapp.com/emojis/{emoji_name}.png'
                try:
                    await ctx.send(url)
                except Exception as e:
                    print(e)
                    async with self.session.get(url) as resp:
                        if resp.status != 200:
                            await ctx.send('```Error: Emote not found.```')
                            return
                        img = await resp.read()

                    kwargs = {'parent_width': 1024, 'parent_height': 1024}
                    convert = False
                    task = functools.partial(bigEmote.generate, img, convert, **kwargs)
                    task = self.client.loop.run_in_executor(None, task)
                    try:
                        img = await asyncio.wait_for(task, timeout=15)
                    except asyncio.TimeoutError:
                        await ctx.send("```Error: Timed Out. Try again in a few seconds")
                        return
                    await ctx.send(file=discord.File(img, filename=name + '.png'))
            
        except Exception as e:
            await ctx.send(f"```Error, couldn't send emote.```")
    
    @staticmethod
    def generate(img, convert, **kwargs):
        img = io.BytesIO(img)
        return img

    @commands.command(name="emojiinfo", aliases=["ei"])
    async def emoji_info(self, ctx, emoji: discord.Emoji = None):
        if not emoji:
            return await ctx.invoke(self.bot.get_command("help"), entity="emojiinfo")

        try:
            emoji = await emoji.guild.fetch_emoji(emoji.id)
        except discord.NotFound:
            return await ctx.send("I could not find this emoji in the given guild.")

        is_managed = "Yes" if emoji.managed else "No"
        is_animated = "Yes" if emoji.animated else "No"
        requires_colons = "Yes" if emoji.require_colons else "No"
        creation_time = emoji.created_at.strftime("%I:%M %p %B %d, %Y")
        can_use_emoji = (
            "Everyone"
            if not emoji.roles
            else " ".join(role.name for role in emoji.roles)
        )

        description = f"""
        **General:**
        **- Name:** {emoji.name}
        **- Id:** {emoji.id}
        **- URL:** [Link To Emoji]({emoji.url})
        **- Author:** {emoji.user.mention}
        **- Time Created:** {creation_time}
        **- Usable by:** {can_use_emoji}
        
        **Other:**
        **- Animated:** {is_animated}
        **- Managed:** {is_managed}
        **- Requires Colons:** {requires_colons}
        **- Guild Name:** {emoji.guild.name}
        **- Guild Id:** {emoji.guild.id}
        """

        embed = discord.Embed(
            title=f"**Emoji Information for:** `{emoji.name}`",
            description=description,
            colour=0xADD8E6,
        )
        embed.set_thumbnail(url=emoji.url)
        await ctx.send(embed=embed)


    @commands.guild_only()
    @commands.command(pass_context=True)
    async def hug(self,ctx, member: discord.Member):
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
    @commands.command(pass_content=True)
    async def pat(self,ctx, member: discord.Member):
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
    @commands.command(pass_content=True)
    async def kiss(self,ctx, member: discord.Member):
        embed6 = discord.Embed(title="kiss",
                            description="**{1}** kisses **{0}**!".format(
                                member.name, ctx.message.author.name),
                            color=0xf7196a)
        embed6.set_image(
            url="https://media.giphy.com/media/X9j3XWxhLr1TWHJS7C/giphy.gif")
        await ctx.send(embed=embed6)


    @commands.guild_only()
    @commands.command()
    async def qr(self,ctx, *, message):
        img = qrcode.make(message)
        img.save("./qrcode.png")
        qrcodefile = discord.File("./qrcode.png")
        filename = "qrcode"
        await ctx.send(message,allowed_mentions=discord.AllowedMentions(everyone=False,roles=False,users=False))
        await ctx.send(file=qrcodefile)


    @commands.guild_only()
    @commands.command(pass_context = True)
    async def kill(self,ctx, member: discord.Member):
        kill_messages = [
            f'{ctx.message.author.mention} killed {member.mention} with a baseball bat!', 
            f'{ctx.message.author.mention} killed {member.mention} with a frying pan!',
            f'{ctx.message.author.mention} tried to kill {member.mention} by burning his hands off, but {member.mention} pulled a tricky-trick and burnt {ctx.author.mention}\'s hands off instead ;)',
            f'{ctx.message.author.mention} attempted to murder {member.mention} but .. NAH!'
        ] 
        await ctx.send(random.choice(kill_messages))
        await ctx.message.delete()

    @commands.guild_only()
    @commands.command()
    async def water(self,ctx):
        await ctx.send('Water is yummy :D I order everyone to drink water RIGHT NOW! xD')

    @commands.guild_only()
    @commands.command(aliases = ["dc"])
    async def deadchat(self,ctx):
        await ctx.send('https://tenor.com/view/rip-chat-chat-dead-dead-chat-inactive-gif-18754855')
        await ctx.message.delete()


    @commands.guild_only()
    @commands.command()
    async def simp(self,ctx):
        await ctx.send('SIMP!! WE FOUND AN SIMP LMAO xD')
        await ctx.message.delete()

    @commands.guild_only()
    @commands.command()
    async def drama(self,ctx):
        await ctx.send('*Grabs popcorn and pop* Nice Drama! I like watching drama! :D')
        await ctx.message.delete()

    @commands.guild_only()
    @commands.command(pass_context = True,aliases = ["cf"])
    async def coinflip(self,ctx):
        coin = [
            f'Head', 
            f'Tails',f'oops it fell']
            
    
        await ctx.send(random.choice(coin))

    @commands.guild_only()
    @commands.command()
    async def cool(self,ctx, member: discord.Member):
        await ctx.send(f'{member.mention} {ctx.author.mention} thinks your cool')
        await ctx.message.delete()  

    @commands.guild_only()
    @commands.command(pass_context = True,aliases = ["joke"])
    async def jokes(self,ctx):
        joke = [
            'What do dentists call their x-rays? Tooth pics!', 
            'Did you hear about the first restaurant to open on the moon? It had great food, but no atmosphere.',
            'What did one ocean say to the other ocean? Nothing, it just waved.',
            'Do you want to hear a construction joke? Sorry, I’m still working on it.',
            'Did you hear about the fire at the circus? It was in tents',
            'What does a nosey pepper do? It gets jalapeño business. ',
            'Why was the math teacher late to work? She took the rhombus.',
            "I'm really excited for the next autopsy club. It's open Mike night!",
            'Where do spiders seek health advice? WebMD.',
            'What did Yoda say when he saw himself in 4K? "HDMI."',
            "My daughter thinks I don't give her enough privacy. At least that's what she wrote in her diary.",
            'A friend of mine got into photographing salmon in different clothing. He said he liked shooting fish in apparel.',
            "Why can't you trust an atom? Because they make up everything.",
            "I'd like to go to Holland someday. Wooden shoe?",
            'The guy that invented the umbrella was gonna call it the brella. But he hesitated.']
            
    
        await ctx.send(random.choice(joke))

def setup(client):
    client.add_cog(fun(client))