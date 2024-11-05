import random


class Gioco:
    global lista_domande
    lista_domande = [
        ["Quanti lati ha un dodecagono?", "12", 1],
        ["Come si chiama l'angolo compreso tra 90 e 180 gradi?", "Ottuso", 1],
        ["Quale espressione usata da Archimede si può tradurre in 'Ho trovato'?", "Eureka", 2],
        ["Se moltiplicassi tutti i numeri su una tastiera telefonica quale numero otterresti?", "0", 1],
        ["Quale lettera dell'alfabeto si usa in matematica per esprimere il numero che elevato al quadrato è uguale a -1?", "i", 3],
        ["La base esadecimale si compone di cifre che cominciano per quale stringa?", "0x", 2],
        ["Quali sono le prime due cifre decimali del Pi Greco?", "14", 2],
        ["Come si chiamano i numeri che sono divisibili solo per 1 e per se stessi?", "Primi", 1],
        ["Qual è il cognome del matematico che si dice abbia inventato l'informatica?", "Turing", 3]
    ]

    print("fin qui tutto bene")
    ## domande contiene liste del tipo (domanda str, risposta str, valore della domanda int)

    def __init__(self):
        self.punteggio = 0
        self.lista = []
        
        print("Classe inizializzata")

    def domande(self, n = 5):

        print("Parto con le domande")
        domande_giocatore = []
        copia_lista_domande = lista_domande

        for indice in range(0, n):
            random_num = random.randint(0, len(copia_lista_domande))
            ## print(str(random_num))
            domande_giocatore.append(copia_lista_domande[random_num])
            copia_lista_domande.pop(random_num)

        self.lista = domande_giocatore

    def corretta(self, valore):
        print("Si, è corretta")
        self.punteggio += valore

    def return_punteggio(self):
        return self.punteggio
    
    def return_lista(self):
        return self.lista

    def fine(self):
        pass
        ## todo, forse elimina

    def printami(self):
        lista_printabile = self.return_lista()
        for domanda in lista_printabile:
            print(domanda)




mygame = Gioco()
mygame.domande()
mygame.printami()