import discord
import os
import random
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata


# Load environment variables from the .env file
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Create a Discord client instance
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.event
async def on_message(message):
    # Extract information from the message
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    # Print message details
    print(f'Message {user_message} by {username} on {channel}')

    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the message is in the "random" channel
    if channel == "random":
        # Respond to specific messages
        if user_message.lower() == "hello world" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "yo yo":
            await message.channel.send(f'Yo')

        elif user_message.lower() == "are you a hottie?":
            responses = ["Yes, I'm a hottie!", "No, not really.", "Why are you asking me that?"]
            await message.channel.send(random.choice(responses))

        # Add EC2 instance metadata message
        elif user_message.lower() == "ec2 info":
            await message.channel.send(f"Your EC2 Data:\nRegion - {ec2_metadata.region}\nIp Address - {ec2_metadata.public_ipv4}\nAvailability Zone - {ec2_metadata.availability_zone}\nInstance Type - {ec2_metadata.instance_type}")

# Run the bot with the provided token"
client.run(token)
        