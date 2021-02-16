import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver


def parsing(word):
    firefoxdriver = r'./drivers/geckodriver.exe'
    options = webdriver.FirefoxOptions()
    options.headless = True
    browser = webdriver.Firefox(executable_path=firefoxdriver, options=options)
    browser.get('https://market.yandex.ru/')
    search = browser.find_element_by_id('header-search')
    search.click()
    search.send_keys(word)
    search.submit()
    time.sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html5lib')
    img_url = soup.find("img", {"class": "_2DyHt9sctH"})
    price = soup.find("div", {"class": "_3NaXxl-HYN _3f2ZtYT7NH _1f_YBwo4nE"})
    return 'https:' + img_url["src"], price.text


# def google_engine(query: str):
#     url = 'https://www.googleapis.com/customsearch/v1'
#     API_KEY = 'AIzaSyDO8Be4yBVOht6rjpDCNZ17XP3RP5NwvM4' (не актуален)
#     se_ID = '0eed1a6041c25ae17' (не актуален)
#     payload = {'key': API_KEY, 'cx': se_ID, 'q': query}
#     response = requests.get(url, params=payload)
#     result = []
#     for i in range(3):
#         result.append(response.json()['items'][i]['pagemap']['cse_image'][0]['src'])
#     return result


# def parsing(word):
#     firefoxdriver = r'./drivers/geckodriver.exe'
#     options = webdriver.FirefoxOptions()
#     options.set_preference('general.useragent.override', user_agent)
#     options.set_preference('dom.webdriver.enabled', False)
#     options.headless = True
#     browser = webdriver.Firefox(executable_path=firefoxdriver, options=options)
#     # browser.get('https://browser-info.ru/')
#     browser.get('https://market.yandex.ru/')
#     # browser.get('https://www.ozon.ru/')
#     search = browser.find_element_by_id('header-search')
#     # search = browser.find_element_by_class_name('b7i5')
#     search.click()
#     search.send_keys(word)
#     search.submit()
#     time.sleep(3)
#     result = search.find_element_by_class_name('_1_IxNTwqll _1JtmTvRG7Z cia-vs cia-cs')
#     return result
