from django.shortcuts import render
from .rest import getPokemon,getInfo
import re


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
    information = getInfo(pokemon_id)
    context = {
            'information':information
        }      
    return render(request,'pokemonApp/pokemonView.html',context)