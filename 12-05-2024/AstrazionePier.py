from abc import ABC, abstractmethod


class Veicolo(ABC):
    def __init__(self, marca, modello, anno):
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._accensione = False

    def get_marca(self):
        return self._marca

    def get_modello(self):
        return self._modello

    def get_anno(self):
        return self._anno

    def get_accensione(self):
        return self._accensione

    def toggle_accensione(self):
        self._accensione = not self._accensione

    def accendi(self):
        if not self.get_accensione():
            self.toggle_accensione()

    def spegni(self):
        if self.get_accensione():
            self.toggle_accensione()

    @abstractmethod
    def mostra_informazioni(self):
        print(f"Veicolo marca {self.get_marca()}, modello {self.get_modello()}, anno {self.get_anno()}")


class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self._tipo = tipo

    def mostra_informazioni(self):
        super().mostra_informazioni()
        print(f"Tipo: {self._tipo}")


    def esegui_wheelie(self):
        if self._tipo.lower() == "sportiva":
            print("La motocicletta sportiva sta facendo un'impennata!")
        else:
            print("Questo tipo di motocicletta non è adatto per le impennate.")
            


    
class ParcoVeicoli:
    def __init__(self):
        self._veicoli = []

    def aggiungi_veicolo(self, veicolo):
        if isinstance(veicolo, Veicolo):
            self._veicoli.append(veicolo)
            print(f"{veicolo._marca} {veicolo._modello} aggiunto al parco veicoli.")
        else:
            print("Errore: L'oggetto non è un veicolo valido.")

    def rimuovi_veicolo(self, marca, modello):
        for veicolo in self._veicoli:
            if veicolo._marca == marca and veicolo._modello == modello:
                self._veicoli.remove(veicolo)
                print(f"{marca} {modello} rimosso dal parco veicoli.")
                return
        print(f"{marca} {modello} non trovato nel parco veicoli.")

    def lista_veicoli(self):
        if not self._veicoli:
            print("Il parco veicoli è vuoto.")
        else:
            for veicolo in self._veicoli:
                print(veicolo.mostra_informazioni())
         
        


                
                

moto = Motocicletta("Yamaha", "R1", 2020, "sportiva")

# Creazione del gestore parco veicol

# Aggiunta dei veicoli al parco


print(moto.mostra_informazioni())

# Lista di tutti i veicoli



