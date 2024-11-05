class ContoBancario:
    def __init__(self, titolare, saldo=0.0):
        # Attributi privati
        self.__titolare = titolare if isinstance(titolare, str)  else None
        self.__saldo = saldo 

    
    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Deposito di {importo} completato.")
        else:
            print("L'importo deve essere positivo per effettuare un deposito.")

    
    def preleva(self, importo):
        if self._ContoBancario__test() == True:
            if self.__saldo >= importo:
                self.__saldo -= importo
                print(f"Prelievo di {importo} completato.")
            else:
                print("Saldo insufficiente per il prelievo.")
        else:
            print("L'importo deve essere positivo per effettuare un prelievo.")

    
    def visualizza_saldo(self):
        return f"Saldo corrente: {self.__saldo}"

    # Getter per l'attributo titolare
    def get_titolare(self):
        return self.__titolare

    # Setter per l'attributo titolare con validazione
    def set_titolare(self, nuovo_titolare):
        if isinstance(nuovo_titolare, str) :
            self.__titolare = nuovo_titolare
            print("Nome del titolare aggiornato.")
        else:
            print("Nome del titolare non valido.")
            
    def __test(self):
        print("Eseguendo il metodo di test interno...")
        # Puoi inserire qui i controlli che desideri
        if  self.__saldo > 0:
            print("Conto valido.")
            self.x = True
            return self.x
        else:
            print("Conto non valido.")
            
            
            


conto = ContoBancario("Mario Rossi", 1000)
conto.deposita(500)
conto.preleva(200)
print(conto.visualizza_saldo())
conto.set_titolare("Luigi Bianchi")
print("Titolare:", conto.get_titolare())
conto._ContoBancario__test() #metodo name mangling per accesso forzato non convenzionale

