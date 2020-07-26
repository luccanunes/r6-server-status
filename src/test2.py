# import requests
# from bs4 import BeautifulSoup

# URL = f'https://www.ubisoft.com/pt-br/game/rainbow-six/siege/game-info/operators/ace'.replace(
#     'Ø', 'O').replace('Ã', 'A').replace('ä', 'a')
# print(URL)
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
# }
# page = requests.get(URL, headers=headers)
# soup = BeautifulSoup(page.content, 'html.parser')

# weapons = soup.select('.operator__loadout__weapon')

# for weapon in weapons:
#     info = weapon.find_all('p')
#     string = ''
#     for inf in info:
#         string += f'{inf.text} '
#     print(string)