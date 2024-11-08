import numpy as np

class SlicingArray:
    def __init__(self, array):
        self.array = np.random.randint(10, 50, 20)
    
    def primi_10_elementi(self):
        self.array[:10]
        return self.array[:10] 
    
    def ultimi_5_elementi(self):
        self.array[-5:]
        return self.array[-5:]  
    
    def elementi_5_15(self):
        self.array[5:15]
        return self.array[5:15]  
    
    def ogni_terzo_elemento(self):
        # Creiamo una lista con tutti gli array
        array_principale = self.array
        array_primi_10 = self.primi_10_elementi()
        array_ultimi_5 = self.ultimi_5_elementi()
        array_5_15 = self.elementi_5_15()
        
    
        risultato = []
        for arr in [array_principale, array_primi_10, array_ultimi_5, array_5_15]:
            if len(arr) > 2:  
                risultato.append(arr[2])
                
        return np.array(risultato)
    
    def modifica_elementi(self):
        self.array[5:10] = 99
        return self.array

# Test della classe

slicing_array = SlicingArray(np.random.randint(10, 50, 20))
    
print("Array originale:", slicing_array.array)
print("Primi 10 elementi:", slicing_array.primi_10_elementi())
print("Ultimi 5 elementi:", slicing_array.ultimi_5_elementi())
print("Elementi 5-15:", slicing_array.elementi_5_15())

print("Terzo elemento di ogni array:", slicing_array.ogni_terzo_elemento())
print("Modifica elementi 5-10:", slicing_array.modifica_elementi())


