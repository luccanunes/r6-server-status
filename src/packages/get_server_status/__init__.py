def get_server_status():
    import json
    import requests
    from bs4 import BeautifulSoup
    from unidecode import unidecode

    URL = unidecode(f'https://game-status-api.ubisoft.com/v1/instances?appIds=e3d5ea9e-50bd-43b7-88bf-39794f4e3d40,fb4cc4c9-2063-461d-a1e8-84a7d36525fc,4008612d-3baf-49e4-957a-33066726a7bc')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    json = json.loads(str(soup))

    dicts = list()

    for platform in json:
        dictionary = {
            "name": platform["Platform"],
            "status": platform["Status"],
            "impactedFeatures": platform["ImpactedFeatures"]
        }
        dicts.append(dictionary)
    pc = dicts[0]
    ps4 = dicts[1]
    xbox = dicts[2]

    return {"pc": pc, "ps4": ps4, "xbox": xbox}


def format_dict(dict):
    import discord
    msg = discord.Embed(title=f"{dict['name']} Server Status", colour=discord.Color.from_rgb(244, 175, 44))

    msg.add_field(name=f'\nStatus', value=f'{dict["status"]}')
    impacted_features = ""
    for feature in dict['impactedFeatures']:
        impacted_features += f'{feature}, ' if feature != dict['impactedFeatures'][-1] else feature
    if len(impacted_features) == 0:
        impacted_features = 'None' 
    msg.add_field(name=f'\nImpacted Features', value=f'{impacted_features}')

    msg.add_field(name='Last Updated', value='Just now')
    
    return msg

get_server_status()