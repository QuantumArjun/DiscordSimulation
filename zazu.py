# Work with Python 3.6
import discord
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

TOKEN = open("token.txt", r).read();

client = discord.Client()

bot =commands.Bot(command_prefix="zazu ")
@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on "+ bot.user.name)
    print ("with the ID: " + bot.user.id)
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("AAAAAAAAAAAAAAAAAAAAA IM ON FIRE SOMEONE PUT ME OUT")
bot.run(TOKEN)
