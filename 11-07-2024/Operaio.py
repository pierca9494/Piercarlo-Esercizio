from abc import ABC, abstractmethod

class Operaio:
    def __init__(self, nome, cognome, eta, salario):
        self.__nome = nome
        self.__cognome = cognome
        self.__eta = eta
        self.__salario = salario
        
    def get_nome(self):
        return self.__nome
    
    def get_cognome(self):
        return self.__cognome
    
    def get_eta(self):
        return self.__eta
    
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, salario):
        self.__salario = salario


# Classe astratta Elettricita
class Elettricita(Operaio, ABC):
    
    @abstractmethod
    def installa_impiano_elettrico(self):
        pass
    
# Classe astratta Carrozzeria
class Carrozzeria(Operaio, ABC):
    
    @abstractmethod
    def ripara_carrozzeria(self):
        pass


# Esempio di una classe concreta che estende Elettricita
class ElettricistaConcreto(Elettricita):
    def installa_impiano_elettrico(self):
        print("Impianto elettrico installato")

# Esempio di una classe concreta che estende Carrozzeria
class CarrozziereConcreto(Carrozzeria):
    def ripara_carrozzeria(self):
        print("Carrozzeria riparata")

# Instanziazione di oggetti concreti
elettricista = ElettricistaConcreto("Mario", "Rossi", 30, 2500)
carrozziere = CarrozziereConcreto("Giovanni", "Bianchi", 35, 2200)

# Utilizzo dei metodi concreti
elettricista.installa_impiano_elettrico()  # "Impianto elettrico installato"
carrozziere.ripara_carrozzeria()  # "Carrozzeria riparata"
