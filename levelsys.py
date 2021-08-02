#import discord
#from discord.ext import commands
#from pymongo import MongoClient
#import dns

#bot_channel = 870014474864689245
#talk_channels = [301728934955843584,870014474864689245]
#        if ctx.channel.id == bot_channel:
#level = ["Active"]
#levelnum = [1]

#cluster = MongoClient("mongodb+srv://admin:300343@cluster0.hvo8s.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#levelling = cluster["discord"]["levelling"]

#class levelsys(commands.Cog):
#    def __init__(self,client):
#        self.client = client
#
#    @commands.Cog.listener()
#    async def on_ready(self):
#        print("working i think")
#
#    @commands.Cog.listener()
#    async def on_message(self,message):
#            stats = levelling.find_one({"id" : message.author.id})
#            if not message.author.id:
#                if stats is None:
#                    newuser = {"id" : message.author.id,"xp" : 100}
#                    levelling.insert_one(newuser)
#                else:
#                    xp = stats["xp"] + 5
#                    levelling.update_one({"id" : message.author.id},{"set":{"xp" : 100}})
#                    lvl = 0 
#                    while True:
#                        if xp < ((50*(lvl**2))+ (50*(lvl-1))):
#                            break
#                        lvl += 1
#                    xp -= ((50*((lvl-1)**2))+ (50*(lvl-1)))
#                    if xp == 0:
#                        await message.channel.send(f"well done {message.author.id}! You leveled up to **level** {level}!")
#                        for i in range(len(level)):
#                            await message.author.add_roles(discord.utils.get(message.author.guild.roles,name=level[i]))
 #                           embed = discord.Embed(description=f"{message.author.mention} you have gotten the role **{level[i]}")
  #                          embed.set_thumbnail(url=message.author.avatar_url)
   #                         await message.channel.send(embed=embed)

    #@commands.command()
    #async def rank(self,ctx):
     #       stats = levelling.find_one({"id": ctx.author.id})
      #      if stats is None:
       #         embed = discord.Embed(description="You haven't sent any messges so you don't have a rank.")
        #        await ctx.channel.send(embed=embed)
         #   else:
          #      xp = stats["xp"]
           #     lvl = 0
            #    rank = 0
             #   while True:
              #      if xp < ((50*(lvl**2))+ (50*(lvl-1))):
               #         break
                #    lvl += 1
                #xp -= ((50*((lvl-1)**2))+ (50*(lvl-1)))
                #boxes = int((xp/(200*(1/2)*lvl))*20)
                #rankings = levelling.find().sort("xp",-1)
                #print(lvl)
                #for x in rankings:
                 #   rank += 1
                  #  if stats["id"] == x["id"]:
                   #     break
                #embed = discord.Embed(title="{}'s level stats".format(ctx.author.name))
                #embed.add_field(name="Name",value=ctx.author.mention,inline=True)
                #embed.add_field(name="XP",value=f"{xp}/{int(200*((1/2)*lvl))}",inline=True)
                #embed.add_field(name="Rank",value=f"{rank}/{ctx.guild.member_Count}")
                #embed.add_field(name="Progress Bar [lvl]",value=boxes * ":blue_sqaure" + (20-boxes) * ":white_large_boxes",inline=False)
                #embed.set_thumbnail(url=ctx.author.avatar_url)
                #await ctx.channel.send(embed=embed)

    #@commands.command()
    #async def leaderboard(self,ctx):
     #       rankings = levelling.find().sort("xp",-1)
      #      i = 1
       #     embed = discord.Embed(title="Rankings:")
        #    for x in rankings:
         #       try:
          #          temp = ctx.guild.get_member(x["id"])
           #         tempxp = x["xp"]
            #        embed.add_field(name=f"{i}: {temp.name}", value=f"Total XP: {tempxp}", inline=False)
             #       i =+1
              #  except:
               #     pass
                #if i == 11:
                 #   break
            #await ctx.channel.send(embed=embed)

#def setup(client):
 #   client.add_cog(levelsys(client))