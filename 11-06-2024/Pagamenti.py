from abc import ABC, abstractmethod

# Classe base MetodoPagamento
class MetodoPagamento(ABC):
    @abstractmethod
    def effettua_pagamento(self, importo):
        pass

# Classe derivata per pagamento tramite carta di credito
class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con carta di credito.")

# Classe derivata per pagamento tramite PayPal
class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con PayPal.")

# Classe derivata per pagamento tramite bonifico bancario
class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con bonifico bancario.")

# Classe GestorePagamenti che utilizza un'istanza di MetodoPagamento
class GestorePagamenti:
    def __init__(self, metodo_pagamento: MetodoPagamento):
        self.metodo_pagamento = metodo_pagamento

    def paga(self, importo):
        self.metodo_pagamento.effettua_pagamento(importo)

# Esempio di utilizzo

carta = CartaDiCredito()
paypal = PayPal()
bonifico = BonificoBancario()

    # Uso di GestorePagamenti con diversi metodi di pagamento
gestore_carta = GestorePagamenti(carta)
gestore_paypal = GestorePagamenti(paypal)
gestore_bonifico = GestorePagamenti(bonifico)

    # Esempi di pagamento
gestore_carta.paga(100)
gestore_paypal.paga(50)
gestore_bonifico.paga(200)
