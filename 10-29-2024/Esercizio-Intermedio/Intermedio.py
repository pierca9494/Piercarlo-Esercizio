def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

numero_utente1 = input(int())
numero_utente2 = input(int())

    



def main():
    prime_numbers = []
    not_prime = []
    numeri = [*range(numero_utente1, numero_utente2+1)]
    
    
    
    for num in numeri:
        if is_prime(num):
            prime_numbers.append(num)
            print("Numeri primi:", prime_numbers)
            
        else:
            not_prime.append(num)
            print("Numeri non primi:", not_prime)