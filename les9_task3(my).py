import requests
from datetime import datetime
import time


class GetPythonFromStackoverflow:
    # специализированный класс для получения информации с сайта Stackoverflow по тэгу "Python"

    def __init__(self, section, tag):
        self.section = section
        self.tag = tag
        # создадим время в секундах для формата UNIX_TIME
        self.AMOUNT_DAYS_AGO_IN_SECONDS = int(time.time()) - int(input("За сколько дней вывести сведения? ")) * 60 * 60 * 24
        page = 1
        while True:
            # возможно следующий блок можно вынести в функцию.. пока не определился
            self.BASE_API_URL = 'https://api.stackexchange.com/2.2'
            self.get_url = self.BASE_API_URL + section
            params = self.params_get(self.BASE_API_URL, self.section, self.tag, page)
            base_request = requests.get(self.get_url, params=params)
            for question in base_request.json()['items']:
                if question['creation_date'] > self.AMOUNT_DAYS_AGO_IN_SECONDS:
                    print(datetime.fromtimestamp(question['creation_date']))
                    print(question['title'])
                else:
                    break
            if question not in base_request.json()['items']:
                break
            print(page)
            print()
            page += 1

    def params_get(self, url, section, tag, page):
        if section == '/questions':
            # page = 1
            params_dict = {'fromdate': self.AMOUNT_DAYS_AGO_IN_SECONDS,
                           'tagged': tag, 'site': 'stackoverflow', 'sort': 'creation', 'page': page}
        elif section == '/tags':
            # nonlocal get_url
            self.get_url = f'{url}{section}{tag}/faq'
            params_dict = {'site': 'stackoverflow'}
        return params_dict


def main():
    # Основный цикли программы

    print("Выберете один из разделов который хотите просмотреть:")
    question = input("1 - вопросы, 2 - упоминания по тэгам\n")
    if question == '1':
        GetPythonFromStackoverflow('/questions', '/python')
    elif question == '2':
        print("Уточнение: за последнии 1000 дней было всего 2 упоминания.")
        print("Используйте эту информацию при выборе количества дней.")
        GetPythonFromStackoverflow('/tags', '/python')
    else:
        print("Вы не выбрали один из двух вариантов. Программа будет закрыта.")
        print("Спасибо за использование данной программы.")


main()