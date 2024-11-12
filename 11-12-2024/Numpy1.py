import numpy as np
from scipy import stats

# # Un array unidimensionale di numeri casuali compresi tra 0 e 1 (10 elementi)
# array_unidimensionale = np.random.rand(10)

# # Un array bidimensionale di dimensione 3x3 con valori interi casuali tra 0 e 10
# array_bidimensionale = np.random.randint(0, 11, (3, 3))

# array_unidimensionale, array_bidimensionale



# array1 = np.random.randint(0, 11, (4, 4))
# array2 = np.random.randint(0, 11, (4, 4))


# sum_last_row_array1 = np.sum(array1[-1, 1:])
# sum_last_row_array2 = np.sum(array2[-1, 1:])


# array_combined = np.concatenate((array1, array2), axis=1)
# array_combined2 = np.concatenate((array1, array2), axis=0)

# array1, array2, sum_last_row_array1, sum_last_row_array2, array_combined

# print(array1)
# print(array2)
# print("Somma ultima riga seconda colonna array1:", sum_last_row_array1)
# print("Somma ultima riga seconda colonna array2:", sum_last_row_array2)
# print("Array combinato:", array_combined)
# print("Array combinato lungo l'asse 0:", array_combined2)




array_1d = np.random.randint(1, 1001, 50)


media = np.mean(array_1d)
moda_risultato= stats.mode(array_1d, keepdims=True)  # `keepdims=True` ensures the result is array-like
moda_valore = moda_risultato.mode[0] if moda_risultato.mode.size > 0 else None
std_dev = np.std(array_1d)


array_reshaped = array_1d.reshape(5, 10)

print(array_1d)
print("Media:", media)
print("Moda:", moda_valore)
print("Deviazione standard:", std_dev)
print("Array trasformato in forma 5x10:", array_reshaped)

