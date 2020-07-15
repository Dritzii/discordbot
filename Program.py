import discord
import configparser
import os


from jokes import Jokes as jk

joke = jk()

config = configparser.ConfigParser()
absolute =  os.path.dirname(os.path.abspath(__file__)) + "/config.ini"
config.read(absolute)
discord_details = {}
discord_credentials = config.options("discord")
for token in discord_credentials:
    try:
        discord_details[token] = config.get("discord", token)
        if discord_details[token] == -1:
            print("skip: %s" % token)
    except:
        print("Exception")


class MyClient(discord.Client):
    async def on_ready(self):
        for guild in client.guilds:
            print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n')
       
    async def on_message(self, message):
        for guild in client.guilds:
            if message.content == "!chuckjoke":
                joke = joke().get_random_joke()
                await message.channel.send(f'Random Joke: {joke}')
            if message.content == "!users":
                await message.channel.send(f'# of Members: {guild.member_count}')
            if message.content == "!members":
                members = '\n - '.join([member.name for member in guild.members])
                await message.channel.send(f'Guild Members:\n - {members}')
            if message.content == "!guildid":
                await message.channel.send(f'Guild id is {guild.id}')
            if message.content == "!help":
                await message.channel.send(f'There are several options avaliable:\n !guildid \n !members \n !users \n !hello')
            if message.content == "!shutdown":
                await client.close()



client = MyClient()
client.run(discord_details['token'])


