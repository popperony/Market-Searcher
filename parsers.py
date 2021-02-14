import requests


def request_market(word):
    url = 'https://market.yandex.ru/list'
    payload = {'text': 'стул'}
    response = requests.get(url, params=payload)
    return response.text

print(request_market(1))















# import time

# from bs4 import BeautifulSoup
# import requests
# from selenium import webdriver


# def ozon_parsing(word):
#     firefoxdriver = r'./drivers/geckodriver'
#     options = webdriver.FirefoxOptions()
#     options.add_argument('--headless')
#     browser = webdriver.Firefox(executable_path=firefoxdriver, options=options)
#     browser.get('https://www.ozon.ru/')
#     browser.get('https://www.ozon.ru/')
#     search = browser.find_element_by_name('search')
#     search.click()
#     search.send_keys(word)
#     search.submit()
#     time.sleep(3)
#     html = browser.page_source
#     soup = BeautifulSoup(html, 'html5lib')
#     price = soup.find("span", {"class": "b5v6 b5v7 c4v8"})
#     img_url = soup.find("div", {"class": "a0i7"})
#     return price, img_url


# def google_engine(query: str):
#     url = 'https://www.googleapis.com/customsearch/v1'
#     API_KEY = 'AIzaSyDO8Be4yBVOht6rjpDCNZ17XP3RP5NwvM4'
#     se_ID = '0eed1a6041c25ae17'
#     payload = {'key': API_KEY, 'cx': se_ID, 'q': query}
#     response = requests.get(url, params=payload)
#     result = []
#     for i in range(3):
#         result.append(response.json()['items'][i]['pagemap']['cse_image'][0]['src'])
#     return result