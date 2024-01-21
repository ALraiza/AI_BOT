import discord
from discord.ext import commands
import random, os
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in  ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f'{file_name}')
            await ctx.send(f'file disimpan atas nama{file_name}')
            hasil = get_class('keras_model.h5', 'labels.txt', file_name)

            if hasil[0] == 'kucing\n' and hasil[1] >= 0.6:
                await ctx.send('INI ADALAH KUCING')
                await ctx.send('....')
            elif hasil[0] == 'anjing\n' and hasil[1] >+ 0.6:
                await ctx.send('INI ADALAH ANJING')
                await ctx.send('....')
            else:
                await ctx.send('GAMBAR TIDAK VALID!')

    else:
        await ctx.send(f'gambar belom terkirim{file_name}')

bot.run("MTEzNDEwNDYxMDE3NzU2NDc3NA.GtgU2y.h-ARm3KFGreZjrr56vr7URsw87_9xpet6dRAgg")