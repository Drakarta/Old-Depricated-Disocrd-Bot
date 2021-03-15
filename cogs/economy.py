import discord
from discord.ext import commands
import asyncio
import random
import json
from datetime import datetime
import threading

Currency_Name = "Tokens"

def Read_Json():
    with open("./Json/Data.json", "r") as f:
        Data = json.load(f)
        return Data

def Write_Json(Data):
    with open("./Json/Data.json", "w") as f:
        json.dump(Data, f, indent=4)

def Check_ID(ID):
    Data = Read_Json()
    if str(ID) not in Data:
        Data[ID] = {
            "Money": 0
        }
        Write_Json(Data)

def checkTime():
    threading.Timer(1, checkTime).start()
    now = datetime.utcnow()
    current_time = now.strftime("%H:%M:%S")
    if(current_time == "08:00:00"):
        Daily = {"Done" : []}
        with open("./Json/Daily.json", "w") as f:
            json.dump(Daily, f, indent=4)

checkTime()

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def balance(self, ctx):
        Check_ID(ctx.author.id)
        await ctx.send(f"{ctx.author.mention}'s has {Read_Json()[str(ctx.author.id)]['Money']} {Currency_Name}.")
    
    @commands.command(pass_context=True)
    async def bal(self, ctx):
        Check_ID(ctx.author.id)
        await ctx.send(f"{ctx.author.mention}'s has {Read_Json()[str(ctx.author.id)]['Money']} {Currency_Name}.")

    @commands.command(pass_context=True)
    async def pay(self, ctx):
        Check_ID(ctx.author.id)
        mentioned = ctx.message.mentions[0]
        Check_ID(str(mentioned.id))
        Amount = int(ctx.message.content.split(" ")[2])
        Data = Read_Json()
        if Data[str(ctx.author.id)]["Money"] >= Amount:
            Data[str(ctx.author.id)]["Money"] -= Amount
            Data[str(mentioned.id)]["Money"] += Amount
            Write_Json(Data)
            await ctx.send(f"{ctx.author.mention} payed {mentioned.mention} {Amount} {Currency_Name}")
        else:
            await ctx.send(f"Not enough {Currency_Name}")
    
    @commands.command(pass_context=True)
    async def daily(self, ctx):
        Check_ID(ctx.author.id)
        with open("./Json/Daily.json", "r") as f:
            Daily = json.load(f)
            if str(ctx.author.id) not in Daily["Done"]:
                Data = Read_Json()
                Data[str(ctx.author.id)]["Money"] += 10
                Write_Json(Data)
                with open("./Json/Daily.json", "w") as f:
                    Daily["Done"].append(str(ctx.author.id))
                    json.dump(Daily, f, indent=4)
                await ctx.send(f"You claimed the daily reward of 10 {Currency_Name}.")
            else:
                await ctx.send(f"You already claimed the daily reward today.")

    @commands.command(pass_context=True)
    async def coinflip(self,ctx):
        Check_ID(ctx.author.id)
        Data = Read_Json()
        Choice = str(ctx.message.content.split(" ")[1])
        Amount = int(ctx.message.content.split(" ")[2])
        if Data[str(ctx.author.id)]["Money"] >= Amount:
            CF = random.choice(["heads", "tails"])
            Data[str(ctx.author.id)]["Money"] -= Amount
            if Choice in ["head", "heads", "h"]:
                if CF == "heads":
                    await ctx.send(f"Bot rolled {CF}\nYou win!")
                    Data[str(ctx.author.id)]["Money"] += 2 * Amount
                    Write_Json(Data)
                else:
                    await ctx.send(f"Bot rolled {CF}\nYou lose!")
            elif Choice in ["tail", "tails","t"]:
                if CF == "tails":
                    await ctx.send(f"Bot rolled {CF}\nYou win!")
                    Data[str(ctx.author.id)]["Money"] += 2 * Amount
                    Write_Json(Data)
                else:
                    await ctx.send(f"Bot rolled {CF}\nYou lose!")
        else:
            await ctx.send(f"You dont have enough to coinflip {Amount} Tokens.")

    @commands.command(pass_context=True)
    async def cf(self,ctx):
        Check_ID(ctx.author.id)
        Data = Read_Json()
        Choice = str(ctx.message.content.split(" ")[1])
        Amount = int(ctx.message.content.split(" ")[2])
        if Data[str(ctx.author.id)]["Money"] >= Amount:
            CF = random.choice(["heads", "tails"])
            Data[str(ctx.author.id)]["Money"] -= Amount
            if Choice in ["head", "heads", "h"]:
                if CF == "heads":
                    await ctx.send(f"Bot rolled {CF}\nYou win!")
                    Data[str(ctx.author.id)]["Money"] += 2 * Amount
                    Write_Json(Data)
                else:
                    await ctx.send(f"Bot rolled {CF}\nYou lose!")
            elif Choice in ["tail", "tails","t"]:
                if CF == "tails":
                    await ctx.send(f"Bot rolled {CF}\nYou win!")
                    Data[str(ctx.author.id)]["Money"] += 2 * Amount
                    Write_Json(Data)
                else:
                    await ctx.send(f"Bot rolled {CF}\nYou lose!")
        else:
            await ctx.send(f"You dont have enough to coinflip {Amount} Tokens.")

def setup(bot):
    bot.add_cog(Economy(bot))