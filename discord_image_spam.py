import discord
import asyncio
import random
import os
from config import *

client = discord.Client()

@client.event
async def on_ready():
    while not client.is_closed:
            UpImage = random.choice(os.listdir(DirPictures)) 
            print(UpImage)
            await client.send_file(discord.Object(id=DiscordChannel), DirPictures + UpImage)
            await asyncio.sleep(0.7) # Changes how fast the images are posted. (Anything under 0.7 tends to break it (┛✧Д✧))┛彡┻━┻ )
            


print("Logged in ┬──┬ ノ( ゜-゜ノ)")

client.run(userEmail, userPassword)
