
import sys
import os

# Asegurarse de que el directorio base esté en sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
from services import APIService
from models import Pokemon


api_service = APIService()
pokemon1Json = api_service.get_pokemon_by_id(1)
print(pokemon1Json)