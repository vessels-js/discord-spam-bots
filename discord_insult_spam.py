import urllib
import discord
import asyncio
from config import *

client = discord.Client()

@client.event
async def on_ready():
    insult_text = urllib.request.urlopen("https://insult.mattbas.org/api/insult.txt").read()
    print(insult_text)
    await client.send_message(discord.Object(id=DiscordChannel), insult_text)
    await asyncio.sleep(0.7) # Changes how fast the messages are posted. (Anything under 0.7 tends to break it (┛✧Д✧))┛彡┻━┻ )

print("Logged in ┬──┬ ノ( ゜-゜ノ)")
client.run(userToken, bot=False)
