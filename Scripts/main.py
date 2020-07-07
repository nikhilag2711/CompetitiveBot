import os, asyncio, random, discord, json, requests, re, datetime
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='cp!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!!!')

@bot.command(name='test', help='Simple command for testing if the bot is active!!')
async def test_bot(ctx):
    await ctx.send(f'Hello human! BEEP BEEP BOOP BOOP')

@bot.command(name='create-channel',help='Creates a channel in you Discord server if it does not exist. (Works only for admin mode)')
@commands.has_role('admin')
async def create_channel(ctx, channel_name: str):
    guild_name = ctx.guild
    existing_channel = discord.utils.get(guild_name.channels, name=channel_name)
    if existing_channel:
        await ctx.send(f'The channel {channel_name} already exists.')
        print(f'The channel {channel_name} already exists.')
    else:
        print(f'Creating a new channel: {channel_name}')
        await guild_name.create_text_channel(channel_name)
        await ctx.send(f'New channel {channel_name} created.')

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

# ~~~~~~~ CODEFORCES ~~~~~~~~~~~
###### Creating Coroutines for User Info#############



######################################################


###### Creating coroutines for standings by use of lists ########



###########################################################


###### Coroutines for rating changes ###################

#####################################################

########### Coroutines for problemset ###############

###################################################

############ Coroutines for contest lists ###############


###############################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

bot.run(TOKEN)
