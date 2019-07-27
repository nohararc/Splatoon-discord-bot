import discord
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dbname = os.path.join(BASE_DIR, "splatoon2.sqlite3")
conn = sqlite3.connect(dbname)
cur = conn.cursor()


def random_buki():
    cur.execute('select name, sub, special from weapons ORDER BY RANDOM() limit 1')
    name, sub, special = cur.fetchall()[0]
    print(name)
    return name


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ぬりたく～る'):
        await message.channel.send('テンタクル!!!')

    if message.content == '/buki':
        buki = random_buki()
        await message.channel.send(f"{message.author.mention}は{buki}を使って塗りまくれ～")

    if message.content == 'a':
        buki = random_buki()
        await message.channel.send(f"{message.author.mention}は{buki}を使えば？")

    if message.content == '/bukia':
        voice_channel = message.guild.voice_channels[0]
        msg = []
        for member in voice_channel.members:
            buki = random_buki()
            msg.append(f'{member.mention}は{buki}')
        await message.channel.send("\n".join(msg))


async def on_member_join(member):
    await message.channel.send(f"{member}さん、いらっしゃーい")
client.run('my token goes here')

