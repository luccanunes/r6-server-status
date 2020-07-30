def get_oplist():
    import requests
    from unidecode import unidecode
    from bs4 import BeautifulSoup

    URL = 'https://www.ubisoft.com/pt-br/game/rainbow-six/siege/game-info/operators'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    ops_raw = soup.select('.oplist__card')
    ops = dict()
    for op in ops_raw:
        ops[unidecode(op.text.lower())] = dict()
        ops[unidecode(op.text.lower())] = get_op_info(op.text)
    return ops


def get_op_info(op):  # TODO - add real name, birthday, birthplace 
    import requests # ! remember to update ops.py afterwards
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
        "loadout": loadout, "gadget": gadget, "side": side, "role": role, "armor": armor, "speed": speed
    }
    return data


# print(get_op_info('ace'))
txt = open('src/op_info.txt', 'w')
ops = get_oplist()
txt.write(str(ops))

# op_txt = open('src/ops.txt', 'w')
# lo_txt = open('src/lo.txt', 'w')
# oplist = get_oplist()
# for op in oplist:
#     op_txt.write(op + '\n')
# loadout = get_loadout(oplist)
# for lo in loadout:
#     lo_txt.write(lo + '\n')
# op_txt.close()
# lo_txt.close()
