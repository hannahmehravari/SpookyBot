# all logic will go here

import discord

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

    #dadbot command (detects string "im/i am X" and replies with "hi X, im Dad!"
    if "im" in message.content.lower():
        reply = find_between(message.content, "im ", " ")
        msg = "Hi "+reply+", im Dad!".format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def find_between(s, start, end):
    return (s.split(start)[1].split(end)[0])
    
# 
client.run('NTAwNDY0MTgxNDY4NzI1MjU2.DqNjSg.uS1w8xjdvqXKIBzfM-6vilypUC0')
