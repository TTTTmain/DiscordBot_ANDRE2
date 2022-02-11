import requests, json, discord, random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_message(message):
    messageText = message.content.strip().upper()
    if "CAT" in messageText:

        response = requests.get("https://aws.random.cat/meow")
        catImg = json.loads(requests.get("https://aws.random.cat/meow").content)["file"]

        await message.channel.send(catImg)

    if "ANDRE" in messageText:
        #await message.delete()
        await message.channel.send("GAY")

    if "SEE" in messageText and "ANDRE" in messageText:
        randomNum = random.randrange(0,24)
        andreImg = ["1.jpg","2.jpg","3.png","4.jpg","5.jpg","6.jpg","7.jpg","8.jpg","9.jpg"\
        ,"10.jpg","11.jpg","12.jpg","13.jpg","14.jpg","15.jpg","16.jpg","17.jpg","18.jpg","19.jpg","20.png"\
        ,"21.png","22.png","22.png","23.png","24.png","25.png"]

        await message.channel.send(file=discord.File('AndreIMG/' + andreImg[randomNum]))

    if "LITTLE" in messageText or "SITH" in messageText or "SITHIJA" in messageText:
        randomNum = random.randrange(0,5)
        sithImg = ["sith1.jpg","sith2.jpg","sith3.jpg","sith4.jpg","sith5.jpg","sith6.png"]

        await message.channel.send(file=discord.File('SithIMG/' + sithImg[randomNum]))

    if "BRYCE" in messageText:

        await message.channel.send(file=discord.File('BryceIMG/bryce1.png'))

    if "PEW" in messageText:
        #await message.delete()
        await message.channel.send("AHHHHH U GOT ME")


client.run('NzMxMDIzMzU1MDQ1NDc4NTAw.XwgAwA.CnjrIvtRMO6anq9Uz2NP-X7F3DE')
