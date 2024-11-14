import mysql.connector
# try:

#     miodb= mysql.connector.connect(
#         host= "localhost",
#         user="root",
#         password= "root"
#         )
    
#     c=miodb.cursor()
#     try:
#      c.execute("CREATE DATABASE IF NOT EXISTS scuola_db")
#      print("Database 'scuola_db' creato con successo.")
#     except mysql.connector.Error as err:
#      print(f"Errore durante l'esecuzione di CREATE DATABASE: {err}")
#     except :
#      print("Errore non riconosciuto")  

# except mysql.connector.Error as conn_err:
#  print(f"Errore di connessione al server MySQL: {conn_err}")
# except :
#  print("Errore non riconosciuto")
# miodb.database= "scuola_db"
# c.execute("""create table if not exists studenti_
#           (id int AUTO_INCREMENT PRIMARY KEY,
#           name VARCHAR(255)""")

# c.execute("""
#     CREATE TABLE IF NOT EXISTS materie (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         nome VARCHAR(255)  UNIQUE NOT NULL 
#     )
# """)

# c.execute (""""
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     studente_id INT,
#     materia_id INT,
#     voto INT,
#     FOREIGN KEY (studente_id) REFERENCES studenti_(id),
#     FOREIGN KEY (materia_id) REFERENCES materie(id)
#     )
# """)





#class Studente:
#   def __init__(self,name,voto_Ita,voto_Mate):
#     self.name=name
#     self.voto_Ita=voto_Ita
#     self.voto_Mate=voto_Mate




class GestioneStudentiDB:
    def __init__(self,host= "localhost", user = "root", password= "root", database = "scuola_db"):
        self.miodb = mysql.connector.connect(
            host= host,
            user=user,
            password= password,
            database=database)
        
        self.cursor = self.miodb.cursor()
        
        
    
    self.cursor.execute("CREATE DATABASE IF NOT EXISTS scuola_db")
    print("Database 'scuola_db' creato con successo.") 


    self.cursor.execute("""create table if not exists studenti_
          (id int AUTO_INCREMENT PRIMARY KEY,
          name VARCHAR(255)""")

    self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS materie (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255)  UNIQUE NOT NULL 
    )
