def get_server_status():
    from selenium import webdriver
    from console_log import clog

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(
        executable_path=r'E:\coding\python\chromedriver.exe', chrome_options=options
    )
    driver.get('https://rainbow6.ubisoft.com/status/')
    driver.implicitly_wait(2)

    last_update = driver.find_element_by_tag_name('span').text

    button = driver.find_element_by_class_name('text-right')
    button.click()

    pc = {
        "name": "PC",
        "Conectividade": driver.find_element_by_xpath('//*[@id="root"]/main/div/div/div[1]/div/ul[1]/li[2]/p/small').text,
        "Autenticação": driver.find_element_by_xpath('//*[@id="root"]/main/div/div/div[1]/div/ul[1]/li[3]/p/small').text,
        "Loja": driver.find_element_by_xpath('//*[@id="root"]/main/div/div/div[1]/div/ul[1]/li[4]/p/small').text,
        "Criação de partidas": driver.find_element_by_xpath('//*[@id="root"]/main/div/div/div[1]/div/ul[1]/li[5]/p/small').text
    }
    ps4 = {
        "name": "PS4",
        "Conectividade": driver.find_element_by_xpath('//*[@id="root"]/main/div/div/div[1]/div/ul[2]/li[2]/p/small').text,
        "Autenticação": driver.find_element_by_xpath('//*[@id="root"]/main/div/div/div[1]/div/ul[2]/li[3]/p/small').text,
        "Loja": driver.find_element_by_xpath('//*[@id="root"]/main/div/div/div[1]/div/ul[2]/li[4]/p/small').text,
        "Criação de partidas": driver.find_element_by_xpath('//*[@id="root"]/main/div/div/div[1]/div/ul[2]/li[5]/p/small').text
    }
    xbox = {
        "name": "Xbox One",
        "Conectividade": driver.find_element_by_xpath('//*[@id="root"]/main/div/div/div[1]/div/ul[3]/li[2]/p/small').text,
        "Autenticação": driver.find_element_by_xpath('//*[@id="root"]/main/div/div/div[1]/div/ul[3]/li[3]/p/small').text,
        "Loja": driver.find_element_by_xpath('//*[@id="root"]/main/div/div/div[1]/div/ul[3]/li[4]/p/small').text,
        "Criação de partidas": driver.find_element_by_xpath('//*[@id="root"]/main/div/div/div[1]/div/ul[3]/li[5]/p/small').text
    }

    return {"last-update": last_update, "pc": pc, "ps4": ps4, "xbox": xbox}


def format_dict(dict):
    import discord
    msg = discord.Embed(title=f"{dict['name']} Server Status", colour=discord.Color.from_rgb(244, 175, 44))
    for key in list(dict.keys())[1:]:
        msg.add_field(name=f'\n{key}', value=f'{dict[key]}')
    return msg
