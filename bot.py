import random
import discord
from discord.ext import commands
from discord_ui import View , Button
import requests
import asyncio
from discord import Interaction
bot = commands.Bot(command_prefix="/", intents = discord.Intents.all())


@bot.event
async def on_ready():
    
    await bot.change_presence(status=discord.Status.idle,activity=discord.Game("Brawl Stars"))
    print("Bot is Ready")

    try:
        synced = await bot.tree.sync()
        print(f"Synces {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.tree.command(name="insult",description="This Command sends a random insult sentence !")
async def hello(interaction: discord.Interaction,user: str):
    url = "https://evilinsult.com/generate_insult.php?lang=en&type=json&num=" + str(random.randint(0, 999))
    data = requests.get(url)
    json_data = data.json()
    ephemeral=True
    await interaction.response.send_message(f""+user+" "+json_data["insult"],ephemeral=ephemeral)

@bot.tree.command(name="roll",description="This Command rolls a dice !")
async def roll(interaction: discord.Interaction):
    await interaction.response.send_message("Think")
    await asyncio.sleep(10)
    die_face = ["https://cdn.discordapp.com/attachments/1045735310350356490/1085928064300621924/Dice_Face1.png","https://cdn.discordapp.com/attachments/1045735310350356490/1085928064560681071/Dice_Face2.png","https://cdn.discordapp.com/attachments/1045735310350356490/1085928064770392174/Dice_Face3.png","https://cdn.discordapp.com/attachments/1045735310350356490/1085928063268823131/Dice_Face4.png","https://cdn.discordapp.com/attachments/1045735310350356490/1085928063570825266/Dice_Face5.png","https://cdn.discordapp.com/attachments/1045735310350356490/1085928063839256647/Dice_Face6.png"]
    die_num=random.randint(0,5)
    die = die_face[die_num]
    embed = discord.Embed(color=discord.Color.dark_gold())
    embed.set_image(url =die)
    embed.set_author(name = die_num+1)
    await interaction.response.send_message(embed=embed)
    ephemeral=True


@bot.tree.command(name="wait", description="This Command Waits and rolls a dice!")
async def roll(interaction: discord.Interaction):
    await interaction.response.defer()  # Defer the initial response

    async with interaction.channel.typing():  # Initiate typing indicator in the channel
        await asyncio.sleep(20)  # Simulate processing time

        die_face = [
            "https://cdn.discordapp.com/attachments/1045735310350356490/1085928064300621924/Dice_Face1.png",
            "https://cdn.discordapp.com/attachments/1045735310350356490/1085928064560681071/Dice_Face2.png",
            "https://cdn.discordapp.com/attachments/1045735310350356490/1085928064770392174/Dice_Face3.png",
            "https://cdn.discordapp.com/attachments/1045735310350356490/1085928063268823131/Dice_Face4.png",
            "https://cdn.discordapp.com/attachments/1045735310350356490/1085928063570825266/Dice_Face5.png",
            "https://cdn.discordapp.com/attachments/1045735310350356490/1085928063839256647/Dice_Face6.png"
        ]
        die_num = random.randint(0, 5)
        die = die_face[die_num]

        embed = discord.Embed(color=discord.Color.dark_gold())
        embed.set_image(url=die)
        embed.set_author(name=die_num + 1)

        await interaction.followup.send(embed=embed)  # Send the final response


@bot.tree.command(name="dms", description="This Command Waits and rolls a dice!")
async def roll(interaction: discord.Interaction):
        #await interaction.response.defer(ephemeral=True)  # Defer the initial response

    # async with interaction.channel.typing():  # Initiate typing indicator in the channel
    #     await asyncio.sleep(20)  # Simulate processing time

        die_face = [
            "https://cdn.discordapp.com/attachments/1045735310350356490/1085928064300621924/Dice_Face1.png",
            "https://cdn.discordapp.com/attachments/1045735310350356490/1085928064560681071/Dice_Face2.png",
            "https://cdn.discordapp.com/attachments/1045735310350356490/1085928064770392174/Dice_Face3.png",
            "https://cdn.discordapp.com/attachments/1045735310350356490/1085928063268823131/Dice_Face4.png",
            "https://cdn.discordapp.com/attachments/1045735310350356490/1085928063570825266/Dice_Face5.png",
            "https://cdn.discordapp.com/attachments/1045735310350356490/1085928063839256647/Dice_Face6.png"
        ]
        die_num = random.randint(0, 5)
        die = die_face[die_num]

        embed = discord.Embed(color=discord.Color.colour(0X4E96D5))
        embed.set_image(url=die)
        embed.set_author(name=die_num + 1)

        if isinstance(interaction.channel, discord.DMChannel):  # Check if interaction is in a DM
            await interaction.response.send_message(embed=embed)  # Send the final response in DM
        else:
            await interaction.followup.send(embed=embed)  # Send the final response in the channel





bot.run('MTIxNDk1NTIwOTAzODQ5NTgwNw.GfnIUj.Fi_SLWJvi3dRB9LbZNlJ7F4sLfSug24j1b-lz4')
