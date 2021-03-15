import discord
from discord.ext import commands
import asyncio

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#    @commands.Cog.listener()
#    async def on_member_join(self, member):
#        guild = member.guild
#        channel = guild.get_channel(753682143758254195)
#        Welcome_Embed = discord.Embed(#
#            title="Welcome to Mythical!",
#            description="We welcome " + member.mention + " to " + guild.name + "!",
#            color=0xff0000)
#        Welcome_Embed.set_author(
#            name=member.name + " has joined the server!",
#            icon_url=member.avatar_url)
#        Welcome_Embed.set_image(
#            url="https://cdn.discordapp.com/attachments/592344619660869653/716271673036505178/ezgif.com-crop.gif")
#        await channel.send(embed=Welcome_Embed)

    @commands.command(pass_context=True)
    async def help(self, ctx):
        Help_Title = discord.Embed(
            title="Help menu",
            description="Pandora's Help menu",
            color=0xff0000)
        Help_Title.set_footer(text="[Note: The prefix is the tilde key.]")
        await ctx.send(embed=Help_Title)
        Help_Tot = 6
        Help_Cur = 1
        Help_General = discord.Embed(
            title="Help menu - General", 
            description="**~Help [**Gets this Help menu.**]**\n",
            color=0xff0000)
        Help_General.set_footer(text=f"[1/{Help_Tot} - General]")
        Help_Information = discord.Embed(
            title="Help menu - Information", 
            description="**~ServerInfo [**Get server info.**]**\n" +
                        "**~UserInfo [**Get user info.**]**\n" +
                        "**~Avatar [**Get profile pic of someone.**]**\n" +
                        "\n" + 
                        "**Usage: [**~Avatar <@mention>",
            color=0xff0000)
        Help_Information.set_footer(text=f"[2/{Help_Tot} - Information]")
        Help_Emoji = discord.Embed(
            title="Help menu - Emoji", 
            description="**Actions**\n"
                        "**~Pat [**Pat someone.**]**\n" +
                        "**~Hug [**Hug someone.**]**\n" +
                        "**~Kiss [**Kiss someone.**]**\n" +
                        "**~Slap [**Slap someone.**]**\n" +
                        "**~Poke [**Poke someone.**]**\n" +
                        "**~Stab [**Stab someone.**]**\n" +
                        "\n" +
                        "**Emotions**\n" +
                        "**~Blush [**You are blushing.**]**\n" +
                        "**~Cry [**You are crying.**]**\n" +
                        "**~Excited [**You are excited.**]**\n" +
                        "**~Smile [**You are smiling.**]**\n" +
                        "**~Angry [**You are angry.**(Soon)]**\n",
            color=0xff0000)
        Help_Emoji.set_footer(text=f"[3/{Help_Tot} - Emoji]")
        Help_Fun = discord.Embed(
            title="Help menu - Fun", 
            description="**~Code [**Encode/decode a message**]**\n" +
                        "**~Ask [**Ask me anything.**]**\n" +
                        "**~RPC [**Rock, Paper, Scissors. **]**\n" +
                        "**~Meme [**Generates a meme.**]**\n" +
                        "**~Quote [**Generates a quote**]**\n",
            color=0xff0000)
        Help_Fun.set_footer(text=f"[4/{Help_Tot} - Fun]")
        Help_Economy = discord.Embed(
            title="Help menu - Economy **(soon)**",
            description="**~Balance [**Check your balance**]**\n" +
                        "**~Pay [**Pay someone cash**]**\n" +
                        "**~Daily [**Recieve a daily reward resets at 08:00 [UTC].**]**\n" +
                        "\n" +
                        "**Gambling**\n" +
                        "**~CoinFlip [**~CF [H/T] [Amount]**]**\n" +
                        "\n" +
                        "**Usage: [**~Pay <@mention> <amount>**]**",
            color=0xff0000)
        Help_Economy.set_footer(text=f"[5/{Help_Tot} - Economy]")
        Help_Admin = discord.Embed(
            title="Help menu - Admin **(soon)**", 
            description="**~Ban [**Ban someone.**]**\n" + 
                        "**~Kick [**Kick someone.**]**\n" +
                        "**~Mute [**Mute someone.**]**\n" +
                        "**~Unmute [**Unmute someone**]**\n" + 
                        "\n" +
                        "**Usage: [**~Ban <@mention> <Reason>**]**",
            color=0xff0000)
        Help_Admin.set_footer(text=f"[6/{Help_Tot} - Admin]")
        Help_Pages = [Help_General, Help_Information, Help_Emoji, Help_Fun, Help_Economy, Help_Admin]
        Send_Help = await ctx.send(embed=Help_Pages[Help_Cur-1])
        await Send_Help.add_reaction("⏹️")
        await Send_Help.add_reaction("▶️")
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)
                if str(reaction.emoji) == "▶️" and Help_Cur != Help_Tot:
                    Help_Cur += 1
                    await Send_Help.edit(embed=Help_Pages[Help_Cur-1])
                    await Send_Help.clear_reactions()
                    if Help_Cur == 1:
                        await Send_Help.add_reaction("⏹️")
                        await Send_Help.add_reaction("▶️")
                    elif Help_Cur == Help_Tot:
                        await Send_Help.add_reaction("◀️")
                        await Send_Help.add_reaction("⏹️")
                    else:
                        await Send_Help.add_reaction("◀️")
                        await Send_Help.add_reaction("▶️")
                elif str(reaction.emoji) == "◀️" and Help_Cur > 1:
                    Help_Cur -= 1
                    await Send_Help.edit(embed=Help_Pages[Help_Cur-1])
                    await Send_Help.clear_reactions()
                    if Help_Cur == 1:
                        await Send_Help.add_reaction("⏹️")
                        await Send_Help.add_reaction("▶️")
                    elif Help_Cur == Help_Tot:
                        await Send_Help.add_reaction("◀️")
                        await Send_Help.add_reaction("⏹️")
                    else:
                        await Send_Help.add_reaction("◀️")
                        await Send_Help.add_reaction("▶️")
                else:
                    await Send_Help.remove_reaction(reaction, user)
            except asyncio.TimeoutError:
                await Send_Help.clear_reactions()
                break

def setup(bot):
    bot.add_cog(Help(bot))