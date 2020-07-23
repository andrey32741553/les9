import datetime as dt
import requests
from bs4 import BeautifulSoup

# поставил 58 часов, потому что "now" выставляет время в моём часовом поясе, а при поиске даты по
# странице выдаёт по UTC, поэтому к 48 часам (двое суток) прибавил 10 часов (это мой часовой пояс по UTC)

def assign_date():
    now = dt.datetime.today()
    delta = dt.timedelta(hours=58)
    two_days_ago = (str(now - delta))[:13]
    return two_days_ago


def making_request():
    page = 1
    while True:
        resp = requests.get(f'https://stackoverflow.com/questions/tagged/python?tab=newest&page={page}&pagesize=50')
        text = resp.text
        soup = BeautifulSoup(text, "html.parser")
        question_list = soup.find('div', {'id': 'questions'}, {'class': 'flush-left'})
        result = question_list.find_all('div', {'class': 'question-summary'})
        question, date = look_for_question_date(result)

        if assign_date() in date:
            break
        print(page)
        page += 1
    return 'questions for two days printed'


def look_for_question_date(items):
    for item in items:
        question = item.find('div', {'class': 'summary'}).find('a').text
        date = (item.find('div', {'class': 'user-action-time'}).find('span').get('title'))[:19]
        print(question)
        print(date)
        print(assign_date())
    return question, date


print(making_request())
