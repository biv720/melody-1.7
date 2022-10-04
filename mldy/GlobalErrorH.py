import discord
import traceback
import sys
from discord.ext import commands
from yarl import URL



class GlobalErrorH(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            ecl=discord.Embed(title = f"** You don't have permission to use this command :angry: **",colour = discord.Colour.red())
            await ctx.send(embed = ecl,delete_after = 30)

        if isinstance(error, commands.MissingRequiredArgument):
            ecl=discord.Embed(title = f"** Please pass in all reqd arguments :pleading_face:  **",colour = discord.Colour.red())
            await ctx.send(embed = ecl,delete_after = 30)

        if isinstance(error, commands.CommandNotFound):
            ecl=discord.Embed(title = f"<:nah:885722102945165362> ** This command doesn't exits. Please check the command  **",description='If you think this is a mistake,please drop a message in support server' '\n' '[**[Sentinel Support Server]**](https://discord.com/api/oauth2/authorize?client_id=868347503714635836&permissions=536836832375&scope=bot)',colour = discord.Colour.red())
            await ctx.send(embed = ecl,delete_after = 30)

        



    


def setup(bot):
    bot.add_cog(GlobalErrorH(bot))
