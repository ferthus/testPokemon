from django.shortcuts import render
from .rest import *
from django.contrib.auth.decorators import login_required
#from testPokemon.pokeApp import views

# class PokemonAppView():
def index(request):#si no es get return negacion 
    if request.method == 'GET':
        pokemons= getPokemon()
        context = {
              'pokemones':pokemons
        }
        return render(request,'pokemonApp/index.html',context)
    else:
        return False 
        
def pokemonView(request):
    if request.method == 'GET':
        pokemon_id = request.GET['id']
        types,abilities = getInfo(pokemon_id)    
        context = {
                    'types':types,
                    'abilities':abilities
                   }      
        return render(request,'pokemonApp/pokemonView.html',context)
    else:
        return False 

def pokemonType(request):
    if request.method == 'GET':
        type_id = request.GET['id']
        pokemonts = getType(type_id)                                                      
        context = {
                    'pokemonts':pokemonts
        }

        return render(request,'pokemonApp/pokemonType.html',context)
    else:
        return False 

@login_required(login_url='/login')
def pokemon_Type(request,id):
    if request.method == 'GET':
        pokemonts = getType(id)                                                      
        context = {
            'pokemonts':pokemonts
        }

        return render(request,'pokemonApp/pokemonType.html',context)
    else:
        return False 


def pokemon_View(request,id):
    if request.method == 'GET':
        types,abilities,image = getInfo(id)    
        context = {
                'types':types,
                'abilities':abilities,
                'image':image,

        }      
        return render(request,'pokemonApp/pokemonView.html',context)
    else:
        return False 

def login(request):
    return render(request,'pokemonApp/login.html')