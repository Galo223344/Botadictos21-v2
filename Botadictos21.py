import os
import time
import discord
import psutil # pip install psutil
import math
import random
import asyncio
import json
import urllib.request # pip install urllib3

from tldextract import extract # pip install tldextract
from colorama import Fore # pip install colorama
from colorama import Style
from discord.ext import commands 
from datetime import datetime

# Cargamos el archivo config.json
with open("config.json") as f:
    data = json.load(f)
    token = data["discord-token"] # Token de Discord
    global guild
    guild_id = data["guild-id"] #ID de la guild
    global bot_operators
    bot_operators = data["bot-operators"] # IDs de los operadores del bot (Acceso a cargar/descargar cogs y demas)
    global logchannel
    logchannel = data["logchannel"] # Canal en donde envia las alertas cuando el bot se enciende
    global sugchannel
    sugchannel = data["sugchannel"] # Canal en donde envia las alertas cuando el bot se enciende
    global gvchannel
    gvchannel = data["gvchannel"] # Canal en donde envia las alertas cuando el bot se enciende



# Ponemos todos los intents de discord (Porque los necesitamos)
intents = discord.Intents.all()

# Configuramos la instancia del bot
bot = discord.Bot(intents=intents)


# Empieza un loop con distintos status
@bot.event    
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a Gtadictos 21 | Usá !ayuda", url="https://youtube.com/c/gtadictos21"))
        await asyncio.sleep(10)
        guild = bot.get_guild(894817804740620350) # ID del servidor de Gtadictos21
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"a {guild.member_count} usuarios | Usá !ayuda"))
        await asyncio.sleep(10)
        elegido = random.choice(guild.members)
        elegido = elegido.name
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"a {elegido} 👀 | Usá !ayuda"))
        await asyncio.sleep(10)

# Inicia el loop y avisa que el bot se conectó		
@bot.event      
async def on_ready():
    ...
    bot.loop.create_task(status_task())
    guild = bot.get_guild(894817804740620350) # ID del servidor de Gtadictos21	
    print(f'{Fore.RED}[BOT INFO]{Fore.CYAN}¡{bot.user.name} se ha conectado!¡Este servidor tiene {Fore.MAGENTA}{guild.member_count}{Fore.CYAN} usuarios!{Style.RESET_ALL}')
    print(f'{Fore.RED}[BOT INFO]{Fore.CYAN}El ID del bot es: {Fore.MAGENTA}{bot.user.id}{Style.RESET_ALL}')
    print(f'{Fore.RED}[BOT INFO]{Fore.CYAN}Bot creado por: {Fore.MAGENTA}Galo223344 {Fore.CYAN}&{Fore.MAGENTA} Gtadictos21{Style.RESET_ALL}')
    print(f'{Fore.RED}[BOT INFO]{Fore.CYAN}Repositorio oficial: {Fore.MAGENTA}https://github.com/galo223344/Botadictos21{Style.RESET_ALL}')
    print(f'{Fore.RED}[BOT INFO]{Fore.CYAN}ID de los operadores: {Fore.MAGENTA}{bot_operators}{Style.RESET_ALL}')
    print(f'{Fore.RED}[SERVER INFO]{Fore.CYAN}Uso de CPU: {Fore.MAGENTA}{psutil.cpu_percent()}%{Style.RESET_ALL}')
    print(f'{Fore.RED}[SERVER INFO]{Fore.CYAN}Uso de RAM: {Fore.MAGENTA}{math.ceil((psutil.virtual_memory()[3]/1024)/1024)}MB {Fore.CYAN}({Fore.MAGENTA}{psutil.virtual_memory()[2]}%{Fore.CYAN}){Style.RESET_ALL}')
    print(f'{Fore.RED}[SERVER INFO]{Fore.CYAN}Ping: {Fore.MAGENTA}{round(bot.latency * 1000)} ms{Style.RESET_ALL}')
    
    # Envia embed para avisar que el bot está activo, junto con algunos datos como uso de CPU, RAM y disco duro
    channel = bot.get_channel(894817856091467796) # ID del canal donde envia el mensaje

    #IP del servidor host
    host = urllib.request.urlopen('https://ident.me').read().decode('utf8')

    embed=discord.Embed(title=f"¡{bot.user.name} se ha conectado!", description=f"¡Este servidor tiene {guild.member_count} usuarios!", timestamp= datetime.now(), color=0x2bff00)
    embed.add_field(name="CPU:", value=f"{psutil.cpu_percent()}%", inline=True)
    embed.add_field(name="Memoria en uso:", value=f"{math.ceil((psutil.virtual_memory()[3]/1024)/1024)} MB ({psutil.virtual_memory()[2]}%)", inline=True)
    embed.add_field(name="Espacio en uso:", value=f"{round(math.ceil(((psutil.disk_usage('/')[1]/1024)/1024))/1024)}GB/{round(math.ceil(((psutil.disk_usage('/')[0]/1024)/1024))/1024)}GB  ({psutil.disk_usage('/')[3]}%)", inline=True)
    embed.add_field(name="Ping:", value=f"{round(bot.latency * 1000)} ms", inline=True)
    embed.add_field(name="Host:", value=f"{host}", inline=True)
    embed.set_thumbnail(url=bot.user.avatar.url)
    await channel.send(embed=embed)

# Si se taggea al bot, envia un mensaje explicando como usar sus comandos. Si se utiliza "!", envia un error
@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        channel = message.channel

        tips = ["Si quieres saber mas sobre mi, utiliza el comando \'/botinfo\'", "¡Este bot fue creado por Galo y Gtadictos21!", "¿Tu internet está funcionando mal? ¡Utiliza \'/ping\' y pruebalo!"]
        random_tips = random.choice(tips)
        
        embed=discord.Embed(title="¡Hola! Soy Botadictos21 🤖", description="Para usar mis comandos, utilizá `/`", color=0x008080)
        embed.set_footer(text=f"{random_tips}", icon_url=bot.user.avatar.url)
        await channel.send(embed=embed)

    elif message.content.startswith("!"):
        channel = message.channel

        tips = ["Si quieres saber mas sobre mi, utiliza el comando \'/botinfo\'", "¡Este bot fue creado por Galo y Gtadictos21!", "¿Tu internet está funcionando mal? ¡Utiliza \'/ping\' y pruebalo!"]
        random_tips = random.choice(tips)

        if "!" in message.content:
            string = message.content
            comando = string.replace("!", "") 

        embed=discord.Embed(title="¡Uy! No entiendo el comando :(", description=f"Recuerda que debes utilizar `/`. Por ejemplo: `/{comando}`", color=0xff0000)
        embed.set_footer(text=f"{random_tips}", icon_url=bot.user.avatar.url)
        await channel.send(embed=embed)


##########################################################
#
# Comandos basicos
#
##########################################################

# Comando de ping (Para saber si el bot está vivo)
@bot.slash_command(name='ping', guild_ids=[894817804740620350], description="¡Revisa la latencia del bot!")
async def _ping(ctx):
    start_time = time.time()
    message = await ctx.send("API ping")
    end_time = time.time()
    await message.delete()
    
    embed=discord.Embed(color=ctx.author.color)
    embed.add_field(name="API ping:", value=f"{round((end_time - start_time) * 1000)}ms", inline=False)
    embed.add_field(name="Bot ping:", value=f"{round(bot.latency * 1000)}ms", inline=False)
    embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
    await ctx.respond(embed=embed)


# Agrega links a la lista negra, y recarga el cog de spam
@bot.slash_command(guild_ids=[894817804740620350], description="Agrega links maliciosos a la lista negra")
async def add(ctx, link = None):

    if ctx.author.id not in bot_operators:
        embed=discord.Embed(title="¡No tienes permisos para utilizar este comando!", description="Necesitas contar con el permiso `BOT_OPERATOR`", color=0xff0000)
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed, ephemeral=True)
        return
            
    if link == None:
        embed=discord.Embed(title="¡Argumento inválido!", description="", color=0x008080)
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed, ephemeral=True)
        return

    tsd, td, tsu = extract(link) 
    url = td + '.' + tsu

    with open('spamlist.txt') as f:   
        lines = f.read().splitlines()

        if url in lines:
            embed=discord.Embed(title="¡Este link ya se encuentra en la lista negra!", description="", color=0xff0000)
            embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
            await ctx.respond(embed=embed, ephemeral=True)
            return
        else:
            with open('spamlist.txt','a') as file:
                file.write(f"{url}\n")
                print(f'{Fore.RED}[BOT INFO]{Fore.WHITE}¡El link: \"{Fore.MAGENTA}{url}{Fore.WHITE}\" ha sido agregado a la lista de spam!{Style.RESET_ALL}')
        
    embed=discord.Embed(title="¡Un nuevo link ha sido agregado a la lista de spam!", description=f"Link agregado: **{url}** ", color=0x008080)
    embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
    await ctx.respond(embed=embed)

    bot.unload_extension("cogs.spam")
    bot.load_extension("cogs.spam")
    print(f'{Fore.RED}[BOT INFO]{Fore.WHITE}¡El cog \"spam\" se ha recargado!{Style.RESET_ALL}')

    channel = bot.get_channel(logchannel)
    embed=discord.Embed(title=f"¡El administrador {ctx.author.display_name} agregó un nuevo link a la lista de spam:", description=f"Link agregado: \"{url}\"", timestamp= datetime.now(), color=0xff7d00)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"ID del usuario: {ctx.author.id}")
    await channel.send(embed=embed)


