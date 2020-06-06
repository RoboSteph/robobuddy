#Connecting RoboBuddy to Discord
#Following RealPython tutorial
#Stephanie Simpler
#6-1-2020

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
#event handler
async def on_ready():
    # #loop through guilds to find the one you're looking for (only connected to one atm, but bot can connect to multiple)
    # for guild in client.guilds:
    #     if guild.name == GUILD:
    #         break

    # #using discord.utils.find() to loop through guilds (only connected to one atm, but bot can connect to multiple)
    # #"Once find() locates an element in the iterable that satisfies the predicate, it will return the element... equivalent to break but cleaner" - Real Python
    # guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)

    #get takes iterable, keyword arguments, builds predicate and passes to find()
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following server:\n'
        f'{guild.name}(id: {guild.id})'
        )

    #print guild members
    members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')

# #untested, need to make test account
# @client.event
# async def on_member_join():
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hey {member.name}, welcome to RoboStephSocial!' 
#         )

#reply to messages about self
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'robobuddy' in message.content.lower():
        await message.channel.send(
            f'Hey {message.author} :)'
            )


    

client.run(TOKEN)