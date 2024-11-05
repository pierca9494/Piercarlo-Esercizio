scelta = input("Vuoi inserire un numero o una stringa? \n1.numero \n2.stringa\nScegli (1 o 2):   ")

if scelta == "1":
   
        risposta = int(input("Inserisci un numero: "))
        if risposta % 2 == 0:
            print("Il numero inserito è pari.")
        else:
            print("Il numero inserito è dispari.")
    
        print("Errore: Non hai inserito un numero valido.")
        
elif scelta == "2":
    risposta = input("Inserisci una stringa: ")
    print("Hai inserito la stringa:", risposta)
else:
    print("Scelta non valida.")
