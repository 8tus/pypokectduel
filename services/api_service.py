# services/api_service.py
import requests

BASE_URL = "https://pokeapi.co/api/v2"
POKEMON_ENDPOINT = 'pokemon'
TOTAL_POKEMON_COUNT = 1302

class APIService:
    def get_pokemon_by_id(self, id, params=None):
        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(f"{BASE_URL}/{POKEMON_ENDPOINT}/{id}", headers=headers, params=params)
            response.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa
            return response.json()  # Devuelve la respuesta en formato JSON
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar la solicitud: {e}")
            return None
