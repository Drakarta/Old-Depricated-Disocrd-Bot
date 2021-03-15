import discord
from discord.ext import commands
import asyncio
import requests
import datetime

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def userinfo(self, ctx):
        try:
            mentioned = ctx.message.mentions[0]
        except IndexError:
            mentioned = ctx.author
        else:
            mentioned = ctx.message.mentions[0]
        Mentioned_Hex = str(mentioned.color)
        Color_API = requests.get(f"https://www.thecolorapi.com/id?hex={Mentioned_Hex[1:len(Mentioned_Hex)]}")
        Info_Embed = discord.Embed(
            title=mentioned.mention,
            description=f"Member's name: {mentioned.mention}",
            color=0xff0000)
        Info_Embed.set_author(
            name=f"{mentioned}'s userinfo.",
            icon_url=mentioned.avatar_url)
        Info_Embed.set_thumbnail(
            url=mentioned.avatar_url)
        Info_Embed.add_field(
            name=f"Member's status:",
            value=f"{mentioned.activity}",
            inline=True)
        Info_Embed.add_field(
            name=f"Member's game:",
            value=f"Error",
            inline=True)
        Info_Embed.add_field(
            name=f"Member's spotify:",
            value=f"Error",
            inline=True)
        Info_Embed.add_field(
            name=f"Member's color:",
            value=f"{Color_API.json()['name']['value']}\n{mentioned.color}",
            inline=True)
        Info_Embed.add_field(
            name=f"Joined at:",
            value=f"{mentioned.joined_at.strftime('%c [UTC]')}",
            inline=True)
        Info_Embed.add_field(
            name=f"Created at:",
            value=f"{mentioned.created_at.strftime('%c [UTC]')}",
            inline=True)
        await ctx.send(embed=Info_Embed)

    @commands.command(pass_context=True)
    async def avatar(self, ctx):
        try:
            mentioned = ctx.message.mentions[0]
        except IndexError:
            mentioned = ctx.author
        else:
            mentioned = ctx.message.mentions[0]
        Avatar_Embed = discord.Embed(
            title=f"Here is {mentioned.name}'s avatar.",
            description="",
            color=0xff0000)
        Avatar_Embed.set_image(url=mentioned.avatar_url)
        await ctx.send(embed=Avatar_Embed)

    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):
        Server_Embed = discord.Embed(
            title=f"{ctx.message.guild}'s server info.",
            description="",
            color=0xff0000)
        Bot = 0
        Members = 0
        Total_Members = 0
        for member in ctx.message.guild.members:
            if member.bot == True:
                Bot += 1
            else:
                Members += 1
            Total_Members += 1
        Server_Embed.add_field(
            name=f"Members:",
            value=f"{Total_Members}",
            inline=True)
        Server_Embed.add_field(
            name=f"Humans:",
            value=f"{Members}",
            inline=True)
        Server_Embed.add_field(
            name=f"Bots:",
            value=f"{Bot}",
            inline=True)
        Server_Embed.add_field(
            name=f"Ownership:",
            value=f"{ctx.message.guild.owner}",
            inline=True)
        Server_Embed.add_field(
            name=f"Creation date:",
            value=f"{ctx.message.guild.created_at.strftime('%c [UTC]')}",
            inline=True)
        Server_Embed.add_field(
            name=f"Region:",
            value=f"{ctx.message.guild.region}",
            inline=True)
        await ctx.send(embed=Server_Embed)

def setup(bot):
    bot.add_cog(Information(bot))