import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event #說這個叫裝飾器
async def on_ready(): # on_ready comes from api
    print('Bot is online')

@bot.event
async def on_member_join(member):
    print(f'{member} join!') #根據不同人會有不同顯示
    channel = bot.get_channel(723496013838549104)
    await channel.send(f'{member} join! And it was shown in channel! Wrrryyyy') # 因為send是協程(coroutine) 所以必須是呼叫 #send意味送資訊

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!') #根據不同人會有不同
    channel = bot.get_channel(723496013838549104)
    await channel.send(f'{member} leave! Shiku Shiku') # 因為send是協程(coroutine) 所以必須是呼叫

bot.run('NzIzMTQ5NDA5NDQxMDIyMDM1.XuySJw.CDar6TF-Ql3a3laUeCYFHmF-c8o')