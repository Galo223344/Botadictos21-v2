import psutil
import math
import discord
import requests
import json
import random

from discord.ext import commands
from discord.app import slash_command
from uptime import uptime
from __main__ import logchannel
from __main__ import bot_operators

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @slash_command(guild_ids=[894817804740620350], description="¡Visita el canal de YouTube de Gtadictos21!")
    async def youtube(self, ctx):

        embed=discord.Embed(title="Canal de YouTube:", description="https://youtube.com/c/Gtadictos21", color=ctx.author.color)
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)

    @slash_command(guild_ids=[894817804740620350], description="¿Eres miembro del canal? ¡Conecta tu cuenta!")
    async def miembro(self,ctx):

        embed=discord.Embed(title="¿Eres miembro del canal? Así puedes obtener el rol correspondiente:", description="", color=ctx.author.color)
        embed.add_field(name="Paso 1:", value="[Vincula tu cuenta de YouTube con Discord](https://gtadictos21.com/conectar-youtube). Recuerda utilizar la cuenta de YouTube con la que has comprado la membresia.", inline=False)
        embed.add_field(name="Paso 2:", value="Luego de vincular tu cuenta de YouTube, automaticamente recibirás el rol correspondiente. Si esto no ocurre, contactate con los <@&750491866570686535>.", inline=False)
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)
    
    @slash_command(guild_ids=[894817804740620350], description="Estado de los servidores de Gtadictos21")
    async def status(self,ctx):

        embed=discord.Embed(title="Estado de los servidores en:", description="https://status.gtadictos21.com", color=ctx.author.color)
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)
    
    @slash_command(guild_ids=[894817804740620350], description="¡Invita a tus amigos al servidor!")
    async def invitacion(self,ctx):

        embed=discord.Embed(title="Copia este link, e invita a tus amigos:", description="https://Gtadictos21.com/discord", color=ctx.author.color)
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)

    @slash_command(guild_ids=[894817804740620350], description="¡No pruebes este comando!")
    async def nopruebesestecomando(self,ctx):

        if ctx.channel.type is discord.ChannelType.private:
            return

        if ctx.author.id in bot_operators:
            embed=discord.Embed(title="¡Hey! No puedo hacer eso", description="", color=0xff0000)
            embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
            await ctx.respond(embed=embed, ephemeral=True)
            return
            

        embed=discord.Embed(title="¡Has sido troleado!", description="Puedes unirte [presionando aquí](https://Gtadictos21.com/discord).", color=0x008080)
        embed.set_footer(text=f"Este es un mensaje automatico, si crees que se envió por error, reportalo.", icon_url=self.bot.user.avatar.url)
        await ctx.author.send(embed=embed)
        await ctx.guild.kick(ctx.author)

        await ctx.respond("https://tenor.com/view/troll-troll-face-ragememe-rageface-trolling-gif-4929853")

        channel = self.bot.get_channel(logchannel)
        embed=discord.Embed(title="Alguien fue troleado, usó !nopruebesestecomando", color=0xff6600)
        embed.add_field(name=f"El usuario {ctx.author} usó el comando: !nopruebesestecomando", value="xDxDxDxDxD", inline=True)
        await channel.send(embed=embed)
    
    @slash_command(guild_ids=[894817804740620350], description="¡Mira todo sobre el bot!")
    async def botinfo(self,ctx):

        embed=discord.Embed(title="Haz click para ver el codigo fuente", url="https://github.com/Galo223344/Botadictos21/", description="", color=ctx.author.color)
        embed.add_field(name="Botadictos21 por:", value="<@388924384016072706>", inline=True)
        embed.add_field(name="Musicadictos21 por:", value="<@503739646895718401>", inline=True)
        embed.add_field(name="Para el servidor:", value="**El Club de los 21\'s**", inline=True)
        embed.add_field(name="Hosteado en:", value="[Sparked Host](https://gtadictos21.com/sparkedhost)", inline=True)
        embed.add_field(name="CPU:", value=f"{psutil.cpu_percent()}%", inline=True)
        embed.add_field(name="Memoria en uso:", value=f"{math.ceil((psutil.virtual_memory()[3]/1024)/1024)} MB ({psutil.virtual_memory()[2]}%)", inline=True)
        embed.add_field(name="Espacio en uso:", value=f"{round(math.ceil(((psutil.disk_usage('/')[1]/1024)/1024))/1024)}GB/{round(math.ceil(((psutil.disk_usage('/')[0]/1024)/1024))/1024)}GB  ({psutil.disk_usage('/')[3]}%)", inline=True)
        embed.add_field(name="Uptime:", value=f"{math.ceil(uptime()/3600)} horas", inline=True)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)

    @slash_command(guild_ids=[894817804740620350], description="¡Diviertete viendo memes de Reddit!")
    async def memes(self,ctx):

        listsubreddit= ["memessanos", "memes", "Divertido", "dankmemes", "me_irl", "CSGOmemes"]
        subreddit = random.choice(listsubreddit)
        res = requests.get(f'https://meme-api.herokuapp.com/gimme/{subreddit}')
        data = json.loads(res.text)
        titulo = data['title']
        autor = data['author']
        sub_reddit = data['subreddit']
        url = data['url']

        embed=discord.Embed(title=f"{titulo}", description=f"Publicado por {autor} en r/{sub_reddit}", color=ctx.author.color)
        embed.set_image(url=f"{url}")
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)
    
    @slash_command(guild_ids=[894817804740620350], description="¡Revisa la información sobre un usuario!")
    async def userinfo(self,ctx, member: discord.Member=None):

        if member == None:
            member = ctx.author
        pingyo = False
        if member.id == 388924384016072706:
            pingyo = True

        roles = [role for role in member.roles]
        esunbot = "No"

        if member.bot:
            esunbot = "Si"

        embed = discord.Embed(color=ctx.author.color)
        embed.set_author(name=f"Info de usuario - {member}")
        embed.add_field(name="ID:", value=f"`{member.id}`", inline=True)
        embed.add_field(name="Nombre:", value=member.display_name, inline=True)
        embed.add_field(name=f"Roles ({len(roles)}):", value=" ".join([role.mention for role in roles]), inline=False)
        embed.add_field(name="Cuenta creada el:", value=member.created_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Unido el:", value=member.joined_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="¿Es un bot?", value=f"{esunbot}", inline=False)
        embed.set_footer(text=f"Pedido por - {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url=member.avatar.url)
        if pingyo:
            embed.add_field(name="¿Es mi creador?", value="Si")
        await ctx.respond(embed=embed)
    
    @slash_command(guild_ids=[894817804740620350], description="¡Revisa el avatar de un usuario!")
    async def avatar(self, ctx, member: discord.Member=None):

        if member == None:
            member = ctx.author

        embed = discord.Embed(color=ctx.author.color)
        embed.set_image(url=f"{member.avatar.url}")
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)
    
    @slash_command(guild_ids=[894817804740620350], description="¿Quieres saber donde está hosteado el bot?")
    async def host(self,ctx):
        embed=discord.Embed(title="Powered by: https://Gtadictos21.com/sparkedhost", description="¿Querés tener tu propio servidor? ¡Usá el código `Gtadictos21` y obtené un 15\% de descuento!", color=ctx.author.color)
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)
    
    @slash_command(guild_ids=[894817804740620350], description="¡Eco!")
    async def eco(self,ctx,canal:discord.TextChannel,*,mensaje:str):
        
        if ctx.author.id not in bot_operators:
            embed=discord.Embed(title="¡No tienes permisos para utilizar este comando!", description="Necesitas contar con el permiso `BOT_OPERATOR`", color=0xff0000)
            embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
            await ctx.respond(embed=embed, ephemeral=True)
            return

        embed=discord.Embed(title=mensaje, colour=ctx.author.color)
        await canal.send(embed=embed)

        embed=discord.Embed(title=f"¡El mensaje ha sido enviado al canal #{canal}!", description="",  color=0x2bff00)
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed, ephemeral=True)
    
    @slash_command(guild_ids=[894817804740620350], description="¡Revisa toda la información sobre el servidor¡")
    async def serverinfo(self, ctx):

        if ctx.guild.premium_tier == 0:
            nivel_boost = "Nivel 0"
        elif ctx.guild.premium_tier == 1:
            nivel_boost = "Nivel 1"
        elif ctx.guild.premium_tier == 2:
            nivel_boost = "Nivel 2"
        else:
            nivel_boost = "Nivel 3"
        
        lista_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
        
        
        embed = discord.Embed(title="", description=ctx.guild.description, color=ctx.author.colour)
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
        embed.add_field(name="Dueño del servidor:", value=ctx.guild.owner, inline=False)
        embed.add_field(name="ID del servidor:", value=f"`{ctx.guild.id}`", inline=False)
        embed.add_field(name="Region del servidor:", value=ctx.guild.region, inline=False)
        embed.add_field(name="Lenguaje:", value=ctx.guild.preferred_locale, inline=False)
        embed.add_field(name="Cantidad de miembros:", value=f"{ctx.guild.member_count} (Bots: {len(lista_bots)})", inline=False)
        embed.add_field(name="Fecha de creación:", value=ctx.guild.created_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Nivel de Boost:", value=f"{nivel_boost} ({ctx.guild.premium_subscription_count} boots)", inline=False)
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url=ctx.guild.icon.url)
        await ctx.respond(embed=embed)
    
    @slash_command(guild_ids=[894817804740620350], description="Envia un embed con las reglas del servidor")
    async def reglas(self,ctx):

        if ctx.author.id not in bot_operators:
            embed=discord.Embed(title="¡No tienes permisos para utilizar este comando!", description="Necesitas contar con el permiso `BOT_OPERATOR`", color=0xff0000)
            embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
            await ctx.respond(embed=embed, ephemeral=True)
            return
            
        embed=discord.Embed(description="¡Si no recuerdas las reglas, siempre puedes revisarlas aquí!", color=0x00b7ff)
        embed.set_author(name=f"¡Bienvenido a {ctx.guild.name}!", icon_url=ctx.guild.icon.url)
        embed.add_field(name="#1", value="<a:Desaprobado:784983048508276787> **NO** insultar, discriminar o faltar el respeto entre los miembros/staff.", inline=False)
        embed.add_field(name="#2", value="<a:Desaprobado:784983048508276787> **NO** se permiten nombres/fotos obscenas. Queda a discreción del staff decidir que se considera como obsceno.", inline=False)
        embed.add_field(name="#3", value="<a:Desaprobado:784983048508276787> **NO** se permite el contenido +18/NSFW. Puede ser un meme cada tanto, pero no pongas una foto de tu prima.", inline=False)
        embed.add_field(name="#4", value="<a:Desaprobado:784983048508276787> **NO** spammear otros discords ajenos a esta comunidad.", inline=False)
        embed.add_field(name="#5", value="<a:Desaprobado:784983048508276787> **NO** spammear canales de YouTube/Twitch sin permiso.", inline=False)
        embed.add_field(name="#6", value="<a:Desaprobado:784983048508276787> **NO** se permite **comprar o vender NADA**, ya sea una bicicleta, un falcon o, un kilito de merca. ", inline=False)
        embed.add_field(name="#7", value="<a:Desaprobado:784983048508276787> **NO** se permite hacer flood, es decir, mensajes que puedan interrumpir una conversación o molestar como, por ejemplo, enviar demasiados mensajes en muy poco tiempo.", inline=False)
        embed.add_field(name="#8", value="<a:Desaprobado:784983048508276787> **NO** se permite hacer \"Name Boosting\", es decir, utilizar caracteres como `! & ?` para aparecer primero en las listas.", inline=False)
        embed.add_field(name="#9", value="<a:Aprobado:784983108663246908> **USAR** los canales correspondientes, si vas a mandar un meme, mándalo a <#750496337916592199>, etc.", inline=False)
        embed.add_field(name="#10", value="<a:Desaprobado:784983048508276787> Al entrar a un chat de voz, **NO GRITES NI SATURES EL MICROFONO**.", inline=False)
        embed.add_field(name="#11", value="<a:Alerta:784982996225884200> **SI USAS CHEATS/SCRIPTS, TE REGALAMOS UNAS VACACIONES PERMANENTES A UGANDA.**", inline=False)
        embed.add_field(name="#12", value="<a:Aprobado:784983108663246908> Para conseguir el rango de <@&750492534857400321> tenes que hablar con un <@&750492134695764059> o en su defecto con un <@&750491866570686535>, ¡y sin problemas, te lo van a dar!", inline=False)
        embed.add_field(name="#13", value="<a:Aprobado:784983108663246908> Ante cualquier duda o consulta, podes hablar con un <@&750492134695764059> o un <@&750491866570686535> y seguro te ayudan a solucionar el problema", inline=False)
        embed.add_field(name="⠀", value="<a:Aprobado:784983108663246908> Recuerda que este servidor se guia por los [Términos y Condiciones de Discord](https://www.discord.com/terms) y por las [Directivas de la Comunidad](https://www.discord.com/guidelines).", inline=False)
        embed.set_footer(text="Nos reservamos el derecho de hacer cambios a las reglas y/o los Términos y condiciones en cualquier momento, sin previo aviso.", icon_url=ctx.guild.icon.url)
        welcome_message = await ctx.send(embed=embed)
        embed=discord.Embed(color=0x00b7ff)
        embed.add_field(name="¿Has sido baneado de este servidor de manera injusta? Puedes apelar aquí:", value="Haz [click aquí](https://Gtadictos21.com/apelacion-ban) para rellenar el formulario de apelaciones.", inline=False)
        embed.set_footer(text="Recuerda que nunca serás baneado si respetas nuestras reglas, así como los Términos y Condiciones de Discord.", icon_url=ctx.guild.icon.url)
        await ctx.respond(embed=embed)
    
    @slash_command(guild_ids=[894817804740620350], description="¡Envia tu sugerencia!")
    async def sugerencia(self,ctx, *, sugerencia=None):

        if sugerencia == None:
            embed=discord.Embed(title="¡La sugerencia no puede estar vacía!", description="", color=0xff0000)
            embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
            await ctx.respond(embed=embed, ephemeral=True)
            return

        sugerencia = str(sugerencia)

        channel=self.bot.get_channel(sugchannel)

        embed=discord.Embed(color=0x8080ff)
        embed.add_field(name=f"El usuario {ctx.author} ha sugerido lo siguiente:", value=f"\"{sugerencia}\"", inline=True)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        mnsj = await channel.send(embed=embed)
        await mnsj.add_reaction("✅")
        await mnsj.add_reaction("❌")

        embed=discord.Embed(title="¡La Sugerencia fue enviada con exito!", description="", color=0x008080)
        embed.set_footer(text=f"Pedido por: {ctx.author.display_name}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Misc(bot))