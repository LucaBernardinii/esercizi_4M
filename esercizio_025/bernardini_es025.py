from datetime import datetime

class Prenotazione:
    def __init__(self, nome, data, numero, stato):
        self._nome = nome
        self._data = datetime
        self._numero = numero
        self._stato = stato

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def stato(self):
        return self._stato

    @stato.setter
    def stato(self, stato):
        self._stato = stato


class Ristorante:
    def __init__(self):
        self._prenotazioni = []
    
    def aggiungi_prenotazione(self, prenotazione):
        self._prenotazioni.append(prenotazione)

    def cerca_preotazione(self, nome):
        for prenotazione in self._prenotazioni:
            if prenotazione.nome == nome:
                return prenotazione
        return None
    
    def visualizza_prenotazioni(self):
        for prenotazione in self._prenotazioni:
            print(f"{prenotazione.nome} {prenotazione.data} {prenotazione.numero} {prenotazione.stato}")

    def cancella_prenotazione(self, nome):
        for prenotazione in self._prenotazioni:
            if prenotazione.nome == nome:
                self._prenotazioni.remove(prenotazione)
                return True
        return False
    

ristorante = Ristorante()
prenotazione1 = Prenotazione("Mario Rossi", datetime(2021, 10, 10), 4, "Confermata")
prenotazione2 = Prenotazione("Luca Bianchi", datetime(2021, 10, 11), 3, "Confermata")
ristorante.aggiungi_prenotazione(prenotazione1)
ristorante.aggiungi_prenotazione(prenotazione2)
ristorante.visualizza_prenotazioni()
print(ristorante.cerca_preotazione("Mario Rossi"))
print(ristorante.cancella_prenotazione("Mario Rossi"))
ristorante.visualizza_prenotazioni()
