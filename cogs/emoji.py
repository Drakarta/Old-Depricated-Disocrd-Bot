import discord
from discord.ext import commands
import random

class Emoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def pat(self, ctx):
        mentioned = ctx.message.mentions[0]
        Pat_Gifs = ["https://cdn.discordapp.com/attachments/709756065339932704/715093703601029160/Pat.gif",
                    "https://cdn.discordapp.com/attachments/709756065339932704/715094573575307274/Pat2.gif",
                    "https://cdn.discordapp.com/attachments/592344619660869653/715123136961577050/Pat4.gif",
                    "https://cdn.discordapp.com/attachments/592344619660869653/715123138215542804/Pat3.gif"] 
        Pat_Embed = discord.Embed(
            title="",
            description="",
            color=0xff0000)
        Pat_Embed.set_author(
            name=f"{mentioned.name} has been patted!",
            icon_url=mentioned.avatar_url)
        Pat_Embed.set_image(url=random.choice(Pat_Gifs))
        await ctx.send(embed=Pat_Embed)
    
    @commands.command(pass_context=True)
    async def hug(self, ctx):
        mentioned = ctx.message.mentions[0]
        Hug_Gifs = ["https://cdn.discordapp.com/attachments/592344619660869653/715124176687595611/hug2.gif",
                    "https://cdn.discordapp.com/attachments/592344619660869653/715124181427159110/hug1.gif",
                    "https://cdn.discordapp.com/attachments/592344619660869653/715124183549476904/hug.gif",
                    "https://cdn.discordapp.com/attachments/592344619660869653/715124119582146670/Baka_hug101.gif"] 
        Hug_Embed = discord.Embed(
            title="",
            description="",
            color=0xff0000)
        Hug_Embed.set_author(
            name=f"{mentioned.name} has been hugged!",
            icon_url=mentioned.avatar_url)
        Hug_Embed.set_image(url=random.choice(Hug_Gifs))
        await ctx.send(embed=Hug_Embed)
        
    @commands.command(pass_context=True)
    async def kiss(self, ctx):
        mentioned = ctx.message.mentions[0]
        Kiss_Gifs = ["https://cdn.discordapp.com/attachments/712606440740749332/716575644640870480/tenor_6.gif",
                    "https://cdn.discordapp.com/attachments/712606440740749332/716575645387456512/giphy_7.gif",
                    "https://cdn.discordapp.com/attachments/712606440740749332/716575649434959913/tenor_5.gif",
                    "https://cdn.discordapp.com/attachments/712606440740749332/716575651313746002/e00f3104927ae27d7d6a32393d163176.gif"] 
        Kiss_Embed = discord.Embed(
            title="",
            description="",
            color=0xff0000)
        Kiss_Embed.set_author(
            name=f"{mentioned.name} has been kissed!",
            icon_url=mentioned.avatar_url)
        Kiss_Embed.set_image(url=random.choice(Kiss_Gifs))
        await ctx.send(embed=Kiss_Embed)

    @commands.command(pass_context=True)
    async def slap(self, ctx):
        mentioned = ctx.message.mentions[0]
        Slap_Gifs = ["https://cdn.discordapp.com/attachments/712606440740749332/716569935647735868/BAKAAA.gif",
                    "https://cdn.discordapp.com/attachments/712606440740749332/716570016018858005/Baka_xDD.gif",
                    "https://cdn.discordapp.com/attachments/712606440740749332/716570979815391262/giphy_3.gif",
                    "https://cdn.discordapp.com/attachments/712606440740749332/716570987541430332/giphy_2.gif"] 
        Slap_Embed = discord.Embed(
            title="",
            description="",
            color=0xff0000)
        Slap_Embed.set_author(
            name=f"{mentioned.name} has been slapped!",
            icon_url=mentioned.avatar_url)
        Slap_Embed.set_image(url=random.choice(Slap_Gifs))
        await ctx.send(embed=Slap_Embed)
    
    @commands.command(pass_context=True)
    async def poke(self, ctx):
        mentioned = ctx.message.mentions[0]
        Poke_Gifs = ["https://cdn.discordapp.com/attachments/712606440740749332/716572221086105620/giphy_5.gif",
                    "https://cdn.discordapp.com/attachments/712606440740749332/716572224513114112/giphy_6.gif",
                    "https://cdn.discordapp.com/attachments/712606440740749332/716572230817153074/giphy_4.gif",
                    "https://cdn.discordapp.com/attachments/712606440740749332/716573136979492924/ezgif.com-optimize.gif"]
        Poke_Embed = discord.Embed(
            title="",
            description="",
            color=0xff0000)
        Poke_Embed.set_author(
            name=f"{mentioned.name} has been poked!",
            icon_url=mentioned.avatar_url)
        Poke_Embed.set_image(url=random.choice(Poke_Gifs))
        await ctx.send(embed=Poke_Embed)
    
    @commands.command(pass_context=True)
    async def stab(self, ctx):
        mentioned = ctx.message.mentions[0]
        Stab_Gifs = ["https://cdn.discordapp.com/attachments/712606440740749332/716574242468003870/tenor_4.gif",
                    "https://cdn.discordapp.com/attachments/712606440740749332/716574267847868446/tenor_2.gif",
                    "https://cdn.discordapp.com/attachments/712606440740749332/716574270846926868/tenor_1.gif",
                    "https://cdn.discordapp.com/attachments/712606440740749332/716574273317109791/tenor_3.gif"] 
        Stab_Embed = discord.Embed(
            title="",
            description="",
            color=0xff0000)
        Stab_Embed.set_author(
            name=mentioned.name + " has been stabbed!",
            icon_url=mentioned.avatar_url)
        Stab_Embed.set_image(url=random.choice(Stab_Gifs))
        await ctx.send(embed=Stab_Embed)
    
    @commands.command(pass_context=True)
    async def blush(self, ctx):
        Blush_Gifs = ["https://cdn.discordapp.com/attachments/727423668883554355/729294502602342420/tenor.gif.cf.gif",
                    "https://cdn.discordapp.com/attachments/727423668883554355/729294502803537920/tenor.gif.cf-1.gif",
                    "https://cdn.discordapp.com/attachments/727423668883554355/729294503051264040/giphy.gif.cf.gif",
                    "https://cdn.discordapp.com/attachments/727423668883554355/729294503675953162/tenor.gif.cf-2.gif"] 
        Blush_Embed = discord.Embed(
            title="",
            description="",
            color=0xff0000)
        Blush_Embed.set_author(
            name=f"{ctx.author.name} is blushing!",
            icon_url=ctx.author.avatar_url)
        Blush_Embed.set_image(url=random.choice(Blush_Gifs))
        await ctx.send(embed=Blush_Embed)
    
    @commands.command(pass_context=True)
    async def cry(self, ctx):
        Cry_Gifs = ["https://cdn.discordapp.com/attachments/727423668883554355/729294660962353202/giphy.gif.cf-1.gif",
                    "https://cdn.discordapp.com/attachments/727423668883554355/729294661239439380/giphy.gif.cf-2.gif",
                    "https://cdn.discordapp.com/attachments/727423668883554355/729294661608538162/giphy.gif.cf-3.gif"] 
        Cry_Embed = discord.Embed(
            title="",
            description="",
            color=0xff0000)
        Cry_Embed.set_author(
            name=f"{ctx.author.name} is crying, oh no.",
            icon_url=ctx.author.avatar_url)
        Cry_Embed.set_image(url=random.choice(Cry_Gifs))
        await ctx.send(embed=Cry_Embed)
    
    @commands.command(pass_context=True)
    async def excited(self, ctx):
        Excited_Gifs = ["https://cdn.discordapp.com/attachments/727423668883554355/729294769187979324/tenor-1.gif",
                    "https://cdn.discordapp.com/attachments/727423668883554355/729294769791959090/giphy.gif.cf-5.gif",
                    "https://cdn.discordapp.com/attachments/727423668883554355/729294770530156584/happy-anime-gif-1.gif.cf.gif",
                    "https://cdn.discordapp.com/attachments/727423668883554355/729294770832277575/giphy.gif.cf-6.gif"] 
        Excited_Embed = discord.Embed(
            title="",
            description="",
            color=0xff0000)
        Excited_Embed.set_author(
            name=f"{ctx.author.name} is very excited!",
            icon_url=ctx.author.avatar_url)
        Excited_Embed.set_image(url=random.choice(Excited_Gifs))
        await ctx.send(embed=Excited_Embed)
    
    @commands.command(pass_context=True)
    async def smile(self, ctx):
        Smile_Gifs = ["https://cdn.discordapp.com/attachments/727423668883554355/729294770232623196/tenor-2.gif",
                    "https://cdn.discordapp.com/attachments/727423668883554355/729294771159433216/happy-anime-gif-14.gif.cf.gif",
                    "https://cdn.discordapp.com/attachments/727423668883554355/729294771436126228/giphy.gif.cf-7.gif",
                    "https://cdn.discordapp.com/attachments/727423668883554355/729294771692109944/giphy.gif.cf-8.gif",
                    "https://cdn.discordapp.com/attachments/727423668883554355/729294771977322547/giphy.gif.cf-9.gif"] 
        Smile_Embed = discord.Embed(
            title="",
            description="",
            color=0xff0000)
        Smile_Embed.set_author(
            name=f"{ctx.author.name} is smiling happily.",
            icon_url=ctx.author.avatar_url)
        Smile_Embed.set_image(url=random.choice(Smile_Gifs))
        await ctx.send(embed=Smile_Embed)

def setup(bot):
    bot.add_cog(Emoji(bot))