import Prodotto

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
            profitto = prodotto.calcola_profitto(prodotto.nome, prodotto.costo_produzione, prodotto.prezzo_vendita, prodotto[quantita])
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


prodotto1 = Prodotto.Prodotto("Prodotto 1", 100, 200)
prodotto2 = Prodotto.Prodotto("Prodotto 2", 150, 250)

fabbrica.aggiungi_prodotto(prodotto1, 50)
fabbrica.aggiungi_prodotto(prodotto2, 30)

fabbrica.vendi_prodotto(prodotto1, 20)
            
        
        
            
            
        