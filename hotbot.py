import discord
import os
import random 
from dotenv import load_dotenv 
from ec2_metadata import ec2_metadata

# Get Discord token from environment variable
load_dotenv() 
  
client = discord.Bot() 
token = os.getenv('MTE3OTExMTM5NzM2NDM0Mjk3Ng.G3bKBp.wgB8PnRx1l7yK4f7wNM6AB_tavV8awuTOT20HM')

@client.event 
async def on_ready(): 
    print("Logged in as a bot {0.user}".format(client))

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!')

# Bot event to display EC2 instance metadata
@bot.event
async def on_message(message):
    if message.content.startswith('!ec2data'):
        username = message.author.name
        await message.channel.send(f"Sooner! {username} Your EC2 Data: {ec2_metadata.region}")

