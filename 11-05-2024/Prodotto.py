class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        
        
    def calcola_profitto(self, prezzo_vendita, costo_produzione, quantita):
        return self.prezzo_vendita - self.costo_produzione
    
class Abbligliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, tipo):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.tipo = tipo
        
class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, marca):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.marca = marca
    
    

# Creazione di un prodotto
prodotto1 = Prodotto("Prodotto 1", 100, 200)

# Calcolo del profitto
profitto1 = prodotto1.calcola_profitto()

print(f"Il profitto del prodotto '{prodotto1.nome}' è: {profitto1}")