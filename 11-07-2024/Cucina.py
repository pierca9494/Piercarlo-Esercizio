from abc import ABC, abstractmethod

class PersonaleCucina(ABC):
    def __init__(self, nome: str, eta: int, max_piatti: int):
        self.__nome = nome
        self.__eta = eta
        self.max_piatti = max_piatti
        self.feedback = []
    
    def get_nome(self):
        return self.__nome
    
    def get_eta(self):
        return self.__eta

    def aggiungi_feedback(self, feedback: str):
        self.feedback.append(feedback)
    
    @abstractmethod
    def lavora(self):
        pass
    
    @abstractmethod
    def stampa(self):
        pass

class Chef(PersonaleCucina):
    def __init__(self, nome: str, eta: int, specializzazione: str, max_piatti: int):
        super().__init__(nome, eta, max_piatti)
        self.__specializzazione = specializzazione
        self.piatto_associato = "Pizza"
        
    def prepara_menu(self):
        return f"Preparo il menu per il giorno con la specializzazione {self.__specializzazione}"
    
    def lavora(self):
        return f"{self.get_nome()} sta lavorando come Chef."

    def stampa(self):
        return f"Chef {self.get_nome()}, ({self.get_eta()} anni) specializzato in {self.__specializzazione}"

class SousChef(PersonaleCucina):
    def __init__(self, nome: str, eta: int, max_piatti: int):
        super().__init__(nome, eta, max_piatti)
        self.piatto_associato = "Pasta"
    
    
    
    def rifornisci_inventario(self, ristorante, ingrediente: str, quantita: int):
        """Rifornisce l'inventario del ristorante."""
        if ingrediente in ristorante.inventario:
            ristorante.inventario[ingrediente] += quantita
        else:
            ristorante.inventario[ingrediente] = quantita
        return f"{self.get_nome()} ha rifornito {ingrediente} con {quantita} unità. Disponibili ora: {ristorante.inventario[ingrediente]}"
    
    def lavora(self):
        return f"{self.get_nome()} sta lavorando come SousChef."

    def stampa(self):
        return f"Sous Chef {self.get_nome()}, ({self.get_eta()} anni)"

class CuocoLinea(PersonaleCucina):
    def __init__(self, nome: str, eta: int, max_piatti: int):
        super().__init__(nome, eta, max_piatti)
        self.piatto_associato = "Zuppa"
    
    def lavora(self):
        return f"{self.get_nome()} sta lavorando come Cuoco di Linea."

    def stampa(self):
        return f"Cuoco di Linea {self.get_nome()}, ({self.get_eta()} anni)"

class Cliente:
    def __init__(self, nome: str):
        self.nome = nome
        self.ordine = []
        self.feedback = []
        
    def aggiungi_ordinazione(self, piatto: str):
        self.ordine.append(piatto)
        return f"{self.nome} ha ordinato {piatto}."
    
    def lascia_feedback(self):
        """Lascia un feedback al cliente."""
        feedback = input()
        self.feedback.append(feedback)
        return f"{self.nome} ha lasciato feedback: '{feedback}'"
    def stampa_feedback(self):
        return f"Feedback del cliente {self.nome}: {', '.join(self.feedback)}"

class Ristorante:
    
    def __init__(self, budget_iniziale: float):
        self.menu = {"Pizza": ["pomodoro", "mozzarella", "farina"],
            "Pasta": ["pasta", "vongole"],
            "Zuppa": ["pesce", "pomodoro"]}
        self.ordinazioni = []
        self.personale = []
        self.budget = budget_iniziale
        self.cost_totale = 0
        self.inventario = {
            "pomodoro": 10,
            "mozzarella": 10,
            "farina": 10,
            "pasta": 10,
            "vongole": 10,
            "pesce": 10
        }
        self.ingredienti_piatti = {
            "Pizza": ["pomodoro", "mozzarella", "farina"],
            "Pasta": ["pasta", "vongole"],
            "Zuppa": ["pesce", "pomodoro"]
        }
        
    def aggiungi_piatto_menu(self, nome_piatto: str, ingredienti: list, costo: float):
        self.menu.append({"nome": nome_piatto, "ingredienti": ingredienti, "costo": costo})
        return f"Piatto '{nome_piatto}' aggiunto al menu con ingredienti: {ingredienti} e costo di preparazione: €{costo}"
    
    def mostra_menu(self):
        return [f"{piatto['nome']} (Costo: €{piatto['costo']}): {piatto['ingredienti']}" for piatto in self.menu]
    
    def aggiungi_personale(self, personale: PersonaleCucina):
        self.personale.append(personale)
        return f"Aggiunto {personale.get_nome()} al personale di cucina."
    
    def verifica_ingredienti(self, piatto):
        ingredienti_necessari = self.ingredienti_piatti.get(piatto, [])
        for ingrediente in ingredienti_necessari:
            if self.inventario.get(ingrediente, 0) < 1:
                return False, ingrediente
        return True
    
    def utilizza_ingredienti(self, piatto):
        
        for ingrediente in self.ingredienti_piatti.get(piatto, []):
            self.inventario[ingrediente] -= 1
    
    def servire_piatto(self, personale: PersonaleCucina, piatto: str):
        if piatto not in [p for p in self.menu]:
            return f"Piatto '{piatto}' non presente nel menu."
        
        if piatto != personale.piatto_associato:
            return f"{personale.get_nome()} non può preparare '{piatto}'. È autorizzato a preparare solo '{personale.piatto_associato}'."
        
        # Verifica disponibilità ingredienti
        disponibili, ingrediente_mancante = self.verifica_ingredienti(piatto)
        if not disponibili:
            return f"Impossibile preparare '{piatto}': manca {ingrediente_mancante}."
        
        # Utilizza ingredienti e serve il piatto
        self.utilizza_ingredienti(piatto)
        return f"{personale.get_nome()} ha preparato il piatto '{piatto}'. Ingredienti utilizzati: {self.ingredienti_piatti[piatto]}"
    
    def mostra_inventario(self):
        return f"Inventario attuale: {self.inventario}"
    
    def mostra_budget(self):
        return f"Budget attuale: €{self.budget}, costo totale degli ordini: €{self.cost_totale}"

# Esempio di utilizzo
ristorante = Ristorante(budget_iniziale=500)
cliente1= Cliente("Luigi")
cliente2= Cliente("Pippo")

# Creazione del personale
chef = Chef("Mario", 40, "Cucina Italiana", max_piatti=2)
sous_chef = SousChef("Luigi", 35, max_piatti=2)
cuoco_linea = CuocoLinea("Giovanni", 28, max_piatti=2)

# Aggiunta del personale al ristorante
ristorante.aggiungi_personale(chef)
ristorante.aggiungi_personale(sous_chef)
ristorante.aggiungi_personale(cuoco_linea)


print(cliente1.aggiungi_ordinazione("Pizza"))
print(ristorante.verifica_ingredienti("Pizza"))
print(ristorante.utilizza_ingredienti("Pizza"))
print(ristorante.servire_piatto(chef, "Pizza"))
print(cliente1.lascia_feedback())
print(cliente1.stampa_feedback())




# Rifornimento inventario da parte del Sous Chef
print(sous_chef.rifornisci_inventario(ristorante, "mozzarella", 5))
print(sous_chef.rifornisci_inventario(ristorante, "farina", 10))

# Mostra inventario aggiornato
print("Inventario aggiornato:")
print(ristorante.mostra_inventario())
