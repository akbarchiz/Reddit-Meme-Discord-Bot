import discord
from discord.ext import commands
import asyncio
import config
import random
import aiohttp


bot = commands.Bot(command_prefix='/')


@bot.event
async def on_ready():
    print('success')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(' /rhelp'))


@bot.command()
async def meme(ctx):
    embed = discord.Embed(title="Post from r/memes.", description='', color=discord.Color.blue())
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)


@bot.command()
async def dice(ctx):
    url = 'https://www.pngall.com/wp-content/uploads/2016/04/Dice-Free-Download-PNG.png'
    embed = discord.Embed(color=discord.Color.blue())
    result = random.randrange(1, 7)
    embed.add_field(name=result, value='You got {}!'.format(result))
    embed.set_thumbnail(url=url)
    await ctx.send(embed=embed)


@bot.command()
async def rhelp(ctx):
    embed = discord.Embed(title='Command List', description='', color=discord.Color.blue())
    embed.add_field(name='Description', value="\n".join(['Get a meme from Reddit', 'Roll Dice']), inline=True)
    embed.add_field(name='Usage', value="\n".join(['/meme', '/dice']), inline=True)

    await ctx.send(embed=embed)


bot.run(config.data['DISCORD_TOKEN'])
