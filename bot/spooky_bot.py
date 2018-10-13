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
