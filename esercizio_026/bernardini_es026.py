class Veicolo:
    def __init__(self, marca, modello, tipo_carburante):
        self._marca = marca
        self._modello = modello
        self._tipo_carburante = tipo_carburante

    @property
    def marca(self):
        return self._marca
    
    marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def modello(self):
        return self._modello
    
    modello.setter
    def modello(self, value):
        self._modello = value

    @property
    def tipo_carburante(self):
        return self._tipo_carburante
    
    tipo_carburante.setter
    def tipo_carburante(self, value):
        self._tipo_carburante = value


class Auto(Veicolo):
    def __init__(self, marca, modello, tipo_carburante):
        super().__init__(marca, modello, tipo_carburante)


class Camion(Veicolo):
    def __init__(self, marca, modello, tipo_carburante):
        super().__init__(marca, modello, tipo_carburante)

class Flotta:
    def __init__(self):
        self._veicoli = []

    def aggiungi_veicolo(self, veicolo):
        self._veicoli.append(veicolo)

    def visualizza_info_veicoli(self):
        for veicolo in self._veicoli:
            print(f"Marca: {veicolo.marca}, Modello: {veicolo.modello}, Tipo carburante: {veicolo.tipo_carburante}")

auto1 = Auto("Fiat", "Panda", "Benzina")
auto2 = Auto("Ford", "Focus", "Diesel")
camion1 = Camion("Iveco", "Eurocargo", "Diesel")
camion2 = Camion("Mercedes", "Actros", "Diesel")

flotta = Flotta()

flotta.aggiungi_veicolo(auto1)
flotta.aggiungi_veicolo(auto2)
flotta.aggiungi_veicolo(camion1)
flotta.aggiungi_veicolo(camion2)

flotta.visualizza_info_veicoli()
