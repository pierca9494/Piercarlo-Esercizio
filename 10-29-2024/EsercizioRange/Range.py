# controllo dei numeri primi

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# funzione per il conteggio all'indietro in cui si prende un numero e si itera un contenggio all'indietro 

def countdown(number):
    while number >= 0:
        print(number)
        number -= 1
        
        
# insieme programmino
def main():
    prime_numbers = []
    while len(prime_numbers) < 5:
        
            num = int(input("Inserisci un numero: "))
            countdown(num)

            if is_prime(num):
                prime_numbers.append(num)
                print("Il numero è primo.")
            else:
                print("Il numero non è primo.")
                
            
            repeat = input("Vuoi ripetere? (s/n): ").lower()
            if repeat != 's':
                break
            
            
            
    
    print("Hai trovato 5 numeri primi:", prime_numbers)
    


