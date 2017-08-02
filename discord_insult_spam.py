import urllib.request
from bs4 import BeautifulSoup, Comment
import discord
import asyncio
from config import *

url='http://foulomatic.hnldesign.nl/'
insult_list = []

client = discord.Client()

@client.event
async def on_ready():
    while not client.is_closed:
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content, "html.parser")
        rows =soup.find_all('div',attrs={"class" : "container"})
        for row in soup.find_all('div',attrs={"class" : "well result"}):
            insult_list.append(row.text) 
                await client.send_message(discord.Object(id=DiscordChannel), insult_list[0] +" "+insult_list[1] +" "+ insult_list[3])
                await asyncio.sleep(0.7) # Changes how fast the messages are posted. (Anything under 0.7 tends to break it (┛✧Д✧))┛彡┻━┻ )
            
            


print("Logged in ┬──┬ ノ( ゜-゜ノ)")

client.run(userEmail, userPassword)
