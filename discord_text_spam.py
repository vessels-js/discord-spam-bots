import discord
import asyncio
import sys
from config import *

client = discord.Client()
token = sys.argv[1]
spam_text = sys.argv[2]

@client.event
async def on_ready():
    print("Started Text Spam")
    while not client.is_closed:
        print(spam_text)
        await client.send_message(discord.Object(id=DiscordChannel), spam_text)
        await asyncio.sleep(0.7) # Changes how fast the messages are posted. (Anything under 0.7 tends to break it (┛✧Д✧))┛彡┻━┻ )

client.run(token, bot=False)

        




