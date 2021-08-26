import discord
import asyncio
from detection import check_phrase
from discord.ext import commands

 
client = commands.Bot(command_prefix = "!")
counter = 0
channel_id = None

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency*1000)}ms')

"""
@client.command()
@commands.has_guild_permissions(administrator=True)
async def init(ctx):
    global channel_id
    guild = ctx.guild
    counter_channel_name = f"That's fair : {counter}"
    if discord.utils.get(ctx.guild.voice_channels,name=counter_channel_name) == None:
        await guild.create_voice_channel(name=counter_channel_name,user_limit=0)
        channel_id = discord.utils.get(ctx.guild.voice_channels,name=counter_channel_name).id
    else:
        None
"""


@client.command()
@commands.has_guild_permissions(administrator=True)
async def reset(ctx):
    global counter
    counter = 0


"""
@client.command()
async def update(ctx):
    guild = ctx.guild
    counter_channel_name = f"That's fair : {counter}"
    if discord.utils.get(ctx.guild.voice_channels,name=counter_channel_name) == None:
        await guild.create_voice_channel(name=counter_channel_name,user_limit=0)
    else:
        None
"""

@client.command()
async def get_count(ctx):
    global counter
    await ctx.send(f"\"That's fair\" has been said {counter} times!")

@client.command()
@commands.has_guild_permissions(administrator=True)
async def set_counter(ctx,new_counter): #Sets counter to new value
    global counter
    counter = int(new_counter)


@client.event #Checks
async def on_message(message): #Checks messages for phrase and increases counter accordingly
    global counter
    if message.content.startswith('!'):
        await client.process_commands(message)
    else:
        if (check_phrase(message.content,"That's fair") == True) and (message.author != client.user): #Line to determine phrase to check for
            counter += 1
            print(counter)
        else:
            None


client.run('')