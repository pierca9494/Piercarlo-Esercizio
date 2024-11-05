import Classifica
import Gioco

username = ""
password = ""
utenti = {}
nuovo_usr = ""
nuovo_psw = ""



def registrazione():
    nuovo_usr = input("Inserisci il nuovo username: ")
    
    nuovo_psw = input("Inserisci la nuova password: ")
    
    utenti[nuovo_usr] = nuovo_psw
    
    print("Registrazione completata.")
    



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
        
        print("2. Login")
        print("3. Esci")
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            registrazione()
            
        
        elif scelta == "2":
            username = login()
        
            print(f"\nBenvenuto, {username}! Cosa vuoi fare?")
            print("1. Gioca")
            print("2. Classifica")
            scelta = input("Scegli un'opzione: ")
            if scelta == "1":
                gioco1 = Gioco()
                gioco1.domande()
                lista1 = gioco1.return_lista()
                print(f"La lista delle domande è: {lista1}")
                
                
            elif scelta == "2":
                Classifica.classifica()
                pass
            else:
                break
                
            
            
                    
        
            
        elif scelta == "5":
            print("Uscita dal sistema.")
            break
        else:
            print("Scelta non valida. Riprova.")

main()
