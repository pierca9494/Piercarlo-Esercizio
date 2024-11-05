def compressione_efficiente(func):
    def wrapper():
        stringa = func()
        risultato = ""
        conteggio = 1

        
        for i in range(len(stringa) - 1):
            if stringa[i] == stringa[i + 1]:
                conteggio += 1
            else:
                risultato += stringa[i] + str(conteggio)
                conteggio = 1

        # Aggiunge l'ultimo carattere e il suo conteggio
        risultato += stringa[-1] + str(conteggio)

        # Restituisce la stringa compressa solo se è più corta dell'originale
        return risultato if len(risultato) < len(stringa) else stringa
    return wrapper

@compressione_efficiente
def comprimi_stringa():
    # Chiede all'utente di inserire una stringa da comprimere
    return input("Inserisci una stringa da comprimere: ")

# Esempio di utilizzo
print(comprimi_stringa())
