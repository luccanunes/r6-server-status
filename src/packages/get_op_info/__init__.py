def get_op_info(op):  
    import requests 
    from bs4 import BeautifulSoup
    from unidecode import unidecode

    loadout = list()
    URL = unidecode(
        f'https://www.ubisoft.com/pt-br/game/rainbow-six/siege/game-info/operators/{op}')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # * LOADOUT
    weapons = soup.select('.operator__loadout__weapon')
    gadget = unidecode(weapons[-1].text).capitalize()
    for weapon in weapons:
        if weapon != weapons[-1]:
            info = weapon.find_all('p')
            string = ''
            for inf in info:
                if inf == info[0]:
                    string += f'{inf.text} '
                else:
                    string += f'{inf.text.capitalize()} '
            loadout.append(unidecode(string.strip()))
    # * SIDE
    side = soup.select(".operator__header__side__detail")[0].text
    # * ROLE
    role = soup.select(".operator__header__roles")[0].text[6:].capitalize()
    
    radios = soup.select(".react-rater-star")
    # * ARMOR
    armor = 0
    for i in range(0, 3):
        if "is-active" in str(radios[i]):
            armor += 1
    # * SPEED
    speed = 0
    for i in range(3, 6):
        if "is-active" in str(radios[i]):
            speed += 1
    data = {
        "name": op.lower(),
        "loadout": loadout, 
        "gadget": gadget, 
        "side": side, 
        "role": role, 
        "armor": armor, 
        "speed": speed
    }
    return data