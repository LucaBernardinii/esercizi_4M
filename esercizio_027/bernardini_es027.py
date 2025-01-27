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