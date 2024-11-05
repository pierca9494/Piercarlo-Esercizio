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
analisi_lista(['ciao', 'pierca', 'eraclio', ])  # Output: Lista vuota