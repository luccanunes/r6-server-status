import discord
import asyncio
from get_info import get_info, format_dict

client = discord.Client()


@client.event
async def on_ready():
    print('now online - hello, world')
    print(client.user.name)
    print(client.user.id)
    print('-'*20)


@client.event
async def on_message(message):
    if message.content.lower().startswith('?help'):
        await message.channel.send(
            "Here's a list of all commands! ```?pcstats - shows info regarding the status of the PC servers\n?ps4stats - shows info regarding the status of the PS4 servers\n?xboxstats - shows info regarding the status of the Xbox One servers```"
        )
    elif message.content.lower().startswith('?pcstats'):
        await message.channel.send("Getting info...")
        data = get_info()
        info = format_dict(data["pc"])
        last_updt = data["last-update"]
        await message.channel.send(f"Last update: {last_updt}")
        await message.channel.send(info)
    elif message.content.lower().startswith('?ps4stats'):
        await message.channel.send("Getting info...")
        data = get_info()
        info = format_dict(data["ps4"])
        last_updt = data["last-update"]
        await message.channel.send(f"Last update: {last_updt}")
        await message.channel.send(info)
    elif message.content.lower().startswith('?xboxstats'):
        await message.channel.send("Getting info...")
        data = get_info()
        info = format_dict(data["xbox"])
        last_updt = data["last-update"]
        await message.channel.send(f"Last update: {last_updt}")
        await message.channel.send(info)

client.run('NzM2NzY2NDg0MDU5MjU4OTMx.XxzlQg._8lktwlNtqNccRRO8vu62LQwHQI')
