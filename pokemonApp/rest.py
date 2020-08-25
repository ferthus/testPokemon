import requests

def getPokemon():
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results',[])
    return results

def getInfo(id):
    url = 'https://pokeapi.co/api/v2/pokemon/'+id
    response = requests.get(url)
    if response.status_code == 200:
        informat = response.json()
        types = informat.get('types',[])
       
    return types

