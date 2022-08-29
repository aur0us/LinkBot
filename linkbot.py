import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print ('We have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
    channel = client.get_channel(891325419930935396)
    if message.author == client.user:
      return

    elif message.content.startswith('https' or 'http'): 
      await channel.send(message.content)
      await message.delete()

client.run(os.getenv('token'))