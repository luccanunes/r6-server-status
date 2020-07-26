def get_oplist():
    import requests
    from bs4 import BeautifulSoup

    URL = 'https://www.ubisoft.com/pt-br/game/rainbow-six/siege/game-info/operators'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    ops_raw = soup.select('.oplist__card')
    ops = list()
    for op in ops_raw:
        ops.append(op.text)

    return ops


def get_loadout(ops):
    import requests
    from bs4 import BeautifulSoup

    for op in ops:
        URL = f'https://www.ubisoft.com/pt-br/game/rainbow-six/siege/game-info/operators/{op}'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
        }
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
