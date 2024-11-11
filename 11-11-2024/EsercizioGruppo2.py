# Nome del file di database
database_file = "database_scolastico.txt"



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
        


write_text_db(diz)

# Menu principale
#funzione principale
def main():
    alunni = GestioneScolastica(database_file)
    
    while True:
        print("1. Aggiungi alunno")
        print("2. Elimina alunno")
        print("3. Visualizza alunni")
        print("4. Esci")
        
        scelta = input("Scegli un'opzione(1/2/3/4): ")
        
        if scelta == "1":
            studente3.nome = input("Nome alunno: ")
            voti = list(map(int, input("Voti: ").split(",")))
            aggiungi_alunno(studente.nome, voti, alunni)
            salva_alunni(alunni)
        
        elif scelta =="2":
            studente.nome = input("Nome alunno da eliminare: ")
            alunni = elimina_alunno(studente.nome, alunni)
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
