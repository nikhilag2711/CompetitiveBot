import os, asyncio, random, discord, json, requests, re, datetime
from dotenv import load_dotenv
from discord.ext import commands
from CFListScraper import ScrapeList
import RanklistCreator as rl
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='cp!')
cf_scraper = ScrapeList()
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

@bot.command(name='ranklist',help='Displays the standings along with rating changes of the users in a list specified by user (Shows at max 17 positions)')
async def disp_ranklist(ctx,contest_id: str,key:str=''):
    handles=''
    if(key!=''):
        handles = cf_scraper.list_scrape(key)
        STANDINGS_URL=f'https://codeforces.com/api/contest.standings?contestId={contest_id}&handles={handles}&showUnofficial=true'
        obj = requests.get(STANDINGS_URL)
    else:
        STANDINGS_URL=f'https://codeforces.com/api/contest.standings?contestId={contest_id}&from=1&count=17'
        obj = requests.get(STANDINGS_URL)
        handles='yay'
    print(handles)
    if(handles==''):
        await ctx.send("Such a list does not exist")
        return
    temp = json.loads(obj.text)
    if(temp['status']=="FAILED"):
        await ctx.send(f'{temp["comment"]}')
    elif len(temp['result'])==0:
        await ctx.send(f'No data available to display')
    else:
        ans = rl.create_ranklist(temp)
        print(ans)
        await ctx.send(ans)




###########################################################


###### Coroutines for rating changes ###################

#####################################################

########### Coroutines for problemset ###############

###################################################

############ Coroutines for contest lists ###############


###############################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

bot.run(TOKEN)
