# Nome del file di database
database_file = "database_scolastico.txt"

class Studente:
    def __init__(self, nome, voti):
        self.nome = nome
        self.voti = voti

    def __str__(self):
        return f"{self.nome} - Voti: {self.voti}"

    def to_string(self):
        return f"{self.nome}:{','.join(map(str, self.voti))}"

class GestioneScolastica:
    def __init__(self, database_file):
        self.database_file = database_file

    def aggiungi_studente(self, studente):
        with open(self.database_file, "a") as file:
            file.write(studente.to_string() + "\n")
        print(f"Studente {studente.nome} aggiunto con voti {studente.voti}")

    def elimina_studente(self, nome):
        with open(self.database_file, "r") as file:
            lines = file.readlines()
        
        
        with open(self.database_file, "w") as file:
            trovato = False
            for line in lines:
                if not line.startswith(nome + ":"):
                    file.write(line)
                else:
                    trovato = True
                    

        if trovato:
            print(f"Studente {nome} eliminato.")
        else:
            print(f"Studente {nome} non trovato nel database.")

    def visualizza_studenti(self):
        try:
            with open(self.database_file, "r") as file:
                lines = file.readlines()
                if not lines:
                    print("Il database è vuoto.")
                else:
                    print("Lista degli studenti e dei voti:")
                    for line in lines:
                        nome, voti = line.strip().split(":")
                        voti = list(map(int, voti.split(",")))
                        studente = Studente(nome, voti)
                        print(studente)
        except FileNotFoundError:
            print("Il database non esiste ancora.")
            
            
    def read_text_db(filepath):
        # file = open(filepath, "r", encoding = "utf-8")
        # stringa = file.read()
        # file.close()
        with open(self.database_file, "r") as file:
            stringa = file.read()
        righe = stringa.splitlines()

        dizionario = {}
        for indice in range(0, int(len(righe) - 1 / 2), 2):
            newdict = {righe[indice].replace("/n", "") : righe[indice + 1].replace("/n", "")}
            dizionario.update(newdict)
        return dizionario


        diz = read_text_db("text_db.txt")
        print(diz)


    def write_text_db(dizionario):
        file = open("text_db2.txt", "w", encoding = "utf-8")
        for key in dizionario.keys():
        stringa1 = key + "/n"
        stringa2 = dizionario.get(key) + "/n"
        file.write(stringa1)
        file.write(stringa2)
    file.close()
            
    
            
    def alunni_media(database_file):
        for key in database_file:
            stringa = "lo studente : " + key
            lista_voti = database_file.get(key).split(",")
            media = 0
            for voto in lista_voti:
                media += int(voto)/len(lista_voti)
            stringa += " ha una media voti pari a: " + str(media)
            print(stringa)

alunni_media(diz)

# Menu principale
#funzione principale
def main():
    alunni = GestioneScolastica(database_file)
    
    while True:
        print("1. Aggiungi alunno")
        print("2. Elimina alunno")
        print("3. Visualizza alunni")
        print("4. media voti di un alunno")
        print("5. Esci")
        
        scelta = input("Scegli un'opzione(1/2/3/4): ")
        
        if scelta == "1":
            nome = input("Nome alunno: ")
            voti = list(map(int, input("Voti: ").split(",")))
            aggiungi_alunno(nome, voti, alunni)
            salva_alunni(alunni)
        
        elif scelta =="2":
            nome = input("Nome alunno da eliminare: ")
            alunni = elimina_alunno(nome, alunni)
            salva_alunni(alunni)
        
        elif scelta =="3":
            visualizza_alunni(alunni)
        
        elif scelta =="4":
            print("Arrivederci!")
            break
        
        else:
            print("Scelta non valida")

#esegue il programma
if __name__ == "__main__":
    main()
