import discord
from discord.ext import commands

# Configura as permissões (Intents)
intents = discord.Intents.default()
intents.message_content = True  # Permite ler o conteúdo das mensagens

# Define o prefixo do bot (ex: !ajuda)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot logado como {'Terraria2.0'} (ID: {1450518108665282771})')
    print('------')

@bot.command()
async def ola(ctx):
    await ctx.send(f'Olá {ctx.author.name}, eu estou vivo!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latência: {round(bot.latency * 1000)}ms')


bot.run('MTQ1MDUxODEwODY2NTI4Mjc3MQ.GTUx1S.o3cJxgDbzCslN5L5pbbgwZ42StNtr3BURtNG_Q')
