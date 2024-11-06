class Posto:
    def __init__(self, numero: int, fila: str):
        self._numero = numero
        self._fila = fila
        self._occupato = False

    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto {self._fila}{self._numero} prenotato con successo.")
        else:
            print(f"Posto {self._fila}{self._numero} è già occupato.") 

    def libera(self):
        if self._occupato:
            self._occupato = False
            print(f"Posto {self._fila}{self._numero} liberato.")
        else:
            print(f"Posto {self._fila}{self._numero} è già libero.")

    @property
    def numero(self):
        return self._numero

    @property
    def fila(self):
        return self._fila

    @property
    def occupato(self):
        return self._occupato


class PostoVIP(Posto):
    def __init__(self, numero: int, fila: str, servizi_extra: str):
        super().__init__(numero, fila)
        self.servizi_extra = servizi_extra

    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto VIP {self._fila}{self._numero} prenotato con successo. Servizi extra: {self.servizi_extra}")
        else:
            print(f"Posto VIP {self._fila}{self._numero} è già occupato.")


class PostoStandard(Posto):
    def __init__(self, numero: int, fila: str, costo_online: float):
        super().__init__(numero, fila)
        self.costo_online = costo_online

    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto Standard {self._fila}{self._numero} prenotato con successo. Costo online: {self.costo_online}")
        else:
            print(f"Posto Standard {self._fila}{self._numero} è già occupato.")


class Teatro:
    def __init__(self):
        self._posti = []
        self.__postiVip = []

    def aggiungi_posto(self, posto: Posto):
        if isinstance(posto, PostoVIP):
            self.__postiVip.append(posto)
        else:
            self._posti.append(posto)

    def prenota_posto(self, numero: int, fila: str):
        for posto in self._posti:
            if posto.numero == numero and posto.fila == fila:
                posto.prenota()
                return
        print(f"Posto {fila}{numero} non trovato.")
        
    def prenota_vip(self, numero:int, fila:str, servizi_extra:str):
        for posto in self.__postiVip:
            if posto.numero == numero and posto.fila == fila and posto.servizi_extra == servizi_extra:
                posto.prenota()
                return
        print(f"Posto VIP {fila}{numero} non trovato.")

    def stampa_posti_occupati(self):
        posti_occupati = [f"{posto.fila}{posto.numero}" for posto in self._posti if posto.occupato]
        if posti_occupati:
            print("Posti occupati:", ", ".join(posti_occupati))
        else:
            print("Nessun posto occupato.")
            
    def stampa_posti_vip(self):
        posti_vip = [f"{posto.fila}{posto.numero}" for posto in self.__postiVip if posto.occupato]
        if posti_vip:
            print("Posti VIP occupati:", ", ".join(posti_vip))
        else:
            print("Nessun posto VIP occupato.")


# Esempio di utilizzo:
teatro = Teatro()
teatro.aggiungi_posto(PostoVIP(1, 'A', 'Accesso al lounge'))
teatro.aggiungi_posto(PostoStandard(2, 'B', 5.0))
teatro.aggiungi_posto(Posto(3, 'C'))

teatro.prenota_vip(1, 'A', 'Accesso al lounge' )
teatro.prenota_posto(2, 'B')
teatro.stampa_posti_occupati()
teatro.stampa_posti_vip()
