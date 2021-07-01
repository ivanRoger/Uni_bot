import discord
from discord.ext import commands
import json

with open('setting.json', mode='r', encoding='utf8') as jfile:  # mode='r':開啟檔案時,以讀取模式(r)開啟。(mode可加可不加)
    jdata = json.load(jfile)
## 若是有一長串的資料或重要訊息，都可以儲存在json檔裡面直接讀取，可讓程式碼更簡潔


bot = commands.Bot(command_prefix= '[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")


@bot.command()
async def 圖片(ctx):
    pic = discord.File('D:\\Discord Bot\\Uni_bot\\pic\\Adventure-Time.jpg')  # 多增加一條反斜線用來轉譯
    await ctx.send(File= pic)




@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member} join!')         # channel.send:在這個頻道傳送文字

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'{member} leave!')


@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')   # bot.latency:機器人延遲時間
# bot.latency*1000:將時間換算成毫秒, round():四捨五入



bot.run(jdata['TOKEN'])  # 這樣就不必因為用bot.run("bot Token")而讓Token顯示出來

