import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('ODU4NjIyNjQ3NDk5MjI3MTU2.YNg0pw.h-RgNQk2uu519ZpTcxIiIb9vUiA')

