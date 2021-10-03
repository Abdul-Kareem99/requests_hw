from pprint import pprint
import requests


def best_hero(url, heroes):
    dict_intelligense = {}
    default_intelligense = 0
    best_hero = ''
    for i in heroes:
        url_request = url + i
        resp = requests.get(url=url_request)
        param_hero = resp.json()
        param_id = param_hero['results'][0]['powerstats']['intelligence']
        print(f'Интеллект {i}: {param_id}')
        dict_intelligense[i] = param_id
    for hero, intell in dict_intelligense.items():
        if int(intell) > default_intelligense:
            default_intelligense = int(intell)
            best_hero = hero
    print(f'Самый высокий интеллект у героя: {best_hero}!')


url = 'https://superheroapi.com/api/2619421814940190/search/'
heroes = ['Hulk', 'Thanos', 'Captain America']
best_hero(url, heroes)

