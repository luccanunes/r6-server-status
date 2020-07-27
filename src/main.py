import discord
import asyncio
from get_server_status import get_server_status, format_dict
from get_news import get_news
from ops import ops
from format_op import format_op
from unidecode import unidecode
from player_info import get_player_info, format_player_info

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
            msg = discord.Embed(title='Commands', description="Here's a list of all commands!", colour=discord.Color.from_rgb(244, 175, 44))
            msg.add_field(name=f'{prefix}pcstats', value='shows info regarding the status of the PC servers')
            msg.add_field(name=f'{prefix}ps4stats', value='shows info regarding the status of the PS4 servers')
            msg.add_field(name=f'{prefix}xboxstats', value='shows info regarding the status of the Xbox One servers')
            msg.add_field(name=f'{prefix}agent (agent name)', value="shows agent's general info")
            msg.add_field(name=f'{prefix}player (name) (platform)', value="tracks player's info")
            await message.channel.send(embed=msg)
        elif 'stats' in message.content.lower():
            await message.channel.send("```Getting info...```")
            if message.content.lower().startswith(f'{prefix}pcstats'):
                status = get_server_status()
                info = format_dict(status["pc"], status['last-update'])
                await message.channel.send(embed=info)
            elif message.content.lower().startswith(f'{prefix}ps4stats'):
                status = get_server_status()
                info = format_dict(status["ps4"], status['last-update'])
                await message.channel.send(embed=info)
            elif message.content.lower().startswith(f'{prefix}xboxstats'):
                status = get_server_status()
                info = format_dict(status["xbox"], status['last-update'])
                await message.channel.send(embed=info)
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
                    await message.channel.send(embed=format_op(op))
                except:
                    await message.channel.send(f"Failed to find {op}'s information! Please check agent's name and try again")
        elif message.content.lower().startswith(f'{prefix}player'):
            try:
                player = unidecode(message.content.split(' ')[1])
                platform = unidecode(message.content.lower().split(' ')[2]).lower()
            except:
                msg = discord.Embed(title='Error', description=f"Please give me a valid player name and/or platform", colour=discord.Color.from_rgb(255, 0, 0))
                await message.channel.send(embed=msg)
            else:
                try:
                    await message.channel.send("```Getting info...```")
                    player_info = format_player_info(get_player_info(platform, player))
                    await message.channel.send(embed=player_info["overview"])
                    await message.channel.send(embed=player_info["ranked"])
                    await message.channel.send(embed=player_info["season"])
                except:
                    msg = discord.Embed(title='Error', description=f"Failed to find {player}'s information! Please check player's name and platform and try again", colour=discord.Color.from_rgb(255, 0, 0))
                    await message.channel.send(embed=msg)

client.run('NzM2NzY2NDg0MDU5MjU4OTMx.XxzlQg._8lktwlNtqNccRRO8vu62LQwHQI')
