# Dati di accesso predefiniti
username_corretta = "admin"
password_corretta = "1234"
domanda_colore = "Qual è il tuo colore preferito? "
domanda_animale = "Qual è il tuo animale preferito? "

# Risposte di sicurezza
risposta_colore = "blu"
risposta_animale = "cane"

# Funzione per il login
def login():
    username_input = input("Inserisci il nome utente: ")
    password_input = input("Inserisci la password: ")
    if username_input == username_corretta and password_input == password_corretta:
        print("Accesso consentito.")
        return True
    else:
        print("Nome utente o password errati.")
        return False

# Funzione per cambiare la password
def cambia_password():
    scelta = input("Vuoi rispondere alla domanda su:\n1. Colore preferito\n2. Animale preferito\nScegli (1 o 2): ")

    if scelta == "1":
        risposta = input(domanda_colore)
        if risposta.lower() == risposta_colore:
            nuova_password = input("Risposta corretta! Inserisci la nuova password: ")
            global password_corretta
            password_corretta = nuova_password
            print("Password aggiornata con successo.")
        else:
            print("Risposta errata.")
    elif scelta == "2":
        risposta = input(domanda_animale)
        if risposta.lower() == risposta_animale:
            nuova_password = input("Risposta corretta! Inserisci la nuova password: ")
            global password_corretta
            password_corretta = nuova_password
            print("Password aggiornata con successo.")
        else:
            print("Risposta errata.")
    else:
        print("Scelta non valida.")

# Main
if login():
    scelta_azione = input("Vuoi cambiare la password? (sì o no): ")
    if scelta_azione.lower() == "sì":
        cambia_password()
    else:
        print("Operazione terminata.")
