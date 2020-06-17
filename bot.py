#Connecting RoboBuddy to Discord
#Following RealPython tutorial
#Stephanie Simpler
#6-1-2020
#Note: Dont forget to add back in responding to name 
#Tried banner but it is 'empty' can't find setting for it in Discord

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#client = discord.Client()

#converting our bot.py to use a bot instead of client
bot = commands.Bot(command_prefix='!')
# guild = discord.utils.get(bot.guilds, name=GUILD)


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user.name} has connected to Discord!\n'
        f'{guild.name}(id: {guild.id})'
        )

@bot.command(name='channels', help='Lists all channels in this server', aliases=['channel'])
#"any command function must accept at least one parameter called ctx.. context.. holds data such as channel and guild the user called the command from"-RealPython
async def list_channels(ctx):
    guild = discord.utils.get(bot.guilds, name=GUILD)
    
    guild_channels = guild.channels
    list_of_channel_ids = []

    #I would like to find a better way to do this that also prints the category names 
    #voice channel is not a link but all text channels are
    for n in guild_channels:
        print(f'{n.name} {n.type}, ')
        if str(n.type) == 'text' or str(n.type) == 'voice':
            list_of_channel_ids.append('<#' + str(n.id) + '>')

    list_of_channel_ids = ' \n'.join(list_of_channel_ids)


    response = 'Here are links to all of our channels: \n' + list_of_channel_ids
    print(list_of_channel_ids)

    await ctx.send(response)

@bot.command(name='emojis', help='Shows all emojis for our server', aliases=['emoji', 'emote', 'emotes'])
async def show_emojis(ctx):
    print("showing emojis...")
    guild = discord.utils.get(bot.guilds, name=GUILD)

    emoji_info = []
    for e in guild.emojis:
        emoji_info.append('<:' + e.name + ':' + str(e.id) + '>')

    emoji_info_joined = ' '.join(emoji_info)

    print(emoji_info_joined)
    response = emoji_info_joined
    await ctx.send(response)

#creating a roll command defining a Converter using function annotations - converts command arguments to int. Decided to add defaults too
@bot.command(name='roll', help='Roll a dice. Type !roll <number_of_dice> <number_of_sides> or !roll for one six-sided die')
async def roll_dice(ctx, number_of_dice: int = 1, number_of_sides: int = 6):

    dice = [
        str(random.choice(range(1, number_of_sides +1)))
        for _ in range(number_of_dice)
        ]
    
    await ctx.send(', '.join(dice))


# @client.event
# #event handler
# async def on_ready():
#     # #loop through guilds to find the one you're looking for (only connected to one atm, but bot can connect to multiple)
#     # for guild in client.guilds:
#     #     if guild.name == GUILD:
#     #         break

#     # #using discord.utils.find() to loop through guilds (only connected to one atm, but bot can connect to multiple)
#     # #"Once find() locates an element in the iterable that satisfies the predicate, it will return the element... equivalent to break but cleaner" - Real Python
#     # guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)

#     #get takes iterable, keyword arguments, builds predicate and passes to find()
#     guild = discord.utils.get(client.guilds, name=GUILD)

#     print(
#         f'{client.user} is connected to the following server:\n'
#         f'{guild.name}(id: {guild.id})'
#         )

#     #print guild members
#     members = '\n - '.join([member.name for member in guild.members])
#     # print(f'Guild Members:\n - {members}')

#----------------------------------------------------------------

# #untested, need to make test account
# @client.event
# async def on_member_join():
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hey {member.name}, welcome to RoboStephSocial!' 
#         )

# #reply to messages about self
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if 'robobuddy' in message.content.lower():
#         await message.channel.send(
#             f'Hey {message.author} :)'
#             )

# #logging any errors
# @client.event
# async def on_error(event, *args, **kwargs):
#     with open('err.log', 'a') as f: 
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else: 
#             raise

    

# client.run(TOKEN)

bot.run(TOKEN)