def is_palindroma(testo):
    
    testo_form = "".join(char.lower() for char in testo if char.isalnum())
    
    return testo_form == testo_form[::-1]

while True:
    testo = input("Inserisci una frase o digita 'esci' per terminare: ")
    
    if testo.lower() == 'esci':
        print("Programma terminato.")
        break

    elif is_palindroma(testo):
        print(f"'{testo}' è palindroma")
    else:
        print(f"'{testo}' non è palindroma")

    