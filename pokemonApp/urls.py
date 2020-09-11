from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name ='index'),
    #path('index',views.index , name = 'index'),
    path('pokemonView',views.pokemonView, name ='pokemonView'),
    path('pokemonType',views.pokemonType,name='pokemonType'),
    path('pokemon_Type/<int:id>/',views.pokemon_Type,name='pokemon_Type'),
    path('pokemon_View/<int:id>/',views.pokemon_View, name ='pokemon_View'),
    path('login/',views.login,name='login')
    
    
]