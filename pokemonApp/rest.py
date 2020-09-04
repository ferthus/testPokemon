import requests
import re

def urlPoke(url):
    ide = re.findall('\d+', url)
    id = ide[1]
    return id

def getPokemon():
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results',[])
        if results:
            for pokemon in results:
                name = pokemon['name']
                url = pokemon['url']
                urls = urlPoke(url)
                pokemon['id'] = urls

    return results

def getInfo(id):
    url = 'https://pokeapi.co/api/v2/pokemon/'+id
    response = requests.get(url)
    if response.status_code == 200:
        informat = response.json()
        types = informat.get('types',[])
       
    return types

