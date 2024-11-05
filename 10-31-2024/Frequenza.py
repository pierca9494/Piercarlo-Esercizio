def calcola_frequenza_caratteri(stringa):
    frequenza = {}
    for carattere in stringa:
        if carattere in frequenza:
            frequenza[carattere] += 1
        else:
            frequenza[carattere] = 1
    return frequenza


stringa = input("Inserisci una stringa: ")

risultato = calcola_frequenza_caratteri(stringa)

# Output del risultato
print("Frequenza dei caratteri:", risultato)
