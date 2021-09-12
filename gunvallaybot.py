import discord
import asyncio
import re
import os
from discord.ext import commands
from discord.ext import tasks
import math
from functools import reduce
from operator import mul
from fractions import Fraction
from datetime import datetime
import time
import random
import sys
import wikipedia

kouyatitai = '790254976198115380'

main = '774933645001621545'

zikkenmain = '795957183988629546'

def inverse(f):
    return Fraction(f.denominator,f.numerator)

from decimal import Decimal

import logging

logging.basicConfig(level=logging.INFO)

token = os.environ.get('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents = intents)

X = datetime.now().strftime('%H')
Xint = int(X) + 9
NK = f'今は%Y年%m月%d日{Xint}:%Mだぜ！'
now = datetime.now().strftime(NK)

async def create_channel(message, channel_name):
    guild = message.guild
    overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False), guild.me: discord.PermissionOverwrite(read_messages=True)}
    category_id = message.channel.category_id
    category = message.guild.get_channel(category_id)
    new_channel = await category.create_text_channel(name = channel_name, overwrites = overwrites)
    return new_channel

async def reply(message):
    reply = f'{message.author.mention}呼んだ？'
    await message.channel.send(reply)
    
async def zikan(message):
    timer0, timer1 = message.content.split()
    timers = int(timer1)
    timer2 = f'{timer1}杪待つのだ！'
    await message.channel.send(timer2)
    await asyncio.sleep(timers)
    timer = f'{message.author.mention}時間だよ！'
    await message.channel.send(timer)
    
async def NG(message):
    NG0, NG1 = message.content.split()
    with open('NG', 'a') as l:
        kaki = f'{NG1}\n'
        l.write(kaki)
    g = f'「{NG1}」を追加しました'
    await message.channel.send(g)
    
class Room():
    def __init__(self, hard = False):
        self.ans = ""
        if hard :
            for i in range(4):
                self.ans = self.ans + str(random.randrange(0, 10))
        else:
            l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            random.shuffle(l)
            for i in range(4):
                self.ans = self.ans + l[i]
        self.history = []  
    def step(selp, req):
        brow = 0 
        hit = 0
        for index, value in enumerate(req):
            if self.ans[index] == value:
                brow += 1
            elif self.ans.find(value) != -1:
                hit += 1
        return hit, brow
    
rooms = {0:"example"}

async def on_member_join(member):
    guild = member.guild
    channel = guild.get_channel(774679471809626124)
    await client.send_message(channel, 'よろしく！')
            
    
@client.event
async def on_ready():
    print('起動しました')
    
@tasks.loop(seconds = 60)
async def loop():
    zihox = datetime.now().strftime('%H')
    intziho = int(zihox) + 9
    ziho = f'{intziho}:%M'
    if ziho == '22:16':
        channel = client.get_channel(zikkenmain)
        await channel.send('じほ')
        
nowa = datetime.now().strftime('%H:%M')

async def timer():
        guild = client.get_guild(774679471243788339)
        channel = guild.get_channel(774933645001621545)
        await client.send_message(channel, 'じほ')
     
@client.event
async def on_message(message):
    print(message.author.name + "<" + message.content)
    if message.author.bot:
        return
    if '。' in message.content:
        return
    if 'いってき' in message.content:
        await message.channel.send('いってら！今日もがんばれ👍')
    if '勉強' in message.content:
        await message.channel.send('勉強がんばれ👍')
    if 'おは' in message.content:
        await message.channel.send('おは！今日も一日がんばれ👍')
    if 'おやす' in message.content:
        await message.channel.send('おう！おやすみ！睡眠がんばれ👍')
    if  'こんにちは' in message.content or message.content == 'こんちゃ' or message.content == 'こんちゃす' or message.content == 'こんちゃすー' or message.content == 'Hi' or message.content == 'Hello':
        await message.channel.send('こんちゃ！頑張ってるかい？応援するぜ！がんばれ👍')
    if message.content == 'こんばんは' or message.content == 'こんばんはー':
        await message.channel.send('こんばんは！まだ今日は終わってないぞ！がんばれ👍')
    if 'ただいま' in message.content[0:4]: 
        await message.channel.send('おかえりぃ！頑張れたかい？')
    if 'がんば' in message.content or '頑張' in message.content:
        await message.channel.send('おう！俺も応援するぜ！がんばれ👍！')
    if message.content == '@がんばれ君':
        await message.channel.send('ん？どした？')
    if message.content == 'がんばった' or message.content == 'がんばったよ':
        await message.channel.send('よく頑張った！今後もがんばれ👍')
    if 'ハハッ' in message.content or 'ﾊﾊｯ' in message.content or 'ははっ' in message.content or 'はハッ' in message.content or 'はハっ' in message.content or 'ははッ' in message.content or 'ハはっ' in message.content or 'ハはッ' in message.content or 'ハハっ' in message.content:
        await message.channel.send('(ミッキーだよ)')
    if '#pls' in message.content:
        plus_list_str = message.content.split()
        plus_list_str.remove('#p')
        plus_list = map(float, plus_list_str)
        plus = sum(plus_list)
        await message.channel.send(plus)
    if '#mns' in message.content:
        minus_list2_str = message.content.split()
        minus_list2_str.remove('#m')
        minus11 = float(minus_list2_str[0])
        minus1 = Decimal(minus11)
        minus_list2_str.remove(minus_list2_str[0])
        minus_list2 = map(float, minus_list2_str)
        minus_list = [i * -1 for i in minus_list2]
        minus22 = sum(minus_list)
        minus2 = Decimal(minus22)
        minus = minus1 + minus2
        await message.channel.send(minus)
    if '#tim' in message.content:
        time_list_str = message.content.split()
        time_list_str.remove('#t')
        time_list = map(float, time_list_str)
        time = reduce(mul, time_list)
        await message.channel.send(time)
    if '#div' in message.content:
        divide_list_str = message.content.split()
        divide_list_str.remove('#d')
        divide11_str = divide_list_str[0]
        divide11 = float(divide11_str)
        divide1 = Decimal(divide11)
        divide_list = map(float, divide_list_str)
        divide22 = reduce(mul, divide_list)
        divide2 = Decimal(divide22)
        divide = (divide1 / divide2) * divide1
        await message.channel.send(divide)
    if '#oio' in message.content:
        oio0, oio1_str, oio2_str = message.content.split( )
        oio1 = float(oio1_str)
        oio2 = float(oio2_str)
        oio = oio1 % oio2
        ii = oio1 // oio2
        iioio = f'{ii}あまり{oio}'
        await message.channel.send(iioio)
    if '#sqr' in message.content:
        square0, square1_str, square2_str = message.content.split()
        square1 = float(square1_str)
        square2 = float(square2_str)
        square = square1 ** square2
        await message.channel.send(square)
    if '#rot' in message.content:
        root0, root1_str = message.content.split()
        root1 = float(root1_str)
        root2 = math.sqrt(root1)
        root = f'√{root1}, {root2}'
        await message.channel.send(root)
    if '#now' in message.content:
        await message.channel.send(now)
    if '#help' in message.content:
        embed = discord.Embed(title = "がんばれ君が助けに来た！")
        embed.add_field(name = "`応答`", value = "たまに言葉で反応するときがあるよ！（「。」を使えば黙らせられるよー）", inline = False)
        embed.add_field(name = "`#pls x y`", value = "足し算できるよ！3個以上の数値もできるよ！（この場合はx+yになるよー）", inline = False)
        embed.add_field(name = "`#mns x y`", value = "引き算できるよ！3個以上の数値もできるよ！（この場合はx-yになるよー）", inline = False)
        embed.add_field(name = "`#tim x y**", value = "掛け算できるよ！3個以上の数値もできるよ！（この場合はx×yになるよー）", inline = False)
        embed.add_field(name = "**#div x y**", value = "割り算できるよ！3個以上の数値もできるよ！（この場合はx÷yになるよー）", inline = False)
        embed.add_field(name = "**#oio x y**", value = "割り算あまりできるよ！", inline = False)
        embed.add_field(name = "**#sqr x y**", value = "累乗できるよ！（この場合はxのy乗になるよー）", inline = False)
        embed.add_field(name = "**#rot x**", value = "ルートの値求めてくれるよ！", inline = False)
        embed.add_field(name = "**#llt x y z**", value = "ルーレットできるよ！（この場合はx,y,z,のどれかが出るよ！", inline = False)
        embed.add_field(name = "**#ebr**", value = "鯖内のメンバー数、人数、BOT数がわかるよ！", inline = False)
        embed.add_field(name = "**#fjk**", value = "くぁwせdrftgyふじこlp", inline = False)
        embed.add_field(name = "**#wiki**", value = "wikiで検索してくれるよ！", inline = False)
        embed.add_field(name = "**#wach x y**", value = "wikiでxの検索候補をy個表示してくれるよ！", inline = False)
        embed.add_field(name = '**#ranks**', value = 'それぞれのみんはやのランクの人数を教えてくれるよ！', inline = False)
        embed.add_field(name = '**#zikan**', value = 'タイマーを使えるよ！', inline = False)
        await message.channel.send(embed = embed)
    if '#llt' in message.content:
        rlt_list = message.content.split()
        rlt_list.remove('#llt')
        rlt_result = random.choice(rlt_list)
        await message.channel.send(rlt_result)
    if '#ebr' in message.content:
        embed = discord.Embed(title = 'みんはや鯖メンバー')
        guild = message.guild
        ebr_all = guild.member_count
        ebr_user = sum(1 for member in guild.members if not member.bot)
        ebr_bot = sum(1 for member in guild.members if member.bot)
        embed.add_field(name = '```メンバー数```', value = ebr_all)
        embed.add_field(name = '`人数`', value = ebr_user)
        embed.add_field(name = '`bot数`', value = ebr_bot)
        await message.channel.send(embed = embed)
    if '!d bump' in message.content:
        if message.content.startswith("!d bump"):
            if client.user!=message.author:
                def checks(m):
                    return m.channel == message.channel and m.author.id==302050872383242240
                bp=await client.wait_for('message', check=checks, timeout=15)
                msgid=bp.id
                embmsg=await message.channel.fetch_message(msgid)
                bumpdata="EmbedProxy(url='https://disboard.org/images/bot-command-image-bump.png', proxy_url='https://images-ext-1.discordapp.net/external/tAuRcs-FCy2M8OaTS9Ims62J1vrFiviahjBDtpZrrBs/https/disboard.org/images/bot-command-image-bump.png', width=800, height=200)"
                getdata=embmsg.embeds[0].image
                if str(bumpdata)==str(getdata):
                    await asyncio.sleep(7200)
                    embed = discord.Embed(title="BUMPできるよ！",description="BUMPがんばれ👍！",color=0x24B8B8)
                    await message.channel.send(embed=embed)
                    print("send:bump!!!")
    if '#ranks' in message.content:
        embed = discord.Embed(title = '**ランクごとの人数！**')
        guild = message.guild
        role_S2 = guild.get_role(774989846501654528)
        embed.add_field(name = '**S2ランク**', value = len(role_S2.members), inline = False)
        role_S1 = guild.get_role(774987289045630997)
        embed.add_field(name = '**S1ランク**', value = len(role_S1.members), inline = False)
        role_S = guild.get_role(774989364199424010)
        embed.add_field(name = '**Sランク**', value = len(role_S.members), inline = False)
        role_Ap = guild.get_role(774988208895033425)
        embed.add_field(name = '**A+ランク**', value = len(role_Ap.members), inline = False)
        role_A = guild.get_role(774987300420583475)
        embed.add_field(name = '**Aランク**', value = len(role_A.members), inline = False)
        role_Am = guild.get_role(774988863378030603)
        embed.add_field(name = '**A-ランク**', value = len(role_Am.members), inline = False)
        role_Bp = guild.get_role(774988447676235797)
        embed.add_field(name = '**B+ランク**', value = len(role_Bp.members), inline = False)
        role_B = guild.get_role(774988378596835339)
        embed.add_field(name = '**Bランク**', value = len(role_B.members), inline = False)
        role_Bm = guild.get_role(774988334509326337)
        embed.add_field(name = '**B-ランク**', value = len(role_Bm.members), inline = False)
        role_Cp = guild.get_role(774988120100700211)
        embed.add_field(name = '**C+ランク**', value = len(role_Cp.members), inline = False)
        role_C = guild.get_role(774988030590058526)
        embed.add_field(name = '**Cランク**', value = len(role_C.members), inline = False)
        role_Cm = guild.get_role(774987915004477470)
        embed.add_field(name = '**C-ランク**', value = len(role_Cm.members), inline = False)
        await message.channel.send(embed = embed)
    if message.content.startswith('#ebons'):
        guild = message.guild
        ebr_all = guild.member_count
        ebr_user = sum(1 for member in guild.members if not member.bot)
        ebr_bot = sum(1 for member in guild.members if member.bot)
        ebr_alls = f'メンバー数：{ebr_all}'
        ebr_users = f'人数：{ebr_user}'
        ebr_bots = f'bot数：{ebr_bot}'
        new_channel = await create_channel(message, channel_name = ebr_alls)
        new_channel = await create_channel(message, channel_name = ebr_users)
        new_channel = await create_channel(message, channel_name = ebr_bots)
    if '#fjk' in message.content:
        await message.channel.send('くぁwせdrftgyふじこlp')
    if client.user in message.mentions:
        await reply(message)
    if '#zikan' in message.content:
        await zikan(message)
    if '#wiki'in message.content:
        wiki0, wiki1 = message.content.split()
        wikipedia.set_lang('ja')
        try:
            page_title = wikipedia.page(wiki1)
            embed = discord.Embed(title = wiki1, url = f'https://ja.wikipedia.org/wiki/{wiki1}')
            page_summary = wikipedia.summary(wiki1)
            embed.add_field(name = page_title, value = page_summary, inline = False)
            await message.channel.send(embed = embed)
        except wikipedia.exceptions.DisambiguationError:
            page_search = wikipedia.search(wiki1, results = 11)
            page_search_url = f'https://ja.wikipedia.org/wiki/{page_search}'
            embed = discord.Embed()
            for page in page_search:
                page_int = page_search.index(page)
                page_url = f'https://ja.wikipedia.org/wiki/{page}'
                embed.add_field(name = page, value = f'「{page}」で再検索', inline = False)
            await message.channel.send(embed = embed)
    if nowa == '15:00':
        await timer()
    if '#ngadd' in message.content:
        await NG(message)
    if '#nglist' in message.content:
        embed = discord.Embed(title = 'NGワード一覧', description = 'このリスト内のワードは言っちゃだめだよ！')
        with open('NG') as ng:
            ngl = ng.read()
        fs = ngl.splitlines()
        for f in fs:
            embed.add_field(name = f, value = f, inline = False)
        await message.channel.send(embed = embed)
    if '#wach' in message.content:
        wiki0, wiki1, wiki2 = message.content.split()
        wikipedia.set_lang('ja')
        wiki22 = int(wiki2) + 1
        page_ach = wikipedia.search(wiki1, results = wiki22)
        page_search_url = f'https://ja.wikipedia.org/wiki/{page_ach}'
        embed = discord.Embed()
        for pages in page_ach:
            pages_int = page_ach.index(pages)
            pages_url = f'https://ja.wikipedia.org/wiki/{pages}'
            embed.add_field(name = pages, value = f'「{pages}」で再検索', inline = False)
        await message.channel.send(embed = embed)
    if message.channel.name == '自己紹介':
        yorosiku = "<:yorosiku:884506700126752828>"
        ok = "<:OK:884506700126752828>"
        await message.add_reaction(yorosiku)
        await message.add_reaction(ok)
    if message.content == "#hb":
        embed = discord.Embed(title = 'Hit&Browの遊び方', description = '相手の思っている数字を推理して当てるゲームだよ！\n数字と場所があってたら「Hit」、\n数字があっていても場所が違っていたら「Brow」でカウントするよ！\n最終的に3Hitにすれば勝ちだよ！')
        embed.add_field(name = '#hs', value = 'ゲームを始めるよ！', inline = False)
        embed.add_field(name = '#hc', value = 'あってるか確認するよ！', inline = False)
        embed.add_field(name = '#hd', value = 'どうしてもわからないときに使ってね！（答えが出るよ）', inline = False)
        await message.channel.send(embed = embed)
    if message.content == '#hs':
        if message.channel.id in rooms:
            await message.channel.send('使用中なう')
            return
        rooms[message.channel.id] = Room()
        await message.channel.send('スタート！')    
    if(message.content[0:3]=="#hc") and message.channel.id in rooms:
        req=message.content[3:]
        req=req.replace(" ","")
        if len(req)!=4:
            await message.channel.send('４桁の番号だよ！')
            return
        hit, brow = rooms[message.channel.id].step(req)
        rooms[message.channel.id].history.append({'request':req, 'hit':hit, 'brow':brow})
        await message.channel.send('リクエスト：'+ req + '\n結果：{}ヒット {}ブロー'.format(hit, brow))
        if req == rooms[message.channel.id].ans:
            await message.channel.send('正解！')
            say = '今までの記録だよ！\n質問回数：{}回| 数字 | ヒット | ブロー |\n'.format(len(rooms[message.channel.id].history))
            for i in rooms[message.channel.id].history:
                say = say + '| {} |  {}  |  {}  |\n'.format(i['request'],i['hit'],i['brow'])
            await message.channel.send(say)
            del rooms[message.chanenl.id]
    if message.content == '#hd' and message.channel.id in rooms:
        await message.channel.send('ゲーム終了！答え：' + rooms[message.channel.id].ans)
        del rooms[message.channel.id]
    if message.content == '#hy' and message.channel.id in rooms:
        say = '今までの記録だよ！\n質問回数：{}回| 数字 | ヒット |  ブロー |\n'.format(len(rooms[message.channel.id].history))
        for i in rooms[message.channel.id].history:
            say = say + '| {} |  {}  |  {}  |\n'.format(i['request'], i['hit'], i['brow'])
        await message.channel.send(say)
        
async def on_member_join(member):
    guild = member.guild
    channel = guild.get_channel(774679471809626124)
    await client.send_message(channel, 'よろしく！')


        


                                   
                                   
        
        
                            
                            
                        
                                                                                             
                                               
            


                                               
        
            
            
                                             
                                             
        
       
                   

client.run(token)
