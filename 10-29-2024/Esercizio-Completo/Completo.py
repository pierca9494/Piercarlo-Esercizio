# Punto 1: Utilizzo di if
def pari_dispari(numero):
    if numero % 2 == 0:
        print("Pari")
    else:
        print("Dispari")

# Esempio di utilizzo
pari_dispari(4)  # Output: Pari


# Punto 2: Utilizzo di while e range
def countdown(n):
    while n >= 0:
        print(n)
        n -= 1
    # Questo ciclo può continuare all'infinito, per ora fermiamolo con un valore iniziale di `n`

# Esempio di utilizzo
countdown(10)  # Output: 10 9 8 ... 0


# Punto 3: Utilizzo di for
def quadrato_numeri(lista):
    for numero in lista:
        print(numero ** 2)

# Esempio di utilizzo
quadrato_numeri([1, 2, 3])  # Output: 1 4 9


# Punto 4: Utilizzo di if, while e for insieme
def analisi_lista(lista):
    if not lista:
        print("Lista vuota")
        return
    
    # Trovare il numero massimo nella lista
    massimo = lista[0]
    for numero in lista:
        if numero > massimo:
            massimo = numero

    # Contare il numero di elementi nella lista
    conteggio = 0
    while conteggio < len(lista):
        conteggio += 1

    # Stampare i risultati
    print(f"Numero massimo: {massimo}")
    print(f"Numero di elementi: {conteggio}")

# Esempio di utilizzo
analisi_lista([10, 3, 5, 8])  # Output: Numero massimo: 10, Numero di elementi: 4
analisi_lista([])  # Output: Lista vuota
