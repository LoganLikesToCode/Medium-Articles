import discord
import random

client = discord.Client()
prefix = "!"

@client.event
async def on_ready():
  print('We have logged in as {0.user}!'.format(client))
 

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  m = message.content
  
  if m.startswith(prefix+"help"):
    await message.channel.send("> **Help Command**\n`help`: Shows this message!\n`dice`: Roll a dice!\n`random`: Get a random number from anywhere between 1-100!")
   
  if m.startswith(prefix+"dice"):
    dice_number = random.randint(1, 6)
    dice_number = str(dice_number)
    await message.channel.send(dice_number)
   
  if m.startswith(prefix+"random"):
    random_number = random.randint(1, 100)
    random_number = str(random_number)
    await message.channel.send(random_number)

client.run("YOUR-TOKEN-HERE")
