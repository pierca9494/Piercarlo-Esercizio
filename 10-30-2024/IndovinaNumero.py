#genera numero casuale utilizzando range
import random

def Genera_numero():
    numero = random.randint(1, 100)
    return numero


def Input_numero():
    numero_utente = input("Inserisci un numero: ")
    return numero_utente

#controlla se il numero_utente e > o < del numero else e' uguale
def Controlla_numero(numero_utente, numero):
    if numero_utente > numero:
        print("Il numero casuale è minore del numero scelto.")
    elif numero_utente < numero:
        print("Il numero casuale è maggiore del numero scelto.")
    else:
        print("Hai indovinato!")
    

#programma principale
while True:
    numero_casuale = Genera_numero()
    numero_utente = Input_numero()
    
    
    numero_utente = int(numero_utente)
    Controlla_numero(numero_utente, numero_casuale)
    
    
    print("Devi inserire un numero.")
    
    