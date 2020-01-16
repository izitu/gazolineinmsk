# скачиваем информацию о заправках в МСК
# https://russiabase.ru/prices.php?region=90

#st = 'Цены: Аи-92 - 42.8 р.; Аи-95 - 46.6 р.; Премиум 95 - 48.199 р.; Дизель - 46.2 р.;'

#print(st.find('Аи-95 - '))
#begin_str = st.find('Аи-95 - ')+8
#end_str = begin_str + st[begin_str:].find('р.')
#print(st[begin_str:end_str])
#exit(0)


import requests, bs4, openpyxl

prefix = 'https://russiabase.ru'
base_url = 'https://russiabase.ru/prices.php?raion=2434&mark=ai95'
#'https://russiabase.ru/prices.php?region=90'
headers = {'accept': '*/*',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
session = requests.Session()
s0 = session.get(base_url, headers=headers)
b = bs4.BeautifulSoup(s0.text, "html.parser")

wb = openpyxl.Workbook()

# добавляем новый лист
wb.create_sheet(title='Первый лист', index=0)
# получаем лист, с которым будем работать
sheet = wb['Первый лист']
# заголовок
cell = sheet.cell(row=1, column=1)
cell.value = 'Название'
cell = sheet.cell(row=1, column=2)
cell.value = 'Адрес'
cell = sheet.cell(row=1, column=3)
cell.value = 'Цена'
cell = sheet.cell(row=1, column=4)
cell.value = 'URL'
r = 2

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
        print(azs_name, azs_url)
        print(azs_adr)
        print(azs.select('.org-body')[0].select('p')[1].text)
        print(azs_95_gaz)

        cell = sheet.cell(row=r, column=1)
        cell.value = azs_name
        cell = sheet.cell(row=r, column=2)
        cell.value = azs_adr
        cell = sheet.cell(row=r, column=3)
        cell.value = azs_95_gaz.replace('.',',').strip()
        cell = sheet.cell(row=r, column=4)
        cell.value = azs_url
        r = r + 1

wb.save('allgaz-lubertzci.xlsx')

