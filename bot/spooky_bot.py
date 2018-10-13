# all logic will go here

import discord, re

# Creates new client
client = discord.Client()

global bool inGame = False
global author player = None

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # 
    if message.content.startswith('!backgammon'):
        msg = '{0.author.mention}, are you ready to face the big Spook?!'.format(message)
        await client.send_message(message.channel, msg)
        inGame = True
        backgammon()

    #dadbot command (detects string "im/i am X" and replies with "hi X, im Dad!")
    if ("im" or "i'm")in message.content.lower():
        regex = r"[a-zA-Z0-9' ]+"
        reply = re.search(regex,message.content).group(0)[3:]
        msg = ("Hi "+reply+", I'm Dad!").format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!spook"):
        spook()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

async def backgammon(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    #making a move
    if inGame and message.content.startswith("!move"):
        regex = r'!\c{4} \d{2} \d'
        move = message.content()
        

    #release from jail

    #bear off

    #help

    #quit
    
    
def backgammon_print(board):
    curLine = board[:61]
    remBoard = board[61:]
    reply = ""
    while (remBoard.len() > 0):
        reply.append(curLine + "\n")
        curLine = remBoard[:61]
        remBoard = remBoard[61:]
    
        
# 
client.run('NTAwNDY0MTgxNDY4NzI1MjU2.DqNjSg.uS1w8xjdvqXKIBzfM-6vilypUC0')
