import discord
import youtube_dl
from bot_token import TOKEN

if not TOKEN:
    raise ValueError("Please add your token to bot_token.py")

client = discord.Client()

@client.event
async def on_message(message):
    if message.author== client.user :
        return
    elif message.content.startswith("*l"):
        msg = f'{message.content[3:]}Hello{message.author.mention}'
        await client.send_message(message.channel, msg)
    elif message.content.startswith("*chante"):
        url= message.content[8:]


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)