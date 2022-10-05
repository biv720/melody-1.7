from discord.ext import commands
from discord.commands import SlashCommandGroup
import discord

intents = discord.Intents.default()
intents.members = True

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.slash_command(name="tria2")
    async def work1(self,ctx):
        await ctx.respond("yep, works1")

    @commands.slash_command(name="ping",description="Return the ping of bot")
    async def ping(self, ctx):
        lct1=round(self.bot.latency* 1000)
        embedp1=discord.Embed(title = f"**<a:pong:884713759925497886> Pong!:  **{round(self.bot.latency* 1000)}ms",colour = discord.Colour.green())
        embedp2=discord.Embed(title = f"**<a:pong:884713759925497886> Pong!:  **{round(self.bot.latency* 1000)}ms",colour = discord.Colour.orange())
        embedp3=discord.Embed(title = f"**<a:pong:884713759925497886> Pong!:  **{round(self.bot.latency* 1000)}ms",colour = discord.Colour.red())
        embedp4=discord.Embed(title = f"**<a:pong:884713759925497886> Pong!:  **{round(self.bot.latency* 1000)}ms",colour = discord.Colour.dark_grey())
        embedp5=discord.Embed(title = f"**<a:pong:884713759925497886> Pong!:  **{round(self.bot.latency* 1000)}ms",colour = discord.Colour(0x000000))


        lct=int(lct1)
        if lct<=75:
            await ctx.send(embed=embedp1)
        elif lct>=76 and lct<=200:
            await ctx.send(embed=embedp2)
        elif lct>=201 and lct<=300:
            await ctx.send(embed=embedp3)
        elif lct>=301 and lct<=500:
            await ctx.send(embed=embedp4)
        else:
            lct>=501
            await ctx.send(embed=embedp5)

    @commands.slash_command(name="help",description="Get all commands/info")
    async def help(self,ctx):
        emh=discord.Embed(title= "Melody Help", description="`<reqd>` || Prefix: Slash",color=discord.Colour.brand_green())
        emh.add_field(name = "Music Commands",value=f'`connect` , `play <song name>` , `queue` , `pause` , `resume`, `disconnect`,`lyrics<song name>`, `volume <0-100>` , `np` , `stop`',inline=False)
        emh.add_field(name = "Utility",value=f'`ping` , `purge<no. of messages>`',inline=False)
        emh.add_field(name = "*Dev Stage*",value=f'`Pre-Alpha`',inline=False)
        emh.set_footer(text = "Melody, made by VulcanB_#7408",icon_url=self.bot.user.avatar.url)        
        await ctx.send(embed=emh)

    @commands.slash_command(name="purge", description="deletes X number of messages")
    @commands.has_permissions(manage_messages=True)
    async def purge(self,ctx,amt=2):
        amt1=int(amt)
        purged=await ctx.channel.purge(limit=amt1)
        await ctx.send(f"Purged {len(purged)} messages",delete_after = 30)

def setup(bot):
    bot.add_cog(Utils(bot))        
