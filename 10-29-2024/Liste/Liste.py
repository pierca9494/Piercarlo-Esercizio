numeri = [1,2,3,4,5]
nomi = ["Alice", "Bob", "Charlie"]
misto = [1, "due", True, 4.5]

print(numeri[0])




lista = [1, 2, 3]
lista.extend([4, 5])
# lista diventa [1, 2, 3, 4, 5]

lista = [1, 2, 3]
elemento = lista.pop(1)
# lista diventa [1, 3] e elemento è 2

lista = [1, 2, 3, 2]
indice = lista.index(2)
# indice è 1


lista = [1, 2, 2, 3]
conteggio = lista.count(2)
# conteggio è 2

lista = [1, 2, 3]
lista.reverse()
# lista diventa [3, 2, 1]


lista = [1, 2, 3]
lista.clear()
# lista diventa []

lista = [1, 2, 3]
copia_lista = lista.copy()
# copia_lista è [1, 2, 3] e non è la stessa lista originale
