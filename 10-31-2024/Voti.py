voti = {}

def registrazione():
    alunno = input("Inserisci il nuovo alunno: ")
    
    voto1 = float(input("Inserisci il primo voto: "))
    voto2 = float(input("Inserisci il secondo voto: "))
    voto3 = float(input("Inserisci il terzo voto: "))
    
    voti[alunno] = [voto1, voto2, voto3]
    
    print("Nuovo alunno inserito.")
    return voti

def calcola_media():
    print("\nMedia dei voti per ogni alunno:")
    for nome, voti_alunno in voti.items():
        media = sum(voti_alunno) / len(voti_alunno)
        print(f"Nome: {nome}, Media: {media:.2f}")

def main():
    while True:
        print("\nBenvenuto! Seleziona un'opzione:")
        print("1. Registrazione")
        print("2. Media")
        print("3. Esci")
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "1":
            registrazione()
        elif scelta == "2":
            calcola_media()
        elif scelta == "3":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida.")

main()






