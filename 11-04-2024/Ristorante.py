class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = {}
        
    def set_apertura(self):
        self.aperto = True
    
    
    def set_chiusura(self):
        self.aperto = False
        
        
    def descrivi_ristorante(self):
        print(f"Nome: {self.nome}")
        print(f"Tipo di cucina: {self.tipo_cucina}")
        print(f"Aperto: {self.aperto}")
        print("Menu:")
        for piatto, prezzo in self.menu.items():
            print(f"{piatto}: {prezzo}")
        
        
    def aprire_ristorante(self):
        if not self.aperto:
            self.set_apertura()
            print(f"Il ristorante {self.nome} è ora aperto.")
        else:
            print(f"Il ristorante {self.nome} è già aperto.")

    def chiudi_ristorante(self):
        if self.aperto:
            self.set_chiusura()
            print(f"Il ristorante {self.nome} è ora chiuso.")
        else:
            print(f"Il ristorante {self.nome} è già chiuso.")
            
            
    def aggiungi_al_menu(self, piatto, prezzo):
        self.menu[piatto] = prezzo
        print(f"Il piatto '{piatto}' è stato aggiunto al menu di {self.nome}.")

    def rimuovi_dal_menu(self, piatto):
        if piatto in self.menu:
            self.menu.remove(piatto)
            print(f"Il piatto '{piatto}' è stato rimosso dal menu di {self.nome}.")
        else:
            print(f"Il piatto '{piatto}' non è presente nel menu di {self.nome}.")

    def stampa_menu(self):
        print(f"Menu di {self.nome}:")
        if not self.menu:
            print("Il menu è vuoto.")
        else:
            for piatto in self.menu:
                print(f"- {piatto} : {self.menu[piatto]}$")
                
                

# Test
ristorante = Ristorante("Tom", "Internazionale")
ristorante.aggiungi_al_menu("Pizza", 12)
ristorante.aggiungi_al_menu("Pasta" , 13)
ristorante.aggiungi_al_menu("Carne", 24.4)
ristorante.stampa_menu()
ristorante.aprire_ristorante()