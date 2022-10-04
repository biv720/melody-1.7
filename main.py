import os
import discord
from discord.ext import commands
import jishaku
from asyncio import sleep

def main():
    intents = discord.Intents.all()
    

    melodyprefix=("m-","M-")
    bot = commands.Bot(command_prefix= commands.when_mentioned_or('m-'), intents = discord.Intents.all())
    bot.remove_command('help')
    
   
    token ="Insert Token"

    @bot.event
    async def Status():
        while True:
            await bot.wait_until_ready()
            await bot.change_presence(activity=discord.Game(name="some tunes"))
            await sleep(6)
            await bot.change_presence(activity=discord.Game(name="Server DJ | m-help"))
            await sleep(6)
    bot.loop.create_task(Status())




        
    
    for filename in os.listdir('./mldy'):
        if filename.endswith('.py'):
            bot.load_extension(f'mldy.{filename[:-3]}')
    
    bot.load_extension('jishaku')
    
    

    


    bot.run(token)

if __name__ == '__main__':
    main()
