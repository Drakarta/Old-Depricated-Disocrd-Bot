import discord
from discord.ext import commands
import asyncio
import json

with open("Json/Token.json", "r") as Json:
    Token = json.load(Json)["Token"]
    Prefix = "~"

bot = commands.Bot(command_prefix="~", case_insensitive=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f"{bot.user} has connected.\nWith the prefix of \" {Prefix} \"")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="with my box."))

bot.load_extension("cogs.help")
bot.load_extension("cogs.information")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.economy")
bot.load_extension("cogs.emoji")
bot.load_extension("cogs.admin")

bot.run(Token)
