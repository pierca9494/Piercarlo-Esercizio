class Veicoli:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        
    
    def stampa_info(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}")
        
class Quad:
    def __init__(self, marca, modello):
        super().__init__(marca, modello)
        self.ruote = 4
        
    