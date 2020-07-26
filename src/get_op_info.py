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
        ops[unidecode(op.text.lower())] = get_loadout(op.text)
    return ops


def get_loadout(op):
    import requests
    from bs4 import BeautifulSoup
    from unidecode import unidecode

    loadout = list()
    URL = unidecode(f'https://www.ubisoft.com/pt-br/game/rainbow-six/siege/game-info/operators/{op}')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    weapons = soup.select('.operator__loadout__weapon')
    gadget = unidecode(weapons[-1].text)
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
    return {"loadout": loadout, "gadget": gadget}


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
