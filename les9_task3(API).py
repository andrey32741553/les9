import requests
import datetime as dt

# данный код выдает только первую страницу, хоть в параметрах API указывал результат за последние два дня.
# Хотел в json взять дату и выполнять программу до нужной даты, но json выдаёт какую-то абру-кадабру
# вместо даты - набор каких-то цифр. Что это я так и не понял, поэтому писал код с использованием
# BeautifulSoup


now = dt.date.today()
delta = dt.timedelta(hours=48)
two_days_ago = now - delta

URL = f'https://api.stackexchange.com/2.2/search?fromdate={two_days_ago}&todate={now}' \
      f'&order=desc&sort=creation&tagged=python&site=stackoverflow'
resp = requests.get(URL)


i = 0
for item in resp.json()['items']:
    print(resp.json()['items'][i]['title'])
    print(resp.json()['items'][i]['creation_date'])
    i += 1
