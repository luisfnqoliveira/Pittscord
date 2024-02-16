import discord
from discord.ext import commands

# get token from parent directory
import sys
sys.path.append('..')
from secret import discord_token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(discord_token)
