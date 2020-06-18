import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Card_Game.settings')
django.setup()

from Card_Game_App.models import PokeType, Pokemon
import requests

for num in range(1,808):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{num}")
    diction = response.json()

    pokemon, created = Pokemon.objects.get_or_create(name=diction['name'])
    pokemon.pokexp = diction['base_experience']
    if pokemon.pokexp >= 300:
        pokemon.pokexp = 'legendary'
    elif pokemon.pokexp >= 200:
        pokemon.pokexp = 'ultra-rare'
    elif pokemon.pokexp >= 100:
        pokemon.pokexp = 'rare'
    elif pokemon.pokexp >= 61:
        pokemon.pokexp = 'uncommon'
    elif pokemon.pokexp <= 60:
        pokemon.pokexp = 'common'
    pokemon.save()

    for type in diction['types']:
        types = type['type']['name']
        poketype, created = PokeType.objects.get_or_create(name=types)
        pokemon.types.add(poketype)



