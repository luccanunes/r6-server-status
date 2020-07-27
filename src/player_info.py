def text(tag):
    i = tag.find('>')
    j = tag.find('<', 1)
    return tag[i+1:j]


def title(div):
    ops = list()
    i = div.find('>')
    imgs = div[i+1:-7].split('\n')
    for j in range(1, len(imgs)):
        index = imgs[j].find('title')
        imgs[j] = imgs[j][index:]
        imgs[j] = imgs[j].split('"')
        ops.append(imgs[j][1])
    return ops


def get_player_info(platform, player):
    '''
    params:
    platform - ('psn', 'pc', 'xbox')
    '''
    import requests
    from bs4 import BeautifulSoup
    from unidecode import unidecode

    URL = unidecode(f'https://r6.tracker.network/profile/{platform}/{player}')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # * OVERVIEW - document.getElementsByClassName("trn-card--dark-header")[0]
    overview_raw = soup.select(".trn-card--dark-header")[0]
    overview_names = overview_raw.select(".trn-defstat__name")
    overview_values = overview_raw.select(".trn-defstat__value")
    overview = dict()
    for i in range(0, len(overview_names) - 7):  # ? it just kept adding random stuff
        name = text(str(overview_names[i])).strip()
        value = text(str(overview_values[i])).strip()
        if name == 'Top Operators':
            value = title(str(overview_values[i]))
        if name not in overview.keys():
            overview[name] = value

    # * RANKED - document.getElementsByClassName("trn-card__content")[6]
    ranked_raw = soup.select(".trn-card__content")[8]
    ranked_names = ranked_raw.select(".trn-defstat__name")
    ranked_values = ranked_raw.select(".trn-defstat__value")
    ranked = dict()
    for i in range(0, len(ranked_names)):
        name = text(str(ranked_names[i])).strip()
        value = text(str(ranked_values[i])).strip()
        if name not in ranked.keys():
            ranked[name] = value

    # * SEASON - document.getElementsByClassName("r6-season__stats")[0]
    season_raw = soup.select(".r6-season__stats")[0]
    season_names = season_raw.select(".trn-defstat__name")
    season_values = season_raw.select(".trn-defstat__value")
    season = dict()
    for i in range(0, len(season_names)):
        name = text(str(season_names[i])).strip()
        value = text(str(season_values[i])).strip()
        if name not in season.keys():
            season[name] = value

    # * DATA
    data = dict()
    data["overview"] = overview
    data["ranked"] = ranked
    data["season"] = season

    return data


def format_player_info(data):
    import discord
    ov = discord.Embed(title='Overview', colour=discord.Color.from_rgb(244, 175, 44))
    for info in data["overview"].keys():
        if type(data["overview"][info]) is not list:
            ov.add_field(name=info, value=data["overview"][info])
        else:
            string = f'{data["overview"][info][0].capitalize()}, {data["overview"][info][1].capitalize()} and {data["overview"][info][2].capitalize()}'
            ov.add_field(name=info, value=string)
    rd = discord.Embed(title='Ranked', colour=discord.Color.from_rgb(244, 175, 44))
    for info in data["ranked"].keys():
        rd.add_field(name=info, value=data["ranked"][info])
    sn = discord.Embed(title='Season', colour=discord.Color.from_rgb(244, 175, 44))
    for info in data["season"].keys():
        sn.add_field(name=info, value=data["season"][info])

    return {'overview': ov, 'ranked': rd, 'season': sn}
