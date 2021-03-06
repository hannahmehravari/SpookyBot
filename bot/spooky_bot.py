import sys
sys.path.append('C:\\Users\\User\Documents\SpookyBot\game')
import discord, re
import random
from discord.ext.commands import Bot
from discord import Game

client= discord.Client()
   
@client.event
async def on_ready():
    await client.change_presence(game = Game(name='Backgammon'))
    print ("Logged in as " + client.user.name)

global in_Game

@client.event
async def on_message(message):
    in_Game = False
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
    if message.content.startswith('!fightme') and in_Game == False:
        possible_responses = [
            '{0.author.mention}, are you ready to face the big Spook?!',
            'Doot Doot',
            "You really want to do this, {0.author.mention}",
        ]
        await client.send_message(message.channel,
                    random.choice(possible_responses).format(message))
        in_Game = True

    # REAL YOUTUBE LINK TO REAL SPOOK STUFF
    if message.content.startswith('!spook'):
        url = "https://www.youtube.com/watch?v=9DECYte0kZ4"
        await client.send_message(message.channel, url)   

    # Show list of commands to user
    if message.content.startswith('!help'):  
        msg = """The currently available commands are: \n
            !help - shows list of all commands \n
            !fightme - starts a fight against SpookyBot \n
            !spook - real scary stuff"""
        await client.send_message(message.channel, msg)

    #meme
    if message.content.startswith("!triangles"):
        possibleResp = [
            "Triangles are the cause of all fires in the world, because of the fire triangles",
            "Using squares or circles will contain the fire, as they stop triangles"]
        await client.send_message(message.channel, random.choice(possibleResp).format(message))
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

