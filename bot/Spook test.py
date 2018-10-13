from discord.ext.commands import Bot
from discord import Game
import random

BOT_PREFIX = ("?","!")
TOKEN = "NTAwNDY0MTgxNDY4NzI1MjU2.DqNjSg.uS1w8xjdvqXKIBzfM-6vilypUC0"

# Commands will be recognised if it matches any prefix
client= Bot(command_prefix=BOT_PREFIX)

@client.command(
        name='backgammon',
        # add details to help function for bot
        description = "Big spook plays backgammon against you",
        brief = "Big Spook vs you @ Backgammon",
        pass_context = True
    )
async def backgammon_test(context):
    possible_responses = [
        '{0.author.mention}, are you ready to face the big Spook?!',
        'Doot Doot',
        "Cam's hands are italic",
    ]
    await client.say(random.choice(possible_responses) +
                     ", " + context.message.author.mention)

    
@client.event
async def on_ready():
    await client.change_presence(game = Game(name='with italic hands'))
    print ("Logged in as " + client.user.name)

client.run(TOKEN)
