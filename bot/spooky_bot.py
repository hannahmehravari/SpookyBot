# all bot logic will go here

import discord, re
import random
from discord.ext.commands import Bot
from discord import Game

TOKEN = 'NTAwNDY0MTgxNDY4NzI1MjU2.DqNjSg.uS1w8xjdvqXKIBzfM-6vilypUC0'
client= discord.Client()
   
@client.event
async def on_ready():
    await client.change_presence(game = Game(name='Backgammon'))
    print ("Logged in as " + client.user.name)

global bool inGame = False
global author player = None

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

<<<<<<< HEAD
=======
    # 
    if message.content.startswith('!backgammon'):
        msg = '{0.author.mention}, are you ready to face the big Spook?!'.format(message)
        await client.send_message(message.channel, msg)
        inGame = True
        backgammon()

>>>>>>> 679f99dd83c262971b2873d6d7db6a20f76507c2
    #dadbot command (detects string "im/i am X" and replies with "hi X, im Dad!")
    if ("im" or "i'm")in message.content.lower():
        regex = r"[a-zA-Z0-9' ]+"
        reply = re.search(regex,message.content).group(0)[3:]
        msg = ("Hi "+reply+", I'm Dad!").format(message)
        await client.send_message(message.channel, msg)

<<<<<<< HEAD
    # Should be changed to command to activate game
    # Currently gives random responses from list when acted upon
    if message.content.startswith('!backgammon'):
        possible_responses = [
            '{0.author.mention}, are you ready to face the big Spook?!',
            'Doot Doot',
            "You really want to do this, {0.author.mention}",
        ]
        await client.send_message(message.channel,
                                  random.choice(possible_responses).format(message))

    # REAL YOUTUBE LINK TO REAL SPOOK STUFF
    if message.content.startswith('!spook'):
        url = "https://www.youtube.com/watch?v=9DECYte0kZ4"
        await client.send_message(message.channel, url)   

    # Show list of commands to user
    if message.content.startswith('!help'):  
        msg = """The currently available commands are: \n
            !help - shows list of all commands \n
            !backgammon - starts game of backgammon against spooky bot \n
            !spook - real scary stuff"""
        await client.send_message(message.channel, msg)
        
client.run(TOKEN)
=======
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
>>>>>>> 679f99dd83c262971b2873d6d7db6a20f76507c2
