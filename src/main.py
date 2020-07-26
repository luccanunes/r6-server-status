import discord
import asyncio
from get_server_status import get_server_status, format_dict
from get_news import get_news
from ops import ops
from format_op import format_op
from unidecode import unidecode

client = discord.Client()


@client.event
async def on_ready():
    print('now online - hello, world')
    print(client.user.name)
    print(client.user.id)
    print('-'*20)


@client.event
async def on_message(message):
    prefix = '?'
    if message.content.lower().startswith(f'{prefix}'):
        if message.content.lower().startswith(f'{prefix}help'):
            await message.channel.send(
                f"Here's a list of all commands! ```{prefix}pcstats - shows info regarding the status of the PC servers\n{prefix}ps4stats - shows info regarding the status of the PS4 servers\n{prefix}xboxstats - shows info regarding the status of the Xbox One servers\n{prefix}news - shows the recente news/updates in R6\n{prefix}agent (agent name) - shows agent's general info```"
            )
        elif 'stats' in message.content.lower():
            await message.channel.send("```Getting info...```")
            if message.content.lower().startswith(f'{prefix}pcstats'):
                status = get_server_status()
                info = format_dict(status["pc"])
                await message.channel.send(info)
            elif message.content.lower().startswith(f'{prefix}ps4stats'):
                status = get_server_status()
                info = format_dict(status["ps4"])
                await message.channel.send(info)
            elif message.content.lower().startswith(f'{prefix}xboxstats'):
                status = get_server_status()
                info = format_dict(status["xbox"])
                await message.channel.send(info)
            elif message.content.lower().startswith(f'{prefix}lastupdate'):
                last_updt = status["last-update"]
                await message.channel.send(last_updt)
        elif message.content.lower().startswith(f'{prefix}news'):
            await message.channel.send("```Getting info...```")
            news = get_news()
            string = ''
            for new, date in news.items():
                string += f'{new} - {date}\n'
            await message.channel.send(string)
        elif message.content.lower().startswith(f'{prefix}agent'):
            try:
                op = unidecode(message.content.lower().split(' ')[1])
            except:
                await message.channel.send(f"Please give me a valid agent")
            else:
                try:
                    await message.channel.send(format_op(op))
                except:
                    await message.channel.send(f"Failed to find {op}'s information! Please check agent's name and try again")

client.run('NzM2NzY2NDg0MDU5MjU4OTMx.XxzlQg._8lktwlNtqNccRRO8vu62LQwHQI')
