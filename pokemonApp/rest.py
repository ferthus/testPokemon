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
        abilities = informat.get('abilities',[]) 
        types = informat.get('types',[])
        if types:
            for typ in types:
                name = typ['type']['name']
                url = typ['type']['url']
                urls = urlPoke(url)
                typ['type']['id'] = urls
       
    return types,abilities

def getType(id):
    url = 'https://pokeapi.co/api/v2/type/'+id
    response = requests.get(url)
    if response.status_code == 200:
        type_result = response.json()
        pokemons = type_result.get('pokemon',[])

    return pokemons