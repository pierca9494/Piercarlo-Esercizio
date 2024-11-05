def is_prime(n):
    
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Input con controllo numero positivo
while True:
    
    n = int(input("Inserisci un numero intero positivo: "))
    if n > 0:
        break
    else:
        print("Il numero deve essere positivo. Riprova.")
            
#Stampa numeri pari
print("\nNumeri pari da 1 a", n)
for i in range(2, n + 1, 2):
    print(i, end=" ")
print()  # Per andare a capo dopo i numeri pari


# Calcolo somma numeri pari
somma_pari = 0
for i in range(2, n + 1, 2):
    somma_pari += i
print(f"\nLa somma dei numeri pari da 1 a {n} è: {somma_pari}")

# Stampa numeri dispari
print(f"\nNumeri dispari da 1 a {n}:")
for i in range(1, n + 1, 2):
    print(i, end=" ")
print()  # Per andare a capo dopo i numeri dispari

#Calcolo somma numeri dispari
somma_dispari = 0
for i in range(1, n + 1, 2):
    somma_dispari += i
print(f"\nLa somma dei numeri dispari da 1 a {n} è: {somma_dispari}")


# Verifica se n è primo
if is_prime(n):
    print(f"\nIl numero {n} è primo")
else:
    print(f"\nIl numero {n} non è primo")