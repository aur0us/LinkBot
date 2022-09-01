import discord
import os

def deleteLink():
    client = discord.Client()
    channelId = os.getenv('linkChannel')

    @client.event
    async def on_ready():
        print ('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        channel = client.get_channel(int(channelId))
        if message.author == client.user:
            return

        elif message.content.startswith('https' or 'http'):
            await channel.send(message.content)
            await message.delete()
    client.run(os.getenv('token'))