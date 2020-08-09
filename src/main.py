import discord
import asyncio
from packages.get_server_status import get_server_status, format_dict
from packages.get_news import get_news
from packages.ops import ops
from packages.format_op import format_op
from unidecode import unidecode
from packages.player_info import get_player_info, format_player_info
from packages.live import get_lives, format_lives
from packages.prefix import change_prefix
from packages.quote import get_quote
from time import sleep

client = discord.Client()

@client.event
async def on_ready():
    print('now online - hello, world')
    print(client.user.name)
    print(client.user.id)
    print('-'*20)


@client.event
async def on_message(message):
    global prefix
    log = open(r'log.txt', 'r+')
    found_prefix = False
    for line in log.readlines():
        if str(message.guild.id) in line:
            prefix = line.split(' ')[1].replace('\n', '')
            found_prefix = True
    if not found_prefix:
        prefix = '?'
    if message.content.lower().startswith(f'{prefix.lower()}'):
        if message.content.lower().startswith(f'{prefix.lower()}help'):
            msg = discord.Embed(title='Commands', description="Here's a list of all commands!", colour=discord.Color.from_rgb(244, 175, 44))
            msg.set_thumbnail(url='https://i.imgur.com/Vgrtz5u.png')
            msg.add_field(name=f'{prefix}pcstats', value='shows info regarding the status of the PC servers')
            msg.add_field(name=f'{prefix}ps4stats', value='shows info regarding the status of the PS4 servers')
            msg.add_field(name=f'{prefix}xboxstats', value='shows info regarding the status of the Xbox One servers')
            msg.add_field(name=f'{prefix}agent (agent name)', value="shows agent's general info")
            msg.add_field(name=f'{prefix}player (name) (platform)', value="tracks player's info (default platform is PC)")
            msg.add_field(name=f'{prefix}live', value=f"shows live streams on twitch ({prefix}lives also works)")
            msg.add_field(name=f'{prefix}prefix (new prefix)', value=f"changes the server's command prefix")
            msg.add_field(name=f'{prefix}quote', value=f"generates a very wise quote.")
            await message.channel.send(embed=msg)
        elif 'stats' in message.content.lower():
            await message.channel.send("Working on it...")
            if message.content.lower().startswith(f'{prefix.lower()}pcstats'):
                status = get_server_status()
                info = format_dict(status["pc"])
                await message.channel.send(embed=info)
            elif message.content.lower().startswith(f'{prefix.lower()}ps4stats'):
                status = get_server_status()
                info = format_dict(status["ps4"])
                await message.channel.send(embed=info)
            elif message.content.lower().startswith(f'{prefix.lower()}xboxstats'):
                status = get_server_status()
                info = format_dict(status["xbox"])
                await message.channel.send(embed=info)
        elif message.content.lower().startswith(f'{prefix.lower()}news'):
            await message.channel.send("Working on it...")
            news = get_news()
            string = ''
            for new, date in news.items():
                string += f'{new} - {date}\n'
            await message.channel.send(string)
        elif message.content.lower().startswith(f'{prefix.lower()}agent'):
            try:
                op = unidecode(message.content.lower().split(' ')[1])
            except:
                msg = discord.Embed(title='Error', description=f"Please give me a valid agent", colour=discord.Color.from_rgb(255, 0, 0))
                await message.channel.send(embed=msg)
            else:
                try:
                    await message.channel.send(embed=format_op(op))
                except:
                    msg = discord.Embed(title='Error', description=f"Failed to find {op}'s information! Please check agent's name and try again", colour=discord.Color.from_rgb(255, 0, 0))
                    await message.channel.send(embed=msg)
        elif message.content.lower().startswith(f'{prefix.lower()}player'):
            try:
                player = unidecode(message.content.split(' ')[1])
            except:
                msg = discord.Embed(title='Error', description=f"Please give me a valid player name and/or platform", colour=discord.Color.from_rgb(255, 0, 0))
                await message.channel.send(embed=msg)
            else:
                try:
                    if len(message.content.split(' ')) == 2:
                        platform = 'pc'
                    else:
                        platform = unidecode(message.content.lower().split(' ')[2]).lower()
                    await message.channel.send("Working on it...")
                    player_info = format_player_info(get_player_info(platform, player))
                    await message.channel.send(embed=player_info["overview"])
                    await message.channel.send(embed=player_info["ranked"])
                    await message.channel.send(embed=player_info["season"])
                except:
                    msg = discord.Embed(title='Error', description=f"Failed to find {player}'s information! Please check player's name and platform and try again", colour=discord.Color.from_rgb(255, 0, 0))
                    await message.channel.send(embed=msg)
        elif message.content.lower().startswith(f'{prefix.lower()}lives') or message.content.lower().startswith(f'{prefix.lower()}live'):
            await message.channel.send("Working on it...")
            lives = get_lives()[:6]
            msg = format_lives(lives)
            await message.channel.send(embed=msg)
        elif message.content.lower().startswith(f'{prefix.lower()}prefix'):
            try:
                new_prefix = message.content.split(' ')[1]
            except:
                msg = discord.Embed(title='Error', description=f"Please give me a valid prefix", colour=discord.Color.from_rgb(255, 0, 0))
                await message.channel.send(embed=msg)
            else:
                log = open(r'log.txt', 'a')
                log.write(f'{message.guild.id}: {new_prefix}\n')
                log.close()
                change_prefix(new_prefix)
                msg = discord.Embed(title='Prefix', description=f"Sucessfully updated prefix to {new_prefix}", colour=discord.Color.from_rgb(244, 175, 44))
                await message.channel.send(embed=msg)
        elif message.content.lower().startswith(f'{prefix.lower()}quote'):
            await message.channel.send(get_quote())
        elif message.content.lower().startswith(f'{prefix.lower()}clear'):
            msg_list = message.content.split(' ')
            if len(msg_list) == 2:
                try:
                    deleted = await message.channel.purge(limit=int(msg_list[1]) + 1)
                except:
                    msg = discord.Embed(title='Error', description=f"Please give me a valid number of messages or upgrade my permissions!", colour=discord.Color.from_rgb(255, 0, 0))
                    await message.channel.send(embed=msg)
                else:
                    msg = discord.Embed(title='Clear', description=f"Sucessfully deleted {len(deleted)} messages", colour=discord.Color.from_rgb(244, 175, 44))
                    await message.channel.send(embed=msg)
            else:
                try:
                    deleted = await message.channel.purge(limit=100)
                    msg = discord.Embed(title='Clear', description=f"Sucessfully deleted {len(deleted)} messages", colour=discord.Color.from_rgb(244, 175, 44))
                    await message.channel.send(embed=msg)
                except:
                    msg = discord.Embed(title='Error', description=f"Please upgrade my permissions!", colour=discord.Color.from_rgb(255, 0, 0))
                    await message.channel.send(embed=msg)

client.run('NzM2NzY2NDg0MDU5MjU4OTMx.XxzlQg._8lktwlNtqNccRRO8vu62LQwHQI')
