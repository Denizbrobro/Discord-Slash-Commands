import discord
from discord.ext import commands
from discord.interactions import Interaction

#intents
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

#codes

@bot.tree.command(name="ping", description="bla bla")
async def ping(interaction: discord.Interaction):
    interaction.response.send_message("Pong!")

@bot.tree.command(
        name="ping2",
        description="bla bla2"
        )
async def ping(interaction: discord.Interaction):
    interaction.response.send_message("Pong2!")

#events
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="/help"))
    try:
        synced = await bot.tree.sync()
        print(f"Currently, there are {len(synced)} executable commands.")
    except Exception as e:
        print("There is an issue with the bot. Please check the bot. Urgent.", e)

bot.run("Your bot token here")
