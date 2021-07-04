import discord
from discord.ext import commands
import json
import random

with open('setting.json', mode='r', encoding='utf8') as jfile:  # mode='r':開啟檔案時,以讀取模式(r)開啟。(mode可加可不加)
    jdata = json.load(jfile)
## 若是有一長串的資料或重要訊息，都可以儲存在json檔裡面直接讀取，可讓程式碼更簡潔


bot = commands.Bot(command_prefix= '[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")


# 選取檔案中的圖片
@bot.command()
async def 圖片(ctx):
    pic = discord.File(jdata['pic'])  # 路徑中多增加一條反斜線用來轉譯
    await ctx.send(file= pic)

# 隨機選取檔案中圖片
@bot.command()
async def 圖片1(ctx):
    random_pic = random.choice(jdata['pic1'])
    pic1 = discord.File(random_pic)
    await ctx.send(file = pic1)

# 隨機選取網路上圖片
@bot.command()
async def web(ctx):
    random_pic_web = random.choice(jdata['url_pic'])
    await ctx.send(random_pic_web)  # 只需要單純送出網址的字串就可以了
    


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



bot.run(jdata['TOKEN'])  # 從json讀取，就不會因為用bot.run("bot Token")而讓Token顯示出來



