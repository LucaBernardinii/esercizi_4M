class Volo:
    def __init__(self, numero_volo, destinazione, data_ora_partenza, numero_massimo_passeggeri):
        self._numero_volo = numero_volo
        self._destinazione = destinazione
        self._data_ora_partenza = data_ora_partenza
        self._numero_massimo_passeggeri = numero_massimo_passeggeri

    @property
    def numero_volo(self):
        return self._numero_volo
    
    numero_volo.setter
    def numero_volo(self, value):
        self._numero_volo = value

    @property
    def destinazione(self):
        return self._destinazione
    
    destinazione.setter
    def destinazione(self, value):
        self._destinazione = value

    @property
    def data_ora_partenza(self):
        return self._data_ora_partenza
    
    data_ora_partenza.setter
    def data_ora_partenza(self, value):
        self._data_ora_partenza = value
    
    @property
    def numero_massimo_passeggeri(self):
        return self._numero_massimo_passeggeri
    
    numero_massimo_passeggeri.setter
    def numero_massimo_passeggeri(self, value):
        self._numero_massimo_passeggeri = value


class Prenotazione:
    def __init__(self, nome_passeggero, tipo_classe, volo):
        self._nome_passeggero = nome_passeggero
        self._tipo_classe = tipo_classe
        self._volo = volo

    @property
    def nome_passeggero(self):
        return self._nome_passeggero
    
    nome_passeggero.setter
    def nome_passeggero(self, value):
        self._nome_passeggero = value

    @property
    def tipo_classe(self):
        return self._tipo_classe
    
    tipo_classe.setter
    def tipo_classe(self, value):
        self._tipo_classe = value

    @property
    def volo(self):
        return self._volo
    
    volo.setter
    def volo(self, value):
        self._volo = value


class SistemaPrenotazione:
    def __init__(self):
        self._lista_voli = []
        self._lista_prenotazioni = []

    def aggiungi_volo(self, volo):
        self._lista_voli.append(volo)

    def aggiungi_prenotazione(self, prenotazione):
        self._lista_prenotazioni.append(prenotazione)

    def visualizza_info_voli(self):
        for volo in self._lista_voli:
            print(f"Numero volo: {volo.numero_volo}")
            print(f"Destinazione: {volo.destinazione}")
            print(f"Data e ora partenza: {volo.data_ora_partenza}")
            print(f"Numero massimo passeggeri: {volo.numero_massimo_passeggeri}")
            print()

    def visualizza_info_prenotazioni(self):
        for prenotazione in self._lista_prenotazioni:
            print(f"Nome passeggero: {prenotazione.nome_passeggero}")
            print(f"Tipo classe: {prenotazione.tipo_classe}")
            print(f"Volo: {prenotazione.volo.numero_volo}")
            print()


volo = Volo("AZ123", "Roma", "2021-12-31 12:00", 200)
prenotazione = Prenotazione("Mario Rossi", "Business", volo)
sistema = SistemaPrenotazione()
sistema.aggiungi_volo(volo)
sistema.aggiungi_prenotazione(prenotazione)
sistema.visualizza_info_voli()
sistema.visualizza_info_prenotazioni()
