class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita, quantita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.quantita = quantita
        
    def traccia(self):
        return f"{self.nome} e'stato prodotto al costo di produzione: {self.costo_produzione}"
        
        
        
    def calcola_profitto(self):
        
        profitto = (self.prezzo_vendita * self.quantita) - (self.costo_produzione * self.quantita)
        return profitto
    
class Abbligliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, tipo):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.tipo = tipo
        
    def traccia(self):
        super().traccia()
        return f"Abbigliamento '{self.nome}' e'stato prodotto al costo di produzione: {self.costo_produzione}, Tipo: {self.tipo}"

        
    def set_abbigliamento(self, nome, costo_produzione, prezzo_vendita, tipo):
         self.nome = nome
         self.costo_produzione = costo_produzione
         self.prezzo_vendita = prezzo_vendita
         self.tipo = tipo
         return f"Abbigliamento '{self.nome}' aggiornato."
     
    def get_abbigliamento(self):
         return f"Nome: {self.nome}, Costo produzione: {self.costo_produzione}, Prezzo vendita: {self.prezzo_vendita}, Tipo: {self.tipo}"
        
        
        
class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, marca):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.marca = marca
        
    def set_elettronica(self, nome, costo_produzione, prezzo_vendita, marca):
         self.nome = nome
         self.costo_produzione = costo_produzione
         self.prezzo_vendita = prezzo_vendita
         self.marca = marca
         return f"Elettronica '{self.nome}' aggiornata."
     
    def traccia(self):
        super().traccia()
        return f"Elettronica '{self.nome}' e'stato prodotto al costo di produzione: {self.costo_produzione}, Marca: {self.marca}"
     
    def get_elettronica(self):
         return f"Nome: {self.nome}, Costo produzione: {self.costo_produzione}, Prezzo vendita: {self.prezzo_vendita}, Marca: {self.marca}"
    
    

# Creazione di un prodotto
prodotto1 = Prodotto("Prodotto 1", 100, 200, 2)

# Calcolo del profitto
profitto1 = prodotto1.calcola_profitto()

print(f"Il profitto del prodotto '{prodotto1.nome}' è: {profitto1}")

class Fabbrica:
    def __init__(self):
        self.inventario = {}
        
    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto in self.inventario:
            self.inventario[prodotto] += quantita
        else:
            self.inventario[prodotto] = quantita
            
    def vendi_prodotto(self, prodotto, quantita ):
        
        if prodotto in self.inventario and self.inventario[prodotto] >= quantita:
            self.inventario[prodotto] -= quantita
            profitto = prodotto.calcola_profitto()
            print(f"Venduto {quantita} {prodotto}, profitto: {profitto}")
        else:
            print(f"Non posso vendere {quantita} {prodotto}, non ho abbastanza.")
            
            
    def resi_prodotto(self, prodotto, quantita):
        if prodotto in self.inventario:
            self.inventario[prodotto] += quantita
            print(f"Reso {quantita} {prodotto}.")
        else:
            print(f"Non posso reso {quantita} {prodotto}, non esiste.")
            
    
            
            
#TEST 
fabbrica = Fabbrica()


prodotto1 = Prodotto("Prodotto 1", 100, 200, 2)
prodotto2 = Prodotto("Prodotto 2", 150, 250,2 )


maglia= Abbligliamento()
produzione = Fabbrica(maglia)
fabbrica.aggiungi_prodotto()

fabbrica.aggiungi_prodotto(prodotto1, 50)
fabbrica.aggiungi_prodotto(prodotto2, 30)

fabbrica.vendi_prodotto(prodotto1, 20)