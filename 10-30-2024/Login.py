import Fibonacci



# Dati

username = ""
password = ""
utenti = {}
admin = {}
nuovo_admin = ""
nuova_psw_admin = ""
nuovo_usr = ""
nuovo_psw = ""



def registrazione():
    nuovo_usr = input("Inserisci il nuovo username: ")
    
    nuovo_psw = input("Inserisci la nuova password: ")
    
    utenti[nuovo_usr] = nuovo_psw
    
    print("Registrazione completata.")
    
def registrazione_admin():
  
    nuovo_admin = input("Inserisci il nuovo Admin:")
    nuova_psw_admin = input("Inserisci la nuova password:")
    admin[nuovo_admin] = nuova_psw_admin


def login():
    username = input("Inserisci il nome utente: ")
    password = input("Inserisci la password: ")
    if username in utenti and utenti[username] == password:
        print("Accesso consentito.")
        return username
    else:
        print("Nome utente o password errati.")
        return None







def main():
    while True:
        print("\nBenvenuto! Seleziona un'opzione:")
        print("1. Registrazione")
        print("2. Registrazione Admin")
        print("3. Login")
        print("4. Login Admin")
        print("5. Esci")
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            registrazione()
            
        elif scelta == "2":
            registrazione_admin()
        elif scelta == "3":
            username = login()
        
            print(f"\nBenvenuto, {username}! Cosa vuoi fare?")
            gioco()
            classica()
            
            
                    
        elif scelta == "4":
            if username == utenti[nuovo_admin]: 
                    # Opzioni per admin
                    print("\nBenvenuto, Admin! Cosa vuoi fare?")
            
                    
        elif scelta == "5":
            print("Uscita dal sistema.")
            break
        else:
            print("Scelta non valida. Riprova.")

main()
