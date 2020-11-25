import discord
from discord.ext import commands
from decouple import config
import os

print("MAIN : STARTED")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=["rs!","Rs!","rS!"],intents=intents,case_insensitive=True)
bot.remove_command("help")

def load_cogs():
  print('MAIN : LOADING COGS')
  for file in os.listdir('./cogs'):
    if file.endswith('.py') and not file.startswith('_'):
      bot.load_extension(f'cogs.{file[:-3]}')

@bot.event
async def on_ready():
  print("MAIN : BOT ONLINE")
  load_cogs()

bot.run(config("TOKEN"))

