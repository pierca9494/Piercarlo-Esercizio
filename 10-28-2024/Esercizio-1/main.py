# Dati
admin_usr = "admin"
admin_psw = "password"
username = ""
password = ""
utenti = {"admin": "password"}  
lista_articoli = ["pane", "latte", "uova"]
lista_acquisti = []


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


def gestione_acquisti():
    scelta = input("Vuoi aggiungere o rimuovere un articolo dalla lista acquisti? (aggiungi/rimuovi/visualizza): ")
    if scelta == "aggiungi":
        articolo = input("Inserisci il nome dell'articolo da aggiungere: ")
        if articolo  in lista_articoli:
            lista_acquisti.append(articolo)
            print(f"{articolo} aggiunto alla lista acquisti.")
        else:
            print("Articolo non disponibile.")
    elif scelta == "rimuovi":
        articolo = input("Inserisci il nome dell'articolo da rimuovere: ")
        if articolo in lista_acquisti:
            lista_acquisti.remove(articolo)
            print(f"{articolo} rimosso dalla lista acquisti.")
        else:
            print("Articolo non presente nella lista acquisti.")
    elif scelta == "visualizza":
        print("Lista acquisti:", lista_acquisti)
    else:
        print("Scelta non valida.")


def gestione_articoli():
    scelta = input("Vuoi aggiungere o rimuovere un articolo dalla lista articoli? (aggiungi/rimuovi/visualizza): ")
    if scelta == "aggiungi":
        articolo = input("Inserisci il nome dell'articolo da aggiungere: ")
        lista_articoli.append(articolo)
        print(f"{articolo} aggiunto alla lista articoli.")
    elif scelta == "rimuovi":
        articolo = input("Inserisci il nome dell'articolo da rimuovere: ")
        if articolo in lista_articoli:
            lista_articoli.remove(articolo)
            print(f"{articolo} rimosso dalla lista articoli.")
        else:
            print("Articolo non presente nella lista articoli.")
    elif scelta == "visualizza":
        print("Lista articoli disponibili:", lista_articoli)
    else:
        print("Scelta non valida.")

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
            if username:
                if username == admin_usr:
                    # Opzioni per admin
                    print("\nBenvenuto, Admin! Cosa vuoi fare?")
                    gestione_articoli()
                else:
                    # Opzioni per utenti
                    print(f"\nBenvenuto, {username}! Cosa vuoi fare?")
                    gestione_acquisti()
        elif scelta == "3":
            print("Uscita dal sistema.")
            break
        else:
            print("Scelta non valida. Riprova.")

main()
