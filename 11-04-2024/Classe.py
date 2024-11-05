class Automobile:
    numero_di_ruote = 4 
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    def stampa_info (self):
     print(f"Marca: {self.marca}, Modello: {self.modello}, Numero di ruote: {self.numero_di_ruote}")