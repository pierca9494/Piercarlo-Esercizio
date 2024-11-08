import numpy as np

class NumpyOperations:
    def __init__(self, array):
        self.array = np.arange(10, 50)
        
    def verifica_tipo_dato(self):
        return self.array.dtype
    def cambio_tipo_dato(self, new_dtype):
        self.array = self.array.astype(new_dtype)
        return self.array
    
    def forma_dato(self):
        return self.array.shape
    
    
# Create an instance of the NumpyOperations class
numpy_operations = NumpyOperations(np.arange(10, 50))

# Test the methods
print("Tipo di dato original:", numpy_operations.verifica_tipo_dato())  # Output: int64

print("Cambio tipo di dato a float64:")
print(numpy_operations.cambio_tipo_dato(np.float64))

print("Nuova forma del dato:", numpy_operations.verifica_tipo_dato())  # Output: float64
print("Forma del dato:", numpy_operations.forma_dato())  # Output: (40,)


