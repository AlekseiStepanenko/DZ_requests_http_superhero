from pprint import pprint

import requests


def dz_requests():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    if response.status_code > 200:
        print (f'Запрос не успешный')
    if response.status_code == 200:
        # pprint(response.json())
        list_superhero = response.json()
        dict_intelligence = {}
        for hero in list_superhero:
            if hero['name'] == 'Hulk' or hero['name'] == 'Captain America' or hero['name'] == 'Thanos':
                dict_intelligence[hero['name']] = hero['powerstats']['intelligence']


        print(f'Самый умный супергерой - {max(dict_intelligence)}')


if __name__ == '__main__':
    dz_requests()