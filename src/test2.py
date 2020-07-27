import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

URL = unidecode(f'https://rainbow6.ubisoft.com/status/')
print(URL)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# weapons = soup.select('.operator__loadout__weapon')

# for weapon in weapons:
#     if weapon != weapons[-1]:
#         info = weapon.find_all('p')
#         string = ''
#         for inf in info:
#             if inf == info[0]:
#                 string += f'{inf.text} '
#             else:
#                 string += f'{inf.text.capitalize()} '
#         print(unidecode(string.strip()))

print(soup.select('.list-group-item'))