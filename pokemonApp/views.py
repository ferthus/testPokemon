from django.shortcuts import render
from .rest import *

# class PokemonAppView():
def index(request):
    if request.method == 'GET':
        pokemons= getPokemon()
        context = {
            'pokemones':pokemons
        }
        return render(request,'pokemonApp/index.html',context)
        
def pokemonView(request):
    pokemon_id = request.GET['id']
    types,abilities = getInfo(pokemon_id)    
    context = {
            'types':types,
            'abilities':abilities

        }      
    return render(request,'pokemonApp/pokemonView.html',context)

def pokemonType(request):
    type_id = request.GET['id']
    pokemonts = getType(type_id)
    context = {
        'pokemonts':pokemonts
    }

    return render(request,'pokemonApp/pokemonType.html',context)
