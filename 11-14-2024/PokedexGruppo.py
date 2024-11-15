import json, requests, random
from pprint import pprint

class Pokedex():

    def __init__(self,nome = "Pokedex"):

        self.nome = nome
        self.pokedex = self.carica_pokedex()

    def aggiungi_pokemon(self, pokemon_selvatico):
        
        for elemento in self.pokedex:

            if pokemon_selvatico.id not in elemento:
                        
                self.pokedex[pokemon_selvatico.id] = {"nome" : pokemon_selvatico.nome,
                                    "hp": pokemon_selvatico.hp,
                                    "abilità" : pokemon_selvatico.abilità,
                                    "xp" : pokemon_selvatico.xp,
                                    "altezza" : pokemon_selvatico.altezza,
                                    "peso" : pokemon_selvatico.peso,
                                    "abilità_attiva" : pokemon_selvatico.abilità_attiva,
                                    "attacco" : pokemon_selvatico.attacco,
                                    "difesa" : pokemon_selvatico.difesa}
                print(f"{pokemon_selvatico.nome} aggiunto al {self.nome}!")


    def pokemon_iniziale(self):


        if self.pokedex != {}:

            id = random.randint(1,1025)
            pokemon = Pokemon(id)

            if id not in self.pokedex:
                        
                self.pokedex[id] = {"nome" : pokemon.nome,
                                    "hp": pokemon.hp,
                                    "abilità" : pokemon.abilità,
                                    "xp" : pokemon.xp,
                                    "altezza" : pokemon.altezza,
                                    "peso" : pokemon.peso,
                                    "abilità_attiva" : pokemon.abilità_attiva,
                                    "attacco" : pokemon.attacco,
                                    "difesa" : pokemon.difesa}

    def cattura_pokemon(self, pokemon_selvatico, scelta):

        if scelta == "y":

            self.aggiungi_pokemon(self, pokemon_selvatico)

        else:
            
            print(f"{pokemon_selvatico.nome} va via.")

    def carica_pokedex():
    
        try:
            pokedex_file = "pokedex.json"
            with open(pokedex_file,"r") as file:
                pokedex = json.load(file)
            
            return pokedex
        
        except:
            print("File pokedex non trovato, creazione in corso.") 
            pokedex = {}
            print("File pokedex creato.")

            return pokedex

    def salva_pokedex(pokedex):

        pokedex_file = "pokedex.json"
        with open(pokedex_file, "w") as file:
            json.dump(pokedex, file)

    def stampa():
        
        pass

class Gioco():


    def show_random_pokemon():

        id = random.randint(1,1025)
        pokemon_selvatico = Pokemon(id)
        print(f"{pokemon_selvatico.nome} è apparso!")
        scelta = input("Vuoi provare a catturarlo?: ").lower()

        return scelta

        
    def inizia_battaglia(self, pokemon1, pokemon2):
        pass



class Pokemon():

    def __init__(self, id):

        url = f"https://pokeapi.co/api/v2/pokemon/{id}"
        response = requests.get(url)
        data = response.json()
        self.nome = data["forms"][0]["name"]
        self.hp = data["stats"][0]["base_stats"]
        self.abilità = data["abilities"]
        self.xp = data["base_experience"]
        self.altezza = data["height"]
        self.peso = data["weight"]
        self.abilità_attiva = None
        self.attacco =  data["stats"][1]["base_stats"]
        self.difesa =  data["stats"][2]["base_stats"]
        #self.tipo = data["types"][0]["type"]["name"]

    def abilità_attive(self):

        for i in range(self.abilità):
            if self.abilità[i]["is_hidden"] == "true":
                self.abilità_attiva = self.abilità[i]["ability"]["name"]


class Gioco:
    def __init__(self):
        self.pokedex = Pokedex()

    def genera_pokemon_casuale(self):
        id = random.randint(1, 1025)
        url = f"https://pokeapi.co/api/v2/pokemon/{id}"
        response = requests.get(url)
        data = response.json()

        return Pokemon(
            id=str(id),
            nome=data["forms"][0]["name"],
            abilita=[ability["ability"]["name"] for ability in data["abilities"]],
            xp=data["base_experience"],
            altezza=data["height"],
            peso=data["weight"],
            attacco=data["stats"][1]["base_stat"],  # Attack stat
            difesa=data["stats"][2]["base_stat"],   # Defense stat
            velocita=data["stats"][5]["base_stat"] # Speed stat
        )

    def cerca_pokemon(self):
        pokemon = self.genera_pokemon_casuale()
        print(f"{pokemon.nome} è apparso!")
        print(f"Stats: Attacco {pokemon.attacco}, Difesa {pokemon.difesa}, Velocità {pokemon.velocita}")
        return pokemon

    def lotta(self, pokemon1, pokemon2):
        pass

    def gioca(self):
        while True:
            print("\n--- Benvenuto nel Gioco Pokémon ---")
            scelta = input("1. Cerca un nuovo Pokémon\n2. Mostra il Pokedex\n3. Esci\nScegli: ")

            if scelta == "1":
                selvatico = self.cerca_pokemon()
                catturato = input(f"Vuoi affrontare {selvatico.nome}? (y/n): ").lower()
                if catturato == "y":
                    # Usa un Pokémon del Pokedex per la lotta
                    if self.pokedex:
                        tuo_pokemon_id = random.choice(list(self.pokedex.keys()))
                        tuo_pokemon_data = self.pokedex[tuo_pokemon_id]
                        tuo_pokemon = Pokemon(
                            id=tuo_pokemon_id,
                            nome=tuo_pokemon_data["nome"],
                            abilita=tuo_pokemon_data["abilità"],
                            xp=tuo_pokemon_data["xp"],
                            altezza=tuo_pokemon_data["altezza"],
                            peso=tuo_pokemon_data["peso"],
                            attacco=tuo_pokemon_data["attacco"],
                            difesa=tuo_pokemon_data["difesa"],
                            velocita=tuo_pokemon_data["velocità"],
                        )

                        vincitore = self.lotta(tuo_pokemon, selvatico)
                        if vincitore == tuo_pokemon:
                            print(f"Hai sconfitto {selvatico.nome}!")
                            self.pokedex.aggiungi_pokemon(selvatico)
                        else:
                            print(f"{tuo_pokemon.nome} è stato sconfitto!")
                    else:
                        print("Non hai Pokémon nella tua squadra!")

            elif scelta == "2":
                self.pokedex.mostra_pokedex()

            elif scelta == "3":
                print("Grazie per aver giocato!")
                self.pokedex.salva_pokedex()
                break

            else:
                print("Scelta non valida. Riprova.")

# --- Avvio del gioco ---
if __name__ == "__main__":
    gioco = Gioco()
    gioco.gioca()