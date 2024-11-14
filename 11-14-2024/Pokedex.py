import requests
import json
import random

# Percorso del file pokedex.json
POKEDEX_FILE = "pokedex.json"

# Funzione per caricare il Pokédex da file
def load_pokedex():
    try:
        with open(POKEDEX_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Funzione per salvare il Pokédex su file
def save_pokedex(pokedex):
    with open(POKEDEX_FILE, "w") as f:
        json.dump(pokedex, f, indent=4)

# Funzione per ottenere un Pokémon casuale dall'API
def get_random_pokemon():
    pokemon_id = random.randint(1, 1008)  # Numero massimo di Pokémon attualmente
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "id": data["id"],
            "name": data["name"],
            "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
            "base_experience": data["base_experience"],
            "weight": data["weight"],
            "height": data["height"]
        }
    else:
        print("Errore nel recupero del Pokémon.")
        return None

# Funzione principale per simulare il Pokédex
def main():
    pokedex = load_pokedex()
    
    # Ottenere un Pokémon casuale
    pokemon = get_random_pokemon()
    if pokemon is None:
        return  # Esce se non è stato possibile ottenere il Pokémon
    
    pokemon_id = str(pokemon["id"])
    
    # Verifica se il Pokémon è già nel Pokédex
    if pokemon_id in pokedex:
        print(f"Hai già catturato {pokemon['name']}!")
    else:
        print(f"Hai incontrato un nuovo Pokémon: {pokemon['name']}!")
        print("Dettagli:")
        print(f" - Abilità: {', '.join(pokemon['abilities'])}")
        print(f" - Esperienza base: {pokemon['base_experience']}")
        print(f" - Peso: {pokemon['weight']} hg")
        print(f" - Altezza: {pokemon['height']} dm")
        
        # Chiedi se l'utente vuole catturarlo
        capture = input("Vuoi catturarlo? (s/n): ").strip().lower()
        if capture == 's':
            # Aggiungi il Pokémon al Pokédex
            pokedex[pokemon_id] = pokemon
            save_pokedex(pokedex)
            print(f"Hai catturato {pokemon['name']}!")
        else:
            print(f"Hai deciso di non catturare {pokemon['name']}.")

if __name__ == "__main__":
    main()
