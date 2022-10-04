import discord 
import traceback
import sys
from discord.ext import commands


class events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        ej=discord.Embed(title=f"{self.bot.user} Connected <:on1:888045240466952203>",colour = discord.Colour.green())
        channel = self.bot.get_channel(885033186109820968)
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))
        await self.bot.wait_until_ready()
        print(f'{self.bot.user} has Connected Successfully! | Available on {serverCount} servers and utilized by {memberCount} members' )
        await channel.send(embed=ej)

    
        
    @commands.Cog.listener()
    async def on_connect(self):
        channel = self.bot.get_channel(885033186109820968)
        print("Connected!")
        await channel.send(":white_check_mark: Checked and Connected!")


    @commands.Cog.listener()
    async def on_resumed(self):
        channel = self.bot.get_channel(885033186109820968)
        ej=discord.Embed(title=f"{self.bot.user} Reconnected 🔁",colour = discord.Colour.gold())
        print("Reconnected!")
        await channel.send(embed=ej)


    @commands.Cog.listener()
    async def on_disconnect(self):
        ej=discord.Embed(title=f"{self.bot.user} Disconnected <:off1:888045130467143711>",colour = discord.Colour.light_gray())
        channel = self.bot.get_channel(885033186109820968)
        print("Disconnected!")
        await channel.send(embed=ej)


    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        channel1 = self.bot.get_channel(885555470046220289)
        ej=discord.Embed(title=f"Hey! I am {self.bot.user}",colour = discord.Colour.gold(),description='use s-help to know more about me')
        ej.set_thumbnail(url=f"{self.bot.user.avatar_url}")
        ej.add_field(name='Invite Me', value=f"**|**" '[**Click Here**](https://discord.com/api/oauth2/authorize?client_id=868347503714635836&permissions=534722903287&scope=bot%20applications.commands)' "**|**")
        ej.set_footer(icon_url=f"{self.bot.user.avatar_url}", text=f"A Bot By: VulcanB_#7777")
        ej2=discord.Embed(title=f"Joined {guild.name}!",description=f"{self.bot.user} was invited to {guild.name}",colour = discord.Colour.gold())
        ej2.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/886966528115871824/886967263310282783/rect68.png") #https://cdn.discordapp.com/attachments/886966528115871824/886967263310282783/rect68.png
        await channel1.send(embed=ej2)
        print(f"I joined a server || Server Name: {guild.name}")
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send(embed=ej)
                print(f"I joined a server || {guild.name}")
                break


    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        channel = self.bot.get_channel(885555470046220289)
        ej=discord.Embed(title=f"Left {guild.name}!",description=f"{self.bot.user} was removed from {guild.name}",colour = discord.Colour.dark_gold())
        ej.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/886966528115871824/886967265717813308/recst68.png")
        await channel.send(embed=ej)
        print(f"I was removed from a server || {guild.name}")


    
def setup(bot):
    bot.add_cog(events(bot))