##########################################################
#
# Cogs
#
##########################################################

@bot.slash_command(guild_ids=[894817804740620350], description="Carga un cog")
async def load(ctx, extension):

    if ctx.author.id not in bot_operators:
        embed=discord.Embed(title="¡No tienes permisos para utilizar este comando!", description="Necesitas contar con el permiso `BOT_OPERATOR`", color=0xff0000)
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed, ephemeral=True)
        return

    bot.load_extension(f"cogs.{extension}")

    embed=discord.Embed(title=f"¡El cog {extension} ha sido cargado!", description="", color=0xff0000)
    embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
    await ctx.respond(embed=embed)

    channel=bot.get_channel(logchannel)
    embed=discord.Embed(title=f"Un operador ha cargado una extensión:", description=f"El operador {ctx.author.mention} ha cargado el cog **{extension}**", timestamp= datetime.now(), color=0xff7d00)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"ID del usuario: {ctx.author.id}")
    await channel.send(embed=embed)

@bot.slash_command(guild_ids=[894817804740620350], description="Descarga un cog")
async def unload(ctx, extension):

    if ctx.author.id not in bot_operators:
        embed=discord.Embed(title="¡No tienes permisos para utilizar este comando!", description="Necesitas contar con el permiso `BOT_OPERATOR`", color=0xff0000)
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed, ephemeral=True)
        return

    bot.unload_extension(f"cogs.{extension}")

    embed=discord.Embed(title=f"¡El cog {extension} ha sido descargado!", description="", color=0xff0000)
    embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
    await ctx.respond(embed=embed)


    channel=bot.get_channel(logchannel)
    embed=discord.Embed(title=f"Un operador ha descargado una extensión:", description=f"El operador {ctx.author.mention} ha descargado el cog **{extension}**", timestamp= datetime.now(), color=0xff7d00)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"ID del usuario: {ctx.author.id}")
    await channel.send(embed=embed)

@bot.slash_command(guild_ids=[894817804740620350], description="Recarga un cog")
async def reload(ctx, extension):
    
    if ctx.author.id not in bot_operators:
        embed=discord.Embed(title="¡No tienes permisos para utilizar este comando!", description="Necesitas contar con el permiso `BOT_OPERATOR`", color=0xff0000)
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed, ephemeral=True)
        return

    if extension == "all":

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.unload_extension(f"cogs.{filename[:-3]}")

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.load_extension(f"cogs.{filename[:-3]}")

        embed=discord.Embed(title=f"¡Todas los cogs han sido recargados!", description="", color=0xff0000)
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)

        channel=bot.get_channel(logchannel)
        embed=discord.Embed(title=f"Un operador ha recargado todas las extensiones", description=f"El operador {ctx.author.mention} ha recargado todas las extensiones", timestamp= datetime.now(), color=0xff7d00)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.set_footer(text=f"ID del usuario: {ctx.author.id}") 
        await channel.send(embed=embed)
        return

    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")

    embed=discord.Embed(title=f"¡El cog {extension} ha sido recargado!", description="", color=0xff0000)
    embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
    await ctx.respond(embed=embed)

    channel=bot.get_channel(logchannel)
    embed=discord.Embed(title=f"Un operador ha recargado una extensión:", description=f"El operador {ctx.author.mention} ha recargado el cog **{extension}**", timestamp= datetime.now(), color=0xff7d00)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=f"ID del usuario: {ctx.author.id}")
    await channel.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")


# Corremos el bot. El token está en el archivo "config.json"
bot.run(token)