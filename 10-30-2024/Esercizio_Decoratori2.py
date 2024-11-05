def compressione_efficiente(func):
    def wrapper():
        
        risultato = func()
        
        return risultato if len(risultato) < len(stringa) else stringa
    

    return wrapper

def inserire(func):
    def wrapper():
        
        
        
        return risultato
        
    print("Inserisci una stringa da comprimere:")
        
    return wrapper    

@compressione_efficiente
@inserire
def comprimi_stringa():
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
    
    

# Esempio di utilizzo
