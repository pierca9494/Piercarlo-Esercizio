class Computer:
 def __init__(self):
   self.__processore = "Intel i5" # Attributo privato

 def get_processore(self):
   return self.__processore

 def set_processore(self, processore):
   self.__processore = processore

pc = Computer()
print(pc.get_processore()) 
# Accede all'attributo privato tramite il getter
pc.set_processore("AMD Ryzen 5") 
# Modifica l'attributo privato tramite il setter
print(pc.get_processore())