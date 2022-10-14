#NOTE INSTALL PycordUtils 
from PycordUtils.Music import EmptyQueue
import discord
from discord import embeds
from discord.embeds import Embed
from discord.ext import commands
import aiohttp
import asyncio
import PycordUtils
#music= PycordUtils.Music()

class music(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
        self.music = PycordUtils.Music()
    
    #join
    @commands.slash_command(name="join",description="Joins VC")
    async def join(self,ctx):
      ec=discord.Embed(title=f"Connected :white_check_mark: ",colour = discord.Colour.green())
      #ec.set_footer(text = "Please check m-how to use",icon_url=self.bot.user.avatar.url)
      ece=discord.Embed(title=f":bangbang: Please join a VC first. ",colour = discord.Colour.light_grey())
      if ctx.author.voice is None:
        await ctx.send(embed=ece)
      voice_channel = ctx.author.voice.channel
      if ctx.voice_client is None:
        await voice_channel.connect()
        c=await ctx.send(embed=ec)
        await c.add_reaction('🆗')
      else:
        await ctx.voice_client.move_to(voice_channel)
        c1=await ctx.send(embed=ec)
        await c1.add_reaction('🆗')


    @commands.slash_command(name="leave", description="Leaves VC")
    async def leave(self,ctx):
      dccc=discord.Embed(title=f"{self.bot.user} Disconnected :white_check_mark: ",colour = discord.Colour.green())
      await ctx.guild.voice_client.disconnect()
      dc= await ctx.send (embed=dccc)
      await dc.add_reaction('🆗')

    #leave
    @commands.slash_command(name="disconnect",description="Disconnect VC")
    async def disconnect(self,ctx):
      ece=discord.Embed(title=f":bangbang: You aren't connected to a VC ",colour = discord.Colour.light_grey())
      ece1=discord.Embed(title=f":bangbang: I am not connected to a VC right now",colour = discord.Colour.light_grey())
      if ctx.author.voice is None:
        dc1=await ctx.send(embed=ece)
        await dc1.add_reaction('❌')
      if ctx.guild.me.voice is None:
        dc2=await ctx.send(embed=ece1)
        await dc2.add_reaction('❌')
      edc=discord.Embed(title=f"{self.bot.user} Disconnected :white_check_mark: ",colour = discord.Colour.green())
      #player = music.get_player(guild_id=ctx.guild.id)
     
      await asyncio.sleep(1)
      await ctx.guild.voice_client.disconnect()
      dc = await ctx.send(embed=edc)
      await dc.add_reaction('🆗')
        
    @commands.slash_command(name="play",description="Plays song in VC")
    async def play(self,ctx, *, url):
        player = music.get_player(guild_id=ctx.guild.id)
        if not player:
            player = music.create_player(ctx, ffmpeg_error_betterfix=True)
        if not ctx.voice_client.is_playing():
            await player.queue(url, search=True)
            song = await player.play()
            await ctx.send(f"Playing {song.name}")
        else:
            song = await player.queue(url, search=True)
            await ctx.send(f"Queued {song.name}")
    
    

    #Queue
    @commands.command(aliases=["q"])
    async def queue(self,ctx):
      player = music.get_player(guild_id=ctx.guild.id)
      x="\n"
      qu=x.join([song.name for song in player.current_queue()])
      equ=discord.Embed(title=f"{ctx.guild.name} Queue:",description=f"**{qu}**",colour = discord.Colour.dark_green())
      #equ.set_thumbnail(url=)
 
      await ctx.send(embed=equ)

    @commands.command(aliases=[])
    async def pause(self,ctx):
      player = music.get_player(guild_id=ctx.guild.id)
      song = await player.pause()
      pu = await ctx.send(f'Paused `{song.name}`')
      await pu.add_reaction('⏸️') 

    @commands.command(aliases=[])
    async def resume(self,ctx):
      player = music.get_player(guild_id=ctx.guild.id)
      song = await player.resume()
      rm = await ctx.send(f'Resumed `{song.name}`')
      await rm.add_reaction('▶️')

    @commands.command(aliases=["now"])
    async def np(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        try:
          song = player.now_playing()
        
          enp=discord.Embed(title=f"Now Playing:",description=f"**{song.name}**",colour = discord.Colour.blurple())
 
          await ctx.send(embed=enp)
        except AttributeError:
          await ctx.send("Melody not in use right now.")

    @commands.command()
    async def stop(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.stop()
        es=discord.Embed(title=f"Stopped playing the song",colour = discord.Colour.orange())
       
        st=await ctx.send(embed=es)
        await st.add_reaction('⏹️')
        
        #await ctx.send(f"Stopped {song.name}")

    @commands.command()
    async def skip(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.skip()
        s1 = await ctx.send(f"Skipped")
        s2 = await ctx.send(f"Skipped {song.name}")
        await s1.add_reaction('⏭️')
        await s2.add_reaction('⏭️')
        

    @commands.command(aliases=["vol"])
    async def volume(self, ctx, vol):
    
        player = music.get_player(guild_id=ctx.guild.id)
        song, volume = await player.change_volume(float(vol) / 100) 
        
        if vol=="100":
          volx="<:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318>"
        elif vol>="90" and vol<="99":
          volx="<:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolN:893103348830568458>"
        elif vol>="80" and vol<="89":
          volx="<:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolN:893103348830568458><:VolN:893103348830568458>"
        elif vol>="70" and vol<="79":
          volx="<:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458>"
        elif vol>="60" and vol<="69":
          volx="<:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458>"
        elif vol>="50" and vol<="59":
          volx="<:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458>"
        elif vol>="40" and vol<="49":
          volx="<:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458>"
        elif vol>="30" and vol<="39":
          volx="<:VolY:893103348901900318><:VolY:893103348901900318><:VolY:893103348901900318><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458>"
        elif vol>="20" and vol<="29":
          volx="<:VolY:893103348901900318><:VolY:893103348901900318><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458>"
        elif vol>="10" and vol<="19":
          volx="<:VolY:893103348901900318><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458>"
        #elif vol>="0" and vol<="9":
        else:
          volx="<:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458><:VolN:893103348830568458>"
        evol=discord.Embed(title=f"Volume is now set at {volume*100}%",description=volx,colour = discord.Colour.purple())
        snd = await ctx.send(embed=evol)
        await snd.add_reaction('🔉')
        #await ctx.send(f"Volume is now set at{volume*100}%")


    @commands.command(aliases=["lyr","lyrics","lyric"])
    async def lyrc(self,ctx,*,ly):
      await ctx.trigger_typing()
      msg1=await ctx.send("Lyrics API might be down")
      async with aiohttp.ClientSession() as sesm:
            async with sesm.get(f"https://some-random-api.ml/lyrics?title={ly}") as ly1:
                lydata=await ly1.json()
                lyr=lydata["lyrics"]
                title=lydata["title"]
                auth=lydata["author"]
                img1=lydata["thumbnail"]["genius"]
                lyl=lydata["links"]["genius"]
                x= discord.Colour.gold or discord.Colour.blurple 
                embed = discord.Embed(title = f"{title} || {auth}",description = f'{lyr}',url=f"{lyl}" ,colour = x())
                embed.set_thumbnail(url=f'{img1}')
                #embed.set_footer(text =f"{title} lyrics requested by: {ctx.message.author}",icon_url=ctx.author.avatar_url)
                await msg1.delete()
                lyr = await ctx.send(embed=embed)
                await lyr.add_reaction('✅')


def setup(bot):
  bot.add_cog(Song(bot))
