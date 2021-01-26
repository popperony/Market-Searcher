from selenium import webdriver
from bs4 import BeautifulSoup


chromedriver = r'./chromedriver.exe'
firefoxdriver = r'./drivers/geckodriver'
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(executable_path=chromedriver)
browser.get('https://www.yandex.ru/')
html = browser.page_source

soup = BeautifulSoup(html, 'html5lib')
quotes = soup.find_all("div", {"class": "weather__temp"})
print(quotes)