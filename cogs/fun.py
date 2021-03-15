import discord
from discord.ext import commands
import random
import requests
from cogs.Modules import SomeSecretCode

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def code(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"{ctx.author.mention}: ``{SomeSecretCode.SomeSecretCode(ctx.message.content[6:len(ctx.message.content)])}``")

    @commands.command(pass_context=True)
    async def ask(self, ctx):
        Ball_Answers = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definetly.", "You may rely on it.", "As i see it, yes.", "Most likely.", "Outlook good.", "Yes.", "signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        _8Ball = discord.Embed(
        title="", 
        description=f"**{ctx.author.mention} asked:** {ctx.message.content[4:len(ctx.message.content)]}\n**<@686500531979419669> answered:** {random.choice(Ball_Answers)}",
        color=0xff0000)
        await ctx.send(embed=_8Ball)

    @commands.command(pass_context=True)
    async def rpc(self, ctx):
        Choices = ["rock", "paper", "scissors"]
        await ctx.send(f"Rock, paper, scissors shoot!")
        def check(m):
            return m.author == ctx.author and m.content.lower() in Choices
        msg = await self.bot.wait_for("message", timeout=60, check=check)
        user = msg.content
        cpu = random.choice(Choices)
        await ctx.send(f"{cpu}")
        if user.lower() == cpu:
            await ctx.send("Draw")
        elif user.lower() == "rock":
            if cpu == "paper":
                await ctx.send("Lose")
            elif cpu == "scissors":
                await ctx.send("Win")
        elif user.lower() == "paper":
            if cpu == "rock":
                await ctx.send("Win")
            elif cpu == "scissors":
                await ctx.send("Lose")
        elif user.lower() == "scissors":
            if cpu == "rock":
                await ctx.send("Lose")
            elif cpu == "paper":
                await ctx.send("Win")

    @commands.command(pass_context=True)
    async def meme(self, ctx):
        Meme_Embed_Title = ["Here is your Meme!", "Meme is ready!", "I reveal you the meme!"]
        Meme_API = requests.get(f"https://meme-api.herokuapp.com/gimme")
        Meme = Meme_API.json()
        Meme_Embed = discord.Embed(
                    title=f"{random.choice(Meme_Embed_Title)}",
                    description="",
                    color=0xff0000)
        Meme_Embed.set_image(url=Meme["url"])
        await ctx.send(embed=Meme_Embed)

    @commands.command(pass_context=True)
    async def quote(self, ctx):
        Quote_API = requests.get(f"https://inspirobot.me/api?generate=true")
        Quote = Quote_API.text
        Quote_Embed = discord.Embed(
            title=f"Here is your quote.",
            description="",
            color=0xff0000)
        Quote_Embed.set_image(url=Quote)
        await ctx.send(embed=Quote_Embed)

def setup(bot):
    bot.add_cog(Fun(bot))