class Animale:
    def __init__(self, nome, eta, specie):
        self.nome = nome
        self.eta = eta
        self.specie = specie

    def fai_suono(self):
        print("Suono generico dell'animale")

class Leone(Animale):
    def __init__(self, nome, eta, specie):
        super().__init__(nome, eta)
        self.specie = specie
        
        

    def fai_suono(self):
        print("Il leone ruggisce")

    def caccia(self):
        print(f"{self.nome} sta cacciando")

class Giraffa(Animale):
    def __init__(self, nome, eta, specie):
        super().__init__(nome, eta)
        self.specie = specie
        
        

    def fai_suono(self):
        print("La giraffa emette un suono particolare")

    def bruca(self):
        print(f"{self.nome} sta brucando le foglie")

class Pinguino(Animale):
    def __init__(self, nome, eta, specie):
        super().__init__(nome, eta)
        self.specie = specie

    def fai_suono(self):
        print("Il pinguino emette un suono squillante")

    def nuota(self):
        print(f"{self.nome} sta nuotando")

# Creazione di istanze di ogni animale
leone = Leone("Simba", 5)
giraffa = Giraffa("Melman", 8)
pinguino = Pinguino("Pingu", 3)

# Test dei metodi
leone.fai_suono()
leone.caccia()

giraffa.fai_suono()
giraffa.bruca()

pinguino.fai_suono()
pinguino.nuota()
