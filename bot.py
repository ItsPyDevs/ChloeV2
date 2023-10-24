import discord
from discord.ext import commands
import sqlite3
import argparse
import shutil

bot = commands.Bot(command_prefix="&", intents=discord.Intents.all())

conn = sqlite3.connect('responses.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS responses (
        key TEXT PRIMARY KEY,
        value TEXT
    )
''')
conn.commit()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def save(ctx, filename):
    if ctx.author.guild_permissions.administrator:
        try:
            shutil.copy('responses.db', f'{filename}.db')
            await ctx.send(f"Base de données sauvegardée sous le nom '{filename}.db'")
        except Exception as e:
            await ctx.send(f"Une erreur s'est produite lors de la sauvegarde : {e}")
    else:
        await ctx.send("Désolé, vous n'avez pas les autorisations nécessaires pour effectuer cette action.")


@bot.command()
async def learn(ctx):
    if ctx.author.guild_permissions.administrator:
        content = ctx.message.content[len("&learn "):]
        parts = content.split("=")  
        if len(parts) == 2:
            key = parts[0].strip()  
            value = parts[1].strip() 
            cursor.execute('INSERT OR REPLACE INTO responses (key, value) VALUES (?, ?)', (key, value))
            conn.commit()
            await ctx.send(f"J'ai apppris : '{key}' -> '{value}'")
        else:
            await ctx.send("Utilisation correcte : `&learn PHRASECLé=PHRASE RéPONSE`")
    else:
        await ctx.send("Désolé, vous n'avez pas les autorisations nécessaires pour effectuer cette action.")


@bot.command()
async def tuto(ctx):
    tutorial_embed = discord.Embed(
        title="🔧 Comment apprendre au bot avec la commande &learn",
        description="Voici comment ajouter des réponses pré-définies au bot :",
        color=discord.Color.blue()
    )

    tutorial_embed.add_field(name="🔑 1. Ajouter une réponse", value="Utilisez la commande `&learn clé=valeur`.", inline=False)
    tutorial_embed.add_field(name="🔍 2. Exemple", value="`&learn qui est tu=J'ai été codé par ItsPyDevs et inspiré du bot Chloé codé par Aywen`", inline=False)
    tutorial_embed.add_field(name="⚙️ 3. Utilisation", value="Demandez au bot en utilisant la clé que vous avez apprise.", inline=False)
    tutorial_embed.add_field(name="Exemple", value="Si vous dites : 'qui est tu', le bot répondra avec : 'J'ai été codé par ItsPyDevs et inspiré du bot Chloé codé par Aywen'", inline=False)
    tutorial_embed.set_footer(text="Assurez-vous d'avoir les autorisations nécessaires pour utiliser &learn.")

    await ctx.send(embed=tutorial_embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()

    
    if content.startswith("&"):
        await bot.process_commands(message)
    else:
        cursor.execute('SELECT value FROM responses WHERE key = ?', (content,))
        response = cursor.fetchone()
        if response:
            await message.channel.send(response[0])
        else:
            await message.channel.send("Erreur 404 : Réponse non trouvée.")

bot.run("BOT_TOKEN")

conn.close()
