
    
def fibonacci_fino_a_n(n):
    
    # Gestione casi particolari
    if n < 0:
        return []
    if n < 1:
        return [0]
        
    # Inizializza la sequenza con i primi due numeri
    sequenza = [0, 1]
    
    # Genera la sequenza fino a N
    while True:
        prossimo = sequenza[-1] + sequenza[-2]
        if prossimo > n:
            break
        sequenza.append(prossimo)
        
    return sequenza

def inserisci_numero(n): 
    int(input("Inserisci un numero N per generare la sequenza di Fibonacci fino a N: "))

def fibonacci():
    # Input dall'utente con gestione errori
    while True:
        
            inserisci_numero(n)
            if n < 0:
                print("Per favore inserisci un numero non negativo.")
                continue
            break
        
            print("Input non valido. Inserisci un numero intero.")
    
    # Genera e mostra la sequenza
    sequenza = fibonacci_fino_a_n(n)
    
    # Formatta l'output
    print("\nSequenza di Fibonacci fino a", n, ":")
    print(", ".join(map(str, sequenza)))
    print(f"\nLa sequenza contiene {len(sequenza)} numeri.")



if __name__ == "__fibonacci__":
    fibonacci()