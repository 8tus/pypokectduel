from models import Pokemon

class DataService:
    """Clase para manejar y procesar los datos obtenidos de la API."""

    @staticmethod
    def build_pokemon(data):
        id = data['url'].split('/')[-1]
        return Pokemon()
    
'''
https://pokeapi.co/api/v2/pokemon/1/
{'name': 'bulbasaur', 'url': 'https://pokeapi.co/api/v2/pokemon/1/'}
'''