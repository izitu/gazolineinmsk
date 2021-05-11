# берем данные с гисметео

import requests
import bs4
from flask import Flask

#app = Flask(__name__)
#@app.route('/')

#def hello_world():
base_url = 'https://www.gismeteo.ru/weather-moscow-4368/tomorrow/'
headers = {'accept': '*/*', 'X-Gismeteo-Token': '56b30cb255.3443075',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
session = requests.Session()
s0 = session.get(base_url, headers=headers)
b = bs4.BeautifulSoup(s0.text, "html.parser")
all_raw_block = b.find_all('div', class_='tabs _center')
al = all_raw_block[0].select('.tooltip')
htm_string = ''
for el in al:
    htm_string = htm_string + el.get('data-text') + '<br />'
    print(el.get('data-text'))
    # выводим дату и время / дату и сегодня или завтра в одну строчку без пробелов
    htm_string = htm_string + el.find_all('div', class_='date')[0].text.strip() + ' ' +\
                 el.find_all('div', class_='date')[1].text.strip() + '<br />' +\
                 'Ночь: ' + el.find_all('span', class_='unit unit_temperature_c')[0].text.strip() +\
                 '/ День:' + el.find_all('span', class_='unit unit_temperature_c')[1].text.strip() + '<hr />'

    print(el.find_all('div', class_='date')[0].text.strip(),
          el.find_all('div', class_='date')[1].text.strip())
    print(el.find_all('span', class_='unit unit_temperature_c')[0].text.strip(), '/',
          el.find_all('span', class_='unit unit_temperature_c')[1].text.strip())

    print('---------------')
print(htm_string)
    #return 'Hello World!'

#if __name__ == '__main__':
#    app.run(debug=True)


