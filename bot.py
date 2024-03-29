import random
import discord
from discord.ext import commands
import requests
import asyncio

intents = discord.Intents.default()
intents.message_content = True  # Explicitly enable message_content intent

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Brawl Stars"))
    print("Bot is Ready")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="insult", description="This Command sends a random insult sentence!")
async def hello(interaction: discord.Interaction, user: str):
    url = "https://evilinsult.com/generate_insult.php?lang=en&type=json&num=" + str(random.randint(0, 999))
    data = requests.get(url)
    json_data = data.json()
    await interaction.response.send_message(f"{user} {json_data['insult']}", ephemeral=True)  # Correct indentation

bot.run('MTIxNDk1NTIwOTAzODQ5NTgwNw.GfnIUj.Fi_SLWJvi3dRB9LbZNlJ7F4sLfSug24j1b-lz4')
