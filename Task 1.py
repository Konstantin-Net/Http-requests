import requests

smartest = {}   # Словарь для добавления героев по интеллекту
hero = ['Hulk', 'Captain America', 'Thanos']
for person in hero:     # В цикле проходим по героям из списка и добавляем в словарь данные по интеллекту каждого
    url = f'https://superheroapi.com/api/2619421814940190/search/{person}'
    resp = requests.get(url)
    intelligence = int(resp.json()['results'][0]['powerstats']['intelligence'])
    smartest[intelligence] = person

print(f"Интеллект участников: {smartest}")
print(f"Cамый умный - {smartest[max(smartest.keys())]}")
