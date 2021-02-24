import time
from selenium import webdriver
from selenium import common


def parsing(word):
    firefoxdriver = r'./drivers/geckodriver.exe'
    options = webdriver.FirefoxOptions()
    options.headless = True
    options.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0')  # NOQA E501
    options.set_preference('dom.webdriver.enabled', False)
    browser = webdriver.Firefox(executable_path=firefoxdriver, options=options)
    browser.get('https://market.yandex.ru/')
    search = browser.find_element_by_id('header-search')
    search.click()
    search.send_keys(word)
    search.submit()
    time.sleep(3)
    search = browser.find_elements_by_class_name('_2DyHt9sctH')
    count = 0
    images = []
    try:
        for i in search:
            if count == 3:
                break
            image = i.get_attribute('src')
            images.append(image)
            count += 1
    except Exception:
        print('Image not found.')
    avg_price = []
    try:
        for j in range(5, 0, -1):
            search = browser.find_element_by_xpath(f'/html/body/div[2]/div[3]/div[3]/div[4]/div/div[1]/div/div/div/article[{j}]/div[3]/div/div/a/div/span/span[1]')  # NOQA E501
            avg_price.append(int(search.text.replace(' ', '')))
        return images, sum(avg_price)/len(avg_price)
    except common.exceptions.NoSuchElementException:
        try:
            print('Element not found, change loop.')
            for k in range(5, 0, -1):
                search = browser.find_element_by_xpath(f'/html/body/div[2]/div[3]/div[3]/div[5]/div/div[1]/div/div/div/article[{k}]/div[4]/div/div[1]/div/div/a/div/span/span[1]')  # NOQA E501
                avg_price.append(int(search.text.replace(' ', '')))
            return images, sum(avg_price)/len(avg_price)
        except common.exceptions.NoSuchElementException:
            try:
                print('Element not found, change loop.')
                for o in range(5, 0, -1):
                    search = browser.find_element_by_xpath(f'/html/body/div[2]/div[3]/div[3]/div[5]/div/div[1]/div/div/div/article[{o}]/div[3]/div/div/a/div/span/span[1]')  # NOQA E501
                    avg_price.append(int(search.text.replace(' ', '')))
                return images, sum(avg_price)/len(avg_price)
            except common.exceptions.NoSuchElementException:
                return 'No results were found with this request.'
