
import numpy as np

# # Creazione di un array
# arr = np.array([1, 2, 3, 4, 5])

# # Utilizzo di alcuni metodi
# print("Forma dell'array:", arr.shape)  # Output: (5,)
# print("Dimensioni dell'array:", arr.ndim)  # Output: 1
# print("Tipo di dati:", arr.dtype)  # Output: int64 (varia a seconda della piattaforma)
# print("Numero di elementi:", arr.size)  # Output: 5
# print("Somma degli elementi:", arr.sum())  # Output: 15
# print("Media degli elementi:", arr.mean())  # Output: 3.0
# print("Valore massimo:", arr.max())  # Output: 5
# print("Indice del valore massimo:", arr.argmax())  # Output: 4

arr = np.arange(6)
reshaped_arr = arr.reshape((1,6))
print(reshaped_arr)
# Output:  [[0 1 2] [3 4 5]]