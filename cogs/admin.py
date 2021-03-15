import discord
from discord.ext import commands
import asyncio

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    

def setup(bot):
    bot.add_cog(Admin(bot))