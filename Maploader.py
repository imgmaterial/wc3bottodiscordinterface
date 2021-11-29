import discord
from os import walk

TOKENFILE = open('TOKEN.txt', 'r')

TOKEN = TOKENFILE.read()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif len(message.attachments) == 1:
        channel = message.channel
        attachment = message.attachments[0]
        if message.attachments[0].filename[-4:] == '.w3x':
            await attachment.save('./maps/' + attachment.filename)
            await channel.send('Map uploaded')
        else:
            await channel.send('Wrong file format')
    elif len(message.attachments) > 1:
        channel = message.channel
        await channel.send('Send maps one by one')
    elif message.content.startswith('maplist'):
        channel = message.channel
        await channel.send('maplist')
        filelist = []
        for (dirpath, dirnames, filenames) in walk("./maps/"):
            filelist.extend(filenames)
            break
        await channel.send(filelist)
    else:
        return
    
    







client.run(TOKEN)