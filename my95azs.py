# цены смотрим на тех, кот. мне интересны
# скачиваем информацию о заправках в МСК
# https://russiabase.ru/prices.php?region=90

import requests, bs4
moi_azs = ['Адрес: Москва, Канатчиковский проезд, 5, стр. 2',
            'Адрес: Москва, Подольских Курсантов ул., 7А',
            'Адрес: Москва, Варшавское шоссе, вл. 99А',
            'Адрес: Москва, Дорожный 1-й проезд, 1А',
            'Адрес: Москва, Даниловская наб., 8Б',
            'Адрес: Москва, Жуков проезд, вл. 15А']

prefix = 'https://russiabase.ru'
base_url = 'https://russiabase.ru/prices.php?region=90'
# МО люберецкий р-он 'https://russiabase.ru/prices.php?raion=2434&mark=ai95'

headers = {'accept': '*/*',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
session = requests.Session()
s0 = session.get(base_url, headers=headers)
b = bs4.BeautifulSoup(s0.text, "html.parser")
all_raw_block = b.select('.org-cont')

for azs in all_raw_block:
    azs_name = azs.select('.org-head')[0].text
    azs_url = prefix + azs.select('.org-head')[0].select('a')[0].get('href')
    azs_adr = azs.select('.org-body')[0].select('p')[0].text
    azs_all_gaz = azs.select('.org-body')[0].select('p')[1].text

    # ищем 95 бензин в стоке, начальную позицию
    # и конечную, там, где р.
    begin_str = azs_all_gaz.find('Аи-95 - ') + 8
    end_str = begin_str + azs_all_gaz[begin_str:].find('р.')
    azs_95_gaz = azs_all_gaz[begin_str:end_str]

    # если begin_str == 7 значит 95 бензин не найден
    if begin_str !=7 :
        if azs_adr in moi_azs:
            #print(azs_name, azs_url)
            print(azs_95_gaz,azs_name,azs_adr)
            #print(azs.select('.org-body')[0].select('p')[1].text)
            #print(azs_95_gaz)
