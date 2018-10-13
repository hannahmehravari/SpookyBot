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
    
    #dadbot command (detects string "im/i am X" and replies with "hi X, im Dad!")
    if ("im" or "i'm")in message.content.lower():
        regex = r"[a-zA-Z0-9' ]+"
        reply = re.search(regex,message.content).group(0)[3:]
        msg = ("Hi "+reply+", I'm Dad!").format(message)
        await client.send_message(message.channel, msg)

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
        inGame = True
        backgammon()

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
        regex = r'!\move \d{2} \d'
        move = message.content().split()
        moveCounter, moveRoll = move[1],move[2]
        BGMove(moveCounter, moveRoll)
        backgammon_print()

    #release from jail
    if inGame and message.content.startswith("!rel"):
        regex = r'!rel \d'
        rel = message.content().split()[1]
        BGRelease(rel)

    #bear off
    if inGame and message.content.startswith("!bearoff"):
        regex = r'!bearoff \d'
        boff = message.content.split()[1]
        BGBearOff(boff)

    #help
    if message.content.startswith("!bghelp"):
        await client.send_message(message.channel,
        """While Playing Backgammon, the commands avaliable to use are: \n

            1. !move (counter) (roll) - where counter is a 2-digit number for
            the column with a counter you want to move, and roll is the number
            of spaces you want to move (has to be a number you rolled)\n
            
            2. !rel (start cell) - where start cell is a 2-digit number for the
            column where you want to release (needs to be a number you rolled,
            and the station needs to have no enemy counters in it)

            3. !bearoff (home cell) - where home cell is a number (1-6), for
            a base station where you have a counter to bear off (has to be a
            number you rolled)

            4. !quit - quits the current game of backgammon against the bot and
            returns the bot to normal function""")
        
    #quit    
    if inGame and message.content.startswith("!quit"):
        inGame = False
        
def backgammon_print(board):
    curLine = board[:61]
    remBoard = board[61:]
    reply = ""
    while (remBoard.len() > 0 and inGame = True):
        reply.append(curLine + "\n")
        curLine = remBoard[:61]
        remBoard = remBoard[61:]

client.run(TOKEN)