""")

    self.cursor.execute (""""
    id INT AUTO_INCREMENT PRIMARY KEY,
    studente_id INT,
    materia_id INT,
    voto INT,
    FOREIGN KEY (studente_id) REFERENCES studenti_(id),
    FOREIGN KEY (materia_id) REFERENCES materie(id)
    )
        """)

    def aggiungi_studente(self, nome):
        try:
            self.cursor.execute("INSERT INTO studenti (nome) VALUES (%s)", (nome,))
            self.miodb.commit()
            print(f"Studente '{nome}' aggiunto.")
        except mysql.connector.Error as err:
            print(f"Errore: {err}")

    def aggiungi_materia(self, materia):
        try:
            self.cursor.execute("INSERT IGNORE INTO materie (nome) VALUES (%s)", (materia,))
            self.miodb.commit()
            print(f"Materia '{materia}' aggiunta.")
        except mysql.connector.Error as err:
          print(f"Errore: {err}")

    def aggiungi_voto(self, nome, materia, voto):
        try:
            self.cursor.execute("SELECT id FROM studenti WHERE nome = %s", (nome,))
            studente = self.cursor.fetchone()
            self.cursor.execute("SELECT id FROM materie WHERE nome = %s", (materia,))
            materia_id = self.cursor.fetchone()

            if studente and materia_id:
                self.cursor.execute("INSERT INTO voti (studente_id, materia_id, voto) VALUES (%s, %s, %s)", 
                                    (studente[0], materia_id[0], voto))
                self.miodb.commit()
                print(f"Voto {voto} aggiunto in '{materia}' per '{nome}'.")
            else:
                print("Studente o materia non trovati.")
        except mysql.connector.Error as err:
            print(f"Errore: {err}")

    def elimina_studente(self, nome):
        try:
            self.cursor.execute("DELETE FROM studenti WHERE nome = %s", (nome,))
            self.miodb.commit()
            print(f"Studente '{nome}' eliminato.")
        except mysql.connector.Error as err:
            print(f"Errore: {err}")

    def modifica_voto(self, nome, materia, indice, nuovo_voto):
        try:
            self.cursor.execute("SELECT id FROM studenti WHERE nome = %s", (nome,))
            studente_id = self.cursor.fetchone()
            self.cursor.execute("SELECT id FROM materie WHERE nome = %s", (materia,))
            materia_id = self.cursor.fetchone()

            if studente_id and materia_id:
                self.cursor.execute(
                    "SELECT id FROM voti WHERE studente_id = %s AND materia_id = %s LIMIT %s, 1",
                    (studente_id[0], materia_id[0], indice)
                )
                voto_id = self.cursor.fetchone()
                
                if voto_id:
                    self.cursor.execute("UPDATE voti SET voto = %s WHERE id = %s", (nuovo_voto, voto_id[0]))
                    self.miodb.commit()
                    print(f"Voto modificato in '{materia}' per '{nome}' a {nuovo_voto}.")
                else:
                    print("Voto non trovato.")
            else:
                print("Studente o materia non trovati.")
        except mysql.connector.Error as err:
            print(f"Errore: {err}")

    def stampa_studenti(self):
        try:
            self.cursor.execute("SELECT id, nome FROM studenti")
            studenti = self.cursor.fetchall()

            for studente in studenti:
                print(f"\nStudente: {studente[1]}")
                self.cursor.execute("""
                    SELECT materie.nome, voti.voto
                    FROM voti
                    JOIN materie ON voti.materia_id = materie.id
                    WHERE voti.studente_id = %s
                """, (studente[0],))
                voti = self.cursor.fetchall()

                voti_per_materia = {}
                for materia, voto in voti:
                    if materia not in voti_per_materia:
                        voti_per_materia[materia] = []
                    voti_per_materia[materia].append(voto)

                media_totale = []
                for materia, voti_lista in voti_per_materia.items():
                    media_materia = sum(voti_lista) / len(voti_lista)
                    media_totale.extend(voti_lista)
                    print(f"  Materia: {materia} - Voti: {voti_lista} - Media: {media_materia:.2f}")
                
                media_generale = sum(media_totale) / len(media_totale) if media_totale else 0
                print(f"Media Generale: {media_generale:.2f}")
        except mysql.connector.Error as err:
            print(f"Errore: {err}")

    def chiudi_connessione(self):
        self.cursor.close()
        self.miodb.close()


# Funzione di menu per interazione
def menu():
    gestione = GestioneStudentiDB(
        host="localhost",
        user="tuo_utente",
        password="tua_password",
        database="gestione_studenti"
    )

    while True:
        print("\n--- Menu Gestionale Studenti ---")
        print("1. Aggiungi studente")
        print("2. Aggiungi materia")
        print("3. Aggiungi voto")
        print("4. Elimina studente")
        print("5. Modifica voto")
        print("6. Stampa studenti e medie")
        print("7. Esci")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            nome = input("Inserisci il nome dello studente: ")
            gestione.aggiungi_studente(nome)

        elif scelta == "2":
            materia = input("Inserisci il nome della materia: ")
            gestione.aggiungi_materia(materia)

        elif scelta == "3":
            nome = input("Inserisci il nome dello studente: ")
            materia = input("Inserisci la materia: ")
            voto = int(input("Inserisci il voto: "))
            gestione.aggiungi_voto(nome, materia, voto)

        elif scelta == "4":
            nome = input("Inserisci il nome dello studente da eliminare: ")
            gestione.elimina_studente(nome)

        elif scelta == "5":
            nome = input("Inserisci il nome dello studente: ")
            materia = input("Inserisci la materia: ")
            indice = int(input("Inserisci l'indice del voto da modificare (0 per il primo voto, 1 per il secondo, ecc.): "))
            nuovo_voto = int(input("Inserisci il nuovo voto: "))
            gestione.modifica_voto(nome, materia, indice, nuovo_voto)

        elif scelta == "6":
            gestione.stampa_studenti()

        elif scelta == "7":
            print("Uscita dal gestionale.")
            gestione.chiudi_connessione()
            break

        else:
            print("Opzione non valida, riprova.")

# Avvia il menu gestionale
menu()
