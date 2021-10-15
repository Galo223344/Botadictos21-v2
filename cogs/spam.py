import discord
import asyncio

from colorama import Fore 
from colorama import Style
from datetime import datetime
from discord.ext import commands
from discord.app import slash_command
from __main__ import logchannel
from __main__ import bot_operators

class Spam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Cargamos la lista de spam en la variable list_url
    try:
        client = MongoClient(MongoDB_URL)
        db = client['bot']
        spamlist = db['spamlist']
        encontrado = spamlist.find({},{'_id': 1 })
        for data in encontrado:
            x = json.dumps(data)
            y = json.loads(x)
            global list_url
            list_url = y["_id"]
            print(f'{Fore.RED}[MONGODB INFO]{Fore.CYAN}¡Se ha conectado con la colección spamlist!{Style.RESET_ALL}')
    except:
        print(f'{Fore.RED}[MONGODB ERROR]{Fore.CYAN}¡No se ha podido conectar con la colección spamlist! Revisa el cog Spam{Style.RESET_ALL}')

    @commands.Cog.listener()
    async def on_message(self, message):

        # Si el mensaje fue enviado por mensaje privado, lo ignoramos
        if message.channel.type is discord.ChannelType.private:
            return

        # La verdad no se porque hay que hacer esto, pero un día dejó de funcionar lol
        guild = message.guild
        member = guild.get_member(message.author.id)

        # Revisamos si el que envió el mensaje es un mod/admin
        if member.id in bot_operators:
            return

        mensaje_procesado2 = []
        mensaje_procesado = []

        # Convertimos el mensaje a minusculas para evitar que eviten el sistema
        mensaje_minus = message.content.lower()

        # Lo separamos por "/"
        mensaje_procesado1 = mensaje_minus.split("/")

        # Lo separamos por espacios así podemos obtener el codigo de invitacion en un solo item de lista
        for i in mensaje_procesado1:
            i = i.split(" ")
            mensaje_procesado2.append(i)

        # Aplanamos la lista

        for sublist in mensaje_procesado2:
            for item in sublist:
                mensaje_procesado.append(item.replace("|",""))

        # Revisamos si el mensaje tiene "discord.gg" O "discord.com" seguido de un "invite"
        if "discord.gg" in mensaje_procesado or ("discord.com" in mensaje_procesado and mensaje_procesado[mensaje_procesado.index("discord.com")+1] == "invite"):

            codigos = []

            # Conseguimos las invitaciones validas actuales
            invitaciones = await message.guild.invites()

            # Separamos los codigos de las invitaciones y los guardamos en la lista "codigos"
            for i in invitaciones:
                i = i.code
                codigos.append(i)

            # Comenzamos el checkeo de discord.gg
            if "discord.gg" in mensaje_procesado:
                # Si el siguiente item despues de "discord.gg" en la lista de mensaje_procesado está en la lista de codigos
                if mensaje_procesado[mensaje_procesado.index("discord.gg")+1] in codigos:
                    return
                elif mensaje_procesado[mensaje_procesado.index("discord.gg")+1] == "gtadictos21":
                    return
                else:
                    # Si no lo está, significa que es una invitación de otro servidor. Así que avisamos al usuario y eliminamos el mensaje
                    embed=discord.Embed(title="¡Por favor, evitá enviar invitaciones de otros servidores de Discord!", description="", color=0xff0000)
                    embed.set_footer(text=f"Este es un mensaje automatico, si crees que se envió por error, reportalo.", icon_url=self.bot.user.avatar.url)
                    await message.author.respond(message.author.mention, embed=embed)
                    await message.delete()

                    # Enviamos un log al canal de logs
                    channel = self.bot.get_channel(logchannel)
                    embed=discord.Embed(title=f" El usuario {message.author} trató de enviar una invitación a otro servidor.", timestamp= datetime.now(), color=0x804000)
                    embed.add_field(name="Mensaje original:", value=message.content, inline=False)
                    embed.set_thumbnail(url=message.author.avatar_url)
                    embed.set_footer(text=f"ID del usuario: {message.author.id}")
                    await channel.send(embed=embed)

                    await asyncio.sleep(15)
                    return

            # Comenzamos el checkeo de discord.com
            if "discord.com" in mensaje_procesado:
                # Si el siguiente item despues de "invite" en la lista de mensaje_procesado está en la lista de codigos
                if mensaje_procesado[mensaje_procesado.index("invite")+1] in codigos:
                    return
                else:
                    # Si no lo está, significa que es una invitación de otro servidor. Así que avisamos al usuario y eliminamos el mensaje
                    embed=discord.Embed(title="¡Por favor, evitá enviar invitaciones de otros servidores de Discord!", description="", color=0xff0000)
                    embed.set_footer(text=f"Este es un mensaje automatico, si crees que se envió por error, reportalo.", icon_url=self.bot.user.avatar.url)
                    await message.author.send(message.author.mention, embed=embed)
                    
                    await message.delete()
                    await message.delete()

                    # Enviamos un log al canal de logs
                    channel = self.bot.get_channel(logchannel)
                    embed=discord.Embed(title=f" El usuario {message.author} trató de enviar una invitación a otro servidor.", timestamp= datetime.now(), color=0x400080)
                    embed.add_field(name="Mensaje original:", value=message.content, inline=False)
                    embed.set_thumbnail(url=message.author.avatar_url)
                    embed.set_footer(text=f"ID del usuario: {message.author.id}")
                    await channel.send(embed=embed)

                    await asyncio.sleep(15)
                    return

        for spam in list_url:

            if spam in mensaje_procesado:
                await message.delete()
                embed=discord.Embed(title=f"El link que acabas de enviar ({spam}) está prohibido. Por favor, comunicate con los administradores para ser desmuteado.", description="Haz click [aquí](https://Gtadictos21.com/discord) para contactarlos.", color=0xff0000)
                embed.set_footer(text=f"Este es un mensaje automatico, si crees que se envió por error, reportalo.", icon_url=self.bot.user.avatar.url)
                await message.author.send(message.author.mention, embed=embed)


                Role = discord.utils.get(member.guild.roles, name="Silenciado")
                role2 = discord.utils.get(member.guild.roles, name="La People👤")
                await member.add_roles(Role)
                await member.remove_roles(role2)

                channel = self.bot.get_channel(logchannel)
                embed=discord.Embed(title=f" El usuario {message.author} envió un link engañoso y fue muteado automaticamente.", timestamp= datetime.now(), color=0x804000)
                embed.add_field(name="Mensaje original:", value=message.content, inline=False)
                embed.set_thumbnail(url=message.author.avatar.url)
                embed.set_footer(text=f"ID del usuario: {message.author.id}")
                await channel.send(embed=embed)
                return

def setup(bot):
    bot.add_cog(Spam(bot))