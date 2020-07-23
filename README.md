# CompetitiveBot
A discord bot which aggregates contestant information like live ranklists, user ratings, solving history etc. from popular competitive programming platforms like
Codeforces, Topcoder etc. The bot also gives problem recommendations filtered on problem rating and topic tags.

## To Install:
- First clone this repo to the desired location. Create and activate a virtual environment if required.
- Install the required python modules by running:
```
$ pip install -r requirements.txt
```
- Create a new discord application and its bot interface by going through [this](https://discordpy.readthedocs.io/en/latest/discord.html) documentation. We will require the bot token in the later steps.
- Make sure that the bot has administrator permissions and add it to your server. (Refer to above documentation)
- Create a dummy handle on Codeforces and remember its credentials.
- Create a .env file in the directory and add the following fields by replacing actual values inside "{ }":
```
DISCORD_TOKEN={discord_token_of_your_created_bot}
CF_HANDLE={handle_of_dummy_codeforces_account}
CF_PASSWORD={password_of_dummy_codeforces_account}
```
- Install geckodriver. (Required for scraping of user lists)
```
$ wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
$ tar xvfz geckodriver-v0.26.0-linux64.tar.gz
$ mv geckodriver ~/.local/bin 
```
- Now go to the *Scripts* folder and run *main.py*:
```
$ cd Scripts/
$ python main.py
```
- Thats it!! Your bot must be up and running in the desired server. You can look up the commands by using: ```cp!help```
