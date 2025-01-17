class Automobile:
    def __init__(self, numero_targa, modello, categoria, disponibilita):
        self._numero_targa = numero_targa
        self._modello = modello
        self._categoria = categoria
        self._disponibilita = disponibilita

    @property
    def numero_targa(self):
        return self._numero_targa
    
    @property
    def modello(self):
        return self._modello
    
    @property
    def categoria(self):
        return self._categoria

    @property
    def disponibilita(self):
        return self._disponibilita


class AgenziaNoleggio:
    def __init__(self):
        self._automobili = []

    @property
    def automobili(self):
        return self._automobili
    
    def aggiungi_automobile(self, automobile):
        self._automobili.append(automobile)

    def noleggio(self, automobile):
        for automobile in self._automobili:
            if automobile.numero_targa == automobile:
                automobile._disponibilita = False
                return True
        return False
    
    def visualizza_disponibili(self):
        disponibili = []
        for automobile in self._automobili:
            if automobile.disponibilita:
                disponibili.append(automobile)
        return disponibili
    
    def visualizza_noleggi(self):
        noleggi = []
        for automobile in self._automobili:
            if not automobile.disponibilita:
                noleggi.append(automobile)
        return noleggi