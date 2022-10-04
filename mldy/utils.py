import DiscordUtils
import discord
from discord import client
import aiohttp
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import command

class Utils(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        lct=round(self.bot.latency* 1000)
        embedp1=discord.Embed(title = f"**<a:pong:884713759925497886> Pong!:  **{round(self.bot.latency* 1000)}ms",colour = discord.Colour.green())
        embedp2=discord.Embed(title = f"**<a:pong:884713759925497886> Pong!:  **{round(self.bot.latency* 1000)}ms",colour = discord.Colour.orange())
        embedp3=discord.Embed(title = f"**<a:pong:884713759925497886> Pong!:  **{round(self.bot.latency* 1000)}ms",colour = discord.Colour.red())
        embedp4=discord.Embed(title = f"**<a:pong:884713759925497886> Pong!:  **{round(self.bot.latency* 1000)}ms",colour = discord.Colour.dark_grey())
        embedp5=discord.Embed(title = f"**<a:pong:884713759925497886> Pong!:  **{round(self.bot.latency* 1000)}ms",colour = discord.Colour(0x000000))



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

    @commands.group(invoke_without_command = True,aliases=["hlp"])
    async def help(self,ctx):
        embed = discord.Embed(title = "Melody Help",description="`<required>`",colour = discord.Colour.blurple())
        embed.add_field(name = "Prefix",value="**m-**",inline=False)
        #embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/868526178586226691/885561358437978212/rect54.png?width=663&height=663")
        embed.add_field(name = "Music Commands",value=f'`connect` , `play <song name>` , `queue` , `pause` , `resume`, `disconnect`,`lyrics<song name>`, `volume <0-100>` , `np` , `stop`',inline=False)
        embed.add_field(name = "Utility",value=f'`ping` , `purge<no. of messages>`',inline=False)
        embed.add_field(name = "*Dev Stage*",value=f'`Pre-Alpha`',inline=False)
        embed.set_footer(text = "Melody, made by VulcanB_#7408 || Dev of Sentinel",icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx,amount=2):
        await ctx.channel.purge(limit=amount)

    @commands.command(aliases=["?","use"])
    async def how(self,ctx,*,arg):
      if arg== "to use":
        embed = discord.Embed(title = "Melody || How To Use",colour = discord.Colour.blurple())
        embed.add_field(name = "Step I",value="*m-join*",inline=False)
        embed.add_field(name = "Step II",value="*m-play <Song Name>*",inline=False)
        embed.add_field(name = "Step IIIa",value="if you want to stop half way *m-stop*",inline=False)
        embed.add_field(name = "Step IIIb",value="after stopping or music is over *m-disconnet*",inline=False)
        embed.add_field(name = "Note",value="Do not m-disconnect while the song is being played",inline=False)
        await ctx.send(embed=embed)
      else:
        await ctx.send("Did you mean m-how to use")
        

    @commands.command()
    async def example(self,ctx):
        embed1 = discord.Embed(color=discord.Colour.blurple()).add_field(name="Step 1", value="m-join")
        embed2 = discord.Embed(color=discord.Colour.gold()).add_field(name="Step 2", value="m-play SongNameGoesHere")
        embed3 = discord.Embed(color=discord.Colour.blurple()).add_field(name="Step 3 (if you want to quit in mid way)", value="m-stop")
        embed4 = discord.Embed(color=discord.Colour.gold()).add_field(name="Step 4", value="m-leave")
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('⏩', "next")
        embeds = [embed1, embed2, embed3, embed4]
        await paginator.run(embeds)

    @commands.command(name="emojiinfo", aliases=["ei","emoteinfo"])
    async def emojiid(self, ctx, emoji: discord.Emoji = None):

        emoji = await emoji.guild.fetch_emoji(emoji.id)
        desp = f'''
        **Emote Name:** {emoji.name}
        **Id:** {emoji.id}
        **Animated:** {emoji.animated}
        '''
        embed = discord.Embed(
            title=f"**Emoji Information for:** `{emoji.name}`",
            description=desp,
            colour=0xADD8E6,
        )
        embed.set_thumbnail(url=emoji.url)
        await ctx.send(embed=embed)

#0x2f3136

def setup(bot):
    bot.add_cog(Utils(bot))