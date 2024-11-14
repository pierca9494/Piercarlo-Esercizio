import mysql.connector
import hashlib

class GestioneStudentiDB:
    def __init__(self):
        self.miodb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="scuola_db"
        )
        
        self.cursor = self.miodb.cursor()
        
        # Creazione database e tabelle
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS scuola_db")
        print("Database 'scuola_db' creato con successo.") 

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS studenti (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS materie (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) UNIQUE NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS voti (
            id INT AUTO_INCREMENT PRIMARY KEY,
            studente_id INT,
            materia_id INT,
            voto INT,
            FOREIGN KEY (studente_id) REFERENCES studenti(id),
            FOREIGN KEY (materia_id) REFERENCES materie(id)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS utenti(
            id INT auto_increment primary key,
            username VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            ruolo enum("admin","studente") ) """  )
            
       

    def aggiungi_studente(self, nome):
        try:
            self.cursor.execute("INSERT INTO studenti (name) VALUES (%s)", (nome,))
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
            self.cursor.execute("SELECT id FROM studenti WHERE name = %s", (nome,))
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
            self.cursor.execute("DELETE FROM studenti WHERE name = %s", (nome,))
            self.miodb.commit()
            print(f"Studente '{nome}' eliminato.")
        except mysql.connector.Error as err:
            print(f"Errore: {err}")

    def modifica_voto(self, nome, materia, indice, nuovo_voto):
        try:
            self.cursor.execute("SELECT id FROM studenti WHERE name = %s", (nome,))
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
            self.cursor.execute("SELECT id, name FROM studenti")
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

    def dati_personali(self,id_studente):
        self.cursor.execute("SELECT voto from voti where studente_id= %s",(id_studente))
        voti= [voto[0] for voto in self.cursor.fetchall()]
        media=sum(voti)/len(voti) if voti else 0
        return voti,media

    def chiudi_connessione(self):
        self.cursor.close()
        self.miodb.close()

    def crea_utente(self,username,psw,ruolo):
        password = hashlib.md5(psw.encode()).hexdigest()  
        self.cursor.execute("INSERT INTO utenti (username,password,ruolo) VALUES( %s,%s,%s)",(username,password,ruolo))
        self.miodb.commit()

    def login(self,username,psw,ruolo):
        password = hashlib.md5(psw.encode()).hexdigest()  
        self.cursor.execute("SELECT * FROM utenti WHERE username = %s and password = %s  and ruolo = %s ",(username,password,ruolo))
        user= self.cursor.fetchone()
        return user


# Funzione di menu per interazione
def menu():
    gestione = GestioneStudentiDB()
    c=gestione.miodb.cursor()
    c.execute("SELECT * from utenti where ruolo = 'admin' ")  
    if c.fetchone()  is None :
        print("Nessun admin trovato")
        admin_user=input("Inserisci admin ")
        admin_psw=input("Inserisci password ")
        gestione.crea_utente(admin_user,admin_psw,"admin")
     
    while True:

        print("\n--- Menu Gestionale Studenti ---")

        username=input("Inserisci utente : ")
        password=input("Inserisci password ")
        ruolo=input("Inserisci ruolo admin o studente ")
        user=gestione.login(username,password,ruolo)
        if user:
            if ruolo== "admin":
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
                    password=  input("Inserisci password ")
                    ruolo=input("Inserisci ruolo admin/studente")
                    gestione.crea_utente(nome,password,ruolo)
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
            elif ruolo == "studente":
                print("1. -Stampa tutti gli studenti ")
                print("2. -Stampa solo il tuo voto e tua media")
                scelta2= input("Seleziona un'opzione: ")
                if scelta2== "1":

                    print("6. Stampa studenti e medie")
                    gestione.stampa_studenti()
                elif scelta2== "2":
                    pass

            else:
                print("Ruolo non valido")

        else:
            print("Opzione non valida, riprova.")
           


# Avvia il menu gestionale
menu()