def get_news():
    import requests
    from bs4 import BeautifulSoup

    # h2 .updatesFeed__item__wrapper__content__title
    # dates -- .date

    URL = 'https://www.ubisoft.com/pt-br/game/rainbow-six/siege/news-updates'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    news_raw = soup.select('.updatesFeed__item__wrapper__content__title')
    dates_raw = soup.select('.date')

    news_dates = dict()

    for i in range(0, len(news_raw)):
        new = news_raw[i].text.capitalize()
        date = dates_raw[i+1].text.capitalize()
        news_dates[new] = date

    return news_dates
