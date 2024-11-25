class Dispositivo:
    numero_dispositivi = 0  # Attributo di classe per contare i dispositivi

    def __init__(self, marca, modello, prezzo):
        self._marca = marca
        self._modello = modello
        self._prezzo = prezzo
        self._disponibile = True
        Dispositivo.numero_dispositivi += 1  # Incrementa il conteggio dei dispositivi

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modello(self):
        return self._modello

    @modello.setter
    def modello(self, modello):
        self._modello = modello

    @property
    def prezzo(self):
        return self._prezzo

    @prezzo.setter
    def prezzo(self, prezzo):
        self._prezzo = prezzo

    @property
    def disponibile(self):
        return self._disponibile

    def vendi(self):
        self._disponibile = False

    def rifornisci(self):
        self._disponibile = True

    @classmethod
    def conta_dispositivi(cls):
        return cls.numero_dispositivi

    @staticmethod
    def calcola_sconto(prezzo, percentuale):
        return prezzo * (1 - percentuale / 100)


class Smartphone(Dispositivo):
    def __init__(self, marca, modello, prezzo, memoria):
        super().__init__(marca, modello, prezzo)
        self._memoria = memoria

    @property
    def memoria(self):
        return self._memoria

    @memoria.setter
    def memoria(self, memoria):
        self._memoria = memoria

    def descrizione(self):
        return f"Smartphone {self.marca} {self.modello} con {self.memoria}GB di memoria"


class Laptop(Dispositivo):
    def __init__(self, marca, modello, prezzo, ram):
        super().__init__(marca, modello, prezzo)
        self._ram = ram

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, ram):
        self._ram = ram

    def descrizione(self):
        return f"Laptop {self.marca} {self.modello} con {self.ram}GB di RAM"


class Tablet(Dispositivo):
    def __init__(self, marca, modello, prezzo, schermo):
        super().__init__(marca, modello, prezzo)
        self._schermo = schermo

    @property
    def schermo(self):
        return self._schermo

    @schermo.setter
    def schermo(self, schermo):
        self._schermo = schermo

    def descrizione(self):
        return f"Tablet {self.marca} {self.modello} con schermo da {self.schermo} pollici"


class Inventario:
    def __init__(self):
        self._dispositivi = []

    def aggiungi_dispositivo(self, dispositivo):
        self._dispositivi.append(dispositivo)

    def cerca_per_prezzo(self, prezzo_max):
        return [d for d in self._dispositivi if d.prezzo < prezzo_max]

    def cerca_disponibili(self):
        return [d for d in self._dispositivi if d.disponibile]

    def stampa_inventario(self):
        for dispositivo in self._dispositivi:
            print(dispositivo.descrizione())


# Esempio di utilizzo
# Fase 1
smartphone = Smartphone("Apple", "iPhone 12", 999, 128)
print(smartphone.marca)  # Output: Apple
smartphone.vendi()
print(smartphone.disponibile)  # Output: False

# Fase 2
laptop = Laptop("Dell", "XPS 13", 1200, 16)
tablet = Tablet("Samsung", "Galaxy Tab S7", 650, 11)

print(smartphone.descrizione())  # Output: Smartphone Apple iPhone 12 con 128GB di memoria
print(laptop.descrizione())  # Output: Laptop Dell XPS 13 con 16GB di RAM
print(tablet.descrizione())  # Output: Tablet Samsung Galaxy Tab S7 con schermo da 11 pollici

# Fase 3
print(Dispositivo.conta_dispositivi())  # Output: 3
print(Dispositivo.calcola_sconto(1000, 10))  # Output: