import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(859324186312704050)
    await channel.send(f'{member} join!')         # channel.send:在這個頻道傳送文字

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(859324216796905482)
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')   # bot.latency:機器人延遲時間
# bot.latency*1000:將時間換算成毫秒, round():四捨五入


bot.run('bot token')

