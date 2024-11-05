def punteggio(partecipante):
    #Otteniamo il punteggio del partecipante
    return partecipante['punteggio']

def classifica(partecipanti):
    # Ordina i partecipanti in base al punteggio
    classifica = sorted(partecipanti, key=punteggio, reverse=True)
    print("Classifica finale:")
    for i in range(len(classifica)):
        nome = classifica[i]['nome']
        punteggio = classifica[i]['punteggio']
        print(f"{i + 1}. {nome} {punteggio} punti")