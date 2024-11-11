import random

# Parte 1: Generazione dei numeri casuali e salvataggio nel file
def genera_numeri():
    numeri = random.sample(range(1, 100), 5)  
    with open("numeri.txt", "w") as file:
        for numero in numeri:
            file.write(f"{numero}\n")
    print("Numeri casuali generati e salvati su 'numeri.txt'.")

# Parte 2: Lettura dei numeri dal file e tentativi di indovinare
def indovina_numeri():
    # Lettura dei numeri salvati
    with open("numeri.txt", "r") as file:
        numeri_salvati = [int(line.strip()) for line in file.readlines()]

    # Richiesta di input all'utente
    tentativi = 5  # L'utente ha 5 tentativi per indovinare
    numeri_indovinati = 0

    print("Prova a indovinare i numeri! Inserisci numeri tra 1 e 100.")
    for _ in range(tentativi):
        try:
            guess = int(input("Inserisci un numero: "))
            if guess in numeri_salvati:
                numeri_indovinati += 1
                numeri_salvati.remove(guess)  # Rimuove il numero già indovinato
                print("Bravo! Numero corretto.")
            else:
                print("Numero sbagliato.")
        except ValueError:
            print("Inserisci un numero valido.")

    # Controllo dei risultati
    if numeri_indovinati >= 2:
        print("Complimenti! Hai indovinato almeno 2 numeri e hai vinto.")
    else:
        print("Peccato, non hai indovinato abbastanza numeri. Hai perso.")

# Esecuzione delle funzioni
genera_numeri()
indovina_numeri()
