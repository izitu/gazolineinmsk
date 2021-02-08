from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

from bs4 import BeautifulSoup

print('now is', time.strftime("%d-%m-%Y"))
options = Options()
options.add_argument('--headless')

driver = webdriver.Firefox(options=options)
adrs = {'Рядом с домом': 'https://m.multigo.ru/benzin/55.7131564;37.60855/11',
        'Рядом с работой': 'https://m.multigo.ru/benzin/55.606751;37.612811/11'}
for elm in adrs:
    driver.get(adrs[elm])
    time.sleep(2)
    htmlSource = driver.page_source
    soup = BeautifulSoup(htmlSource, 'html.parser')
    alel = soup.find_all('div', class_='mob-box mob-borderfalse mob-cls')

    print(elm)
    for el in alel:
        if el.find('div', class_='price green'):
            print(el.find('div', class_='price').contents[0], '\t',
                  el.find('div', class_='price').contents[1].text, '\t',
                  el.find('div', class_='name').text, '\t',
                  el.find('div', class_='address').text)

driver.quit()
