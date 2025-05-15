import json
import requests

class Gestorjson:
    def __init__(self,arch):
        self.arch = arch

    def leer_json(self):
        try:
            with open(self.arch, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Archivo no existe")
            return {}
        except json.JSONDecodeError():
            print("El archivo no es Json")
            return {}

    def escribir_json(self,datos):
        try:
            with open(self.arch, 'w') as f: 
                return json.dump(datos, f, indent=4)
        except FileNotFoundError:
            print("Archivo no existe")
            return {}
        except json.JSONDecodeError():
            print("El archivo no es Json")
            return {}
        
    def modificar_json(self, llave, valor):
        datos = self.leer_json()
        datos[llave] = valor
        self.escribir_json(datos)

    def obtener_pokemon(self, pokemon):
        try:   
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            self.escribir_json(data)
        except requests.exceptions.HTTPError:
            print("El enlace no existe")
        except requests.exceptions.RequestException:
            print("No se pudo realizar la peticion")

gJson = Gestorjson("pokemon.json")
gJson.obtener_pokemon("Lopunny")
pokemon_info = gJson.leer_json()
#print(pokemon_info)
tipos = [tipo["type"]["name"] for tipo in pokemon_info.get("types", [])]
movimientos = [move["move"]["name"]for move in pokemon_info.get("moves", [])]
print(f"Nombre del pokemon: {pokemon_info.get('name')}")
print(f"Altura: {pokemon_info.get('height')}m")
print(f"Peso: {pokemon_info.get('weight')} g")
print(f"Id en la pokedex: {pokemon_info.get('id')}")
print(f"Tipo: {', '.join(tipos)}")
print(f"Movimientos: {", ".join(movimientos)}")
