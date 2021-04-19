import discord 
from discord.ext import commands
import random
import pickle
import json
import os

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('Bot is ready')



os.chdir(r'C:\Users\jmcod\Desktop\python\workspace\DiscordBot')

# Sistema Funas

@client.command()
async def funar(ctx, *, nombre):
    if (nombre[0] != '<') :
        await ctx.send('Debes funar a alguien.\nUsa el @ sacowea.')
        return
    if ' ' in nombre:
        await ctx.send('Pon el puro nombre weta...')
        return
    try:
        a_file = open("Funados.txt", "rb")
        Funados = pickle.load(a_file)
        a_file.close()
    except:
        Funados = {}

    if nombre in Funados.keys():
        Funados[nombre] += 1
    else:
        Funados[nombre] = 1
    
    a_file = open("funados.txt", "wb")
    pickle.dump(Funados, a_file)
    a_file.close()

    await ctx.send(f'Quiero funar a {nombre}.\n{nombre} ha sido funado {Funados[nombre]} veces. ')
   

@client.command()
async def masfunados(ctx):
    try:
        a_file = open("Funados.txt", "rb")
        Funados = pickle.load(a_file)
        a_file.close()
    except:
        Funados = {}

    topfunados = sorted(Funados.items(),key = lambda funado:funado[1], reverse = True)
    topfunados = topfunados[0:7]
    message = ''
    for f,v in topfunados:
        message += f'{f}, {v}\n'
    await ctx.send(message)

@client.command()
async def reyfunado(ctx):
    try:
        a_file = open("Funados.txt", "rb")
        Funados = pickle.load(a_file)
        a_file.close()
    except:
        Funados = {}

    topfunados = sorted(Funados.items(),key = lambda funado:funado[1], reverse = True)
    f, v = topfunados[0]
    await ctx.send(f'{f} es el rey de los funados, con {v} funas.')

@client.command()
async def k(ctx, name):
    print(type(name))
    print(name)

@client.command()
async def pejerrey(ctx):
    await ctx.send('De Linares pa\' arria') 



@client.command()
async def teleserie(ctx):
    await ctx.send('TA WENAAA')

@client.command(aliases = ['basado'])
async def piza(ctx):
    await ctx.send('El piza es medio fleto, pero no le digan.')

@client.command()
async def anibal(ctx):
    await ctx.send('La historia de Anibal parte un dia oscuro, el dia en que el Piza entró a su habitación, el dia en que el Victor lo vio todo.\n Era un dia lluvioso, de mayo si mal no recuerdo. La bruma del rio cubría todo Talca, ciudad de completos y flores. Pero el aire susurraba silenciosamente, Anibal fleto... Anibal fleto...')

client.run('ODIxMTU5MTcyOTkyNDAxNDE5.YE_qEw.6IAPEpHacNpf1y0HmV5MjF1bgrA')

