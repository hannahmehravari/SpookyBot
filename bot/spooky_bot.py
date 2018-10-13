# all logic will go here

import discord, re

# Creates new client
client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # 
    if message.content.startswith('!backgammon'):
        msg = '{0.author.mention}, are you ready to face the big Spook?!'.format(message)
        await client.send_message(message.channel, msg)

    #dadbot command (detects string "im/i am X" and replies with "hi X, im Dad!")
    if ("im" or "i'm")in message.content.lower():
        regex = r"[a-zA-Z0-9']"
        reply = re.search(
        msg = "Hi "+reply+", I'm Dad!".format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def dad_split(s, start, end):
    return (s.split(start)[1].split(end)[0])
    
# 
client.run('NTAwNDY0MTgxNDY4NzI1MjU2.DqNjSg.uS1w8xjdvqXKIBzfM-6vilypUC0')
