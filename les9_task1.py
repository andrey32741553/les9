import requests

# resp_hulk = requests.get('https://superheroapi.com/api.php/2619421814940190/search/Hulk')
# resp_cap_am = requests.get('https://superheroapi.com/api.php/2619421814940190/search/Captain America')
# resp_thanos = requests.get('https://superheroapi.com/api.php/2619421814940190/search/Thanos')
#
# # print(resp.json())
#
# h_name = resp_hulk.json()['results'][0]['name']
# hulk_intelligence = resp_hulk.json()['results'][0]['powerstats']['intelligence']
# c_name = resp_cap_am.json()['results'][0]['name']
# resp_cap_am_intelligence = resp_cap_am.json()['results'][0]['powerstats']['intelligence']
# t_name = resp_thanos.json()['results'][0]['name']
# thanos_intelligence = resp_thanos.json()['results'][0]['powerstats']['intelligence']
#
# print(f'{h_name}: {hulk_intelligence}')
# print(f'{c_name}: {resp_cap_am_intelligence}')
# print(f'{t_name}: {thanos_intelligence}')


def making_hero_data_dict():
    count = 1
    hero_data_dict = {}
    while count < 4:
        name = input('Введите имя героя: ')
        response = requests.get(f'https://superheroapi.com/api.php/2619421814940190/search/{name}')
        intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
        hero_data_dict[name] = intelligence
        count += 1
    return hero_data_dict


def find_most_clever():
    hero_dict = making_hero_data_dict()
    max_value = max(hero_dict.values())
    final_dict = {key: value for key, value in hero_dict.items() if value == max_value}
    return final_dict


print(find_most_clever())
