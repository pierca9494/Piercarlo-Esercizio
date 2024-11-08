import numpy as np

class SlicingArray:
    def __init__(self):
        self.array = np.random.randint(10, 50, 20)
    
    def primi_n_elementi(self, n):
        return self.array[:n]
    
    def ultimi_n_elementi(self, n):
        return self.array[-n:]
    
    def elementi_intervallo(self, start, end):
        return self.array[start:end]
    
    def ogni_terzo_elemento(self):
        risultato = []
        for arr in [self.array, self.primi_n_elementi(10), self.ultimi_n_elementi(5), self.elementi_intervallo(5, 15)]:
            if len(arr) > 2:  
                risultato.append(arr[2])
        return np.array(risultato)
    
    def modifica_elementi(self):
        self.array[5:10] = 99
        return self.array

# Funzione principale per eseguire l'applicazione
def esegui_applicazione():
    slicing_array = SlicingArray()
    print("Array originale:", slicing_array.array)
    
    while True:
        print("\nSeleziona un'opzione:")
        print("0. Visualizza  lista originale")
        print("1. Visualizza i primi N elementi")
        print("2. Visualizza gli ultimi N elementi")
        print("3. Visualizza elementi in un intervallo specifico")
        print("4. Visualizza il terzo elemento di ogni array")
        print("5. Modifica elementi 5-10 a 99")
        print("6. Esci")
        
        scelta = input("Scegli un'opzione: ")
        
        
        if scelta == '0':
            print("Array originale:", slicing_array.array)
        
        
        elif scelta == '1':
            n = int(input("Quanti elementi vuoi visualizzare dal primo? "))
            print("Primi", n, "elementi:", slicing_array.primi_n_elementi(n))
        
        elif scelta == '2':
            n = int(input("Quanti elementi vuoi visualizzare dalla fine? "))
            print("Ultimi", n, "elementi:", slicing_array.ultimi_n_elementi(n))
        
        elif scelta == '3':
            start = int(input("Indice di inizio dell'intervallo: "))
            end = int(input("Indice di fine dell'intervallo escluso: "))
            print("Elementi da", start, "a", end, ":", slicing_array.elementi_intervallo(start, end))
        
        elif scelta == '4':
            print("Terzo elemento di ogni array:", slicing_array.ogni_terzo_elemento())
        
        elif scelta == '5':
            print("Array con elementi 5-10 modificati:", slicing_array.modifica_elementi())
        
        elif scelta == '6':
            print("Uscita dal programma.")
            break
        
        else:
            print("Opzione non valida. Riprova.")

# Avvio dell'applicazione
esegui_applicazione()
