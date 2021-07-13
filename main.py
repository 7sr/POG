import discord
from discord.ext import commands
import random
import requests

PREFIX=","
TOKEN="YOUR TOKEN GOES HERE"

client = commands.Bot(command_prefix = PREFIX)  #edit on the 7th line
client.remove_command("help")


@client.event
async def on_ready():
    print("MEME BOT ONLINE !")
    await client.change_presence(activity=discord.Streaming(name="Watch My Streeam", url='https://www.youtube.com/watch?v=1iESjxnR_HY'))


@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "help", description = f"My Prefix is `{PREFIX}` | Commands For This Bot !.",color = ctx.author.color)

    em.add_field(name = "**Fun**", value = "`meme` | `howgay` | `pp`")
    em.set_footer(text="Made by sr#8067 .")

    await ctx.send(embed = em)



@client.command()
async def meme(ctx):
 response = requests.get("https://meme-api.herokuapp.com/gimme")
 fox = response.json()
 image = fox['url']
 title = fox['title']
 postlink = fox['postLink']
 reddit = fox['subreddit']
 embed=discord.Embed(title=title, url=postlink, color=0x00eeff)
 embed.set_author(name=reddit, icon_url="https://www.sharethis.com/wp-content/uploads/2017/05/Reddit.png")
 embed.set_image(url=image)
 await ctx.send(embed=embed)



@client.command(aliases=["gay"])
async def howgay(ctx, member: discord.Member = None):
        member = member or ctx.author
        response=[random.randint(0,100)]
        embed=discord.Embed(title='Gay Rating Device!',
        description=f"\n{member.mention} is {random.choice(response)}% gay!!  :rainbow_flag:",color  = 0xdb7bff)
        await ctx.send(embed=embed)





@client.command(aliases=["pp"])
async def howpp(ctx, member: discord.Member = None):
        member = member or ctx.author
        response=['8=======D','8==D', '8===D','8====D', '8====D', '8=========D','8D', '8=D']
        embed=discord.Embed(title='How long is the pp?',
        description=f"\n{member.mention} pp is {random.choice(response)}",color  = 0x206694)
        await ctx.send(embed=embed)



client.run(TOKEN)
