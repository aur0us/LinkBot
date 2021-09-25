import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print ('We have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    if message.content.endswith('.com'):
      channel = client.get_channel(891325419930935396)
      await channel.send(message.content)      

client.run(os.getenv('TOKEN'))