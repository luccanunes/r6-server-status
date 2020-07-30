def get_lives():
    from selenium import webdriver
    from time import sleep
    # TODO add streamer name/link, language, viewers

    URL = "https://www.twitch.tv/directory/game/Tom%20Clancy's%20Rainbow%20Six%3A%20Siege"

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    driver = webdriver.Chrome(
        executable_path=r'.\chromedriver.exe', chrome_options=options
    )
    driver.get(URL)
    sleep(3)

    # * LIVE STREAMERS - document.getElementsByClassName('tw-c-text-alt-2')[12:16]
    streamers = driver.find_elements_by_class_name(
        'tw-c-text-alt-2')[6:]  # ! CHANGE HERE TO GET OTHER STREAMERS
    lives = list()
    for streamer in streamers:
        lives.append(streamer.text)

    return lives


def format_lives(lives):
    import discord
    msg = discord.Embed(
        # title='Live Streams',
        colour=discord.Color.from_rgb(100, 65, 165)
    )
    msg.set_thumbnail(url='https://i.imgur.com/wLPYW8A.png')
    for live in lives:
        # msg.add_field(name=live, value=f'https://www.twitch.tv/{live}')
        msg.add_field(name=live, value=f'[watch](https://www.twitch.tv/{live})')

    return msg

