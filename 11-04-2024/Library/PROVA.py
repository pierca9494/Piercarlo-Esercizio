import Libro

class Biblioteca:
    def __init__(self):
        self.libri = []
        
    def aggiungi_libro(self, titolo, autore, pagine):
        libro = Libro.Libro(titolo, autore, pagine)
        self.libri.append(libro)
        
    def elenca_libri(self):
        
        if not self.libri:
            print("Nessun libro aggiunto")
        else:
            
            for libro in self.libri:
                print(libro.descrizione())
                
biblioteca = Biblioteca()

# Aggiunta di libri
while True:
    titolo = input("Inserisci il titolo del libro (o scrivi 'stop' per terminare): ")
    if titolo.lower() == 'stop':
        break
    autore = input("Inserisci l'autore del libro: ")
    pagine = int(input("Inserisci il numero di pagine del libro: "))
    biblioteca.aggiungi_libro(titolo, autore, pagine)

# Stampa di tutti i libri nella biblioteca
biblioteca.elenca_libri()

