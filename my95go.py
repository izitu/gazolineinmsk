# берем более актуальные данные https://multigo.ru
import requests, bs4

base_url = 'https://multigo.ru/benzin/55.708592;37.582879/11#50d2e4449078501bf3da1bf1'


headers = {'accept': '*/*',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
session = requests.Session()
s0 = session.get(base_url, headers=headers)
b = bs4.BeautifulSoup(s0.text, "html.parser")

print(b)

# защита стоит