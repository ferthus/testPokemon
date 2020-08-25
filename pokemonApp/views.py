from django.shortcuts import render
from .rest import getPokemon,getInfo
import re


def urlPoke(url):
    ide = re.findall('\d+', url)
    id = ide[1]
    return id
# Create your views here.
class PokemonAppView():
    def index(self,request):
        pokemons= getPokemon()
        context = {
            'pokemones':pokemons
        }
        return render(request,'pokemonApp/index.html',context)
    
    def pokemonView(self,request):
        url = request.GET.get('url')
        urlid = urlPoke(url)
        info = getInfo(urlid)
        context = {
            'informacion':info
        }
        return render(request,'pokemonApp/pokemonView.html',context)