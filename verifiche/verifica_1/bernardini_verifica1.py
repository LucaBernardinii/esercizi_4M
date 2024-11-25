class Dispositivo:
    def __init__(self, marca: str, modello: str, prezzo: float, disponibile: True):
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo
        self.disponibile = disponibile
        self.numero_dispositivi = numero_dispositivi

    def descrizione(self):
        return f"{self.marca} {self.modello}"

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_modello(self):
        return self.modello

    def set_modello(self, modello):
        self.modello = modello

    def get_prezzo(self):
        return self.prezzo

    def set_prezzo(self, prezzo):
        self.prezzo = prezzo

    def get_disponibile(self):
        return self.disponibile

    def set_disponibile(self, disponibile):
        self.disponibile = disponibile

    def vendi(self, disponibile):
        self.disponibile = False
        return self.disponibile
    
    def rifornisci(self, disponibile):
        self.disponibile = True
        return self.disponibile

    def conta_dispositivi():
        return numero_dispositivi
    
    @staticmethod
    def calcola_sconto(self, prezzo, sconto):
        self.prezzo = 

class Smartphone(Dispositivo):
    def __init__(self, marca: str, modello: str, prezzo: float, disponibile: True, memoria: int):
        super.__init__(marca, modello, prezzo, disponibile)
        self.memoria = memoria

    def descrizione(self):
        return f"Smartphone {self.marca} {self.modello} con {self.memoria}GB"

    def get_memoria(self):
        return self.memoria

    def set_memoria(self, memoria):
        self.memoria = memoria

class Laptop(Dispositivo):
    def __init__(self, marca: str, modello: str, prezzo: float, disponibile: True, ram: int):
        super.__init__(marca, modello, prezzo, disponibile)
        self.ram = ram

    def descrizione(self):
        return f"Laptop {self.marca} {self.modello} con {self.ram}GB di RAM"

    def get_ram(self):
        return self.ram
    
    def set_ram(self, ram):
        self.ram = ram

class Tablet(Dispositivo):
    def __init__(self, marca: str, modello: str, prezzo: float, disponibile: True, schermo: int):
        super.__init__(marca, modello, prezzo, disponibile)
        self.schermo = schermo

    def descrizione(self):
        return f"Tablet {self.marca} {self.modello} con schermo da {self.schermo} pollici"

    def get_schermo(self):
        return self.schermo
        
    def set_schermo(self, schermo):
        self.schermo = schermo


smartphone = Smartphone("Apple", "iPhone 12", 999, 128)
print(smartphone.get_marca())  
smartphone.vendi()
print(smartphone.disponibile)  


laptop = Laptop("Dell", "XPS 13", 1200, 16)
tablet = Tablet("Samsung", "Galaxy Tab S7", 650, 11)

print(smartphone.descrizione())  
print(laptop.descrizione())  
print(tablet.descrizione())  

print(Dispositivo.conta_dispositivi())
print(Dispositivo.calcola_sconto(1000, 10))


inventario = Inventario()
inventario.aggiungi_dispositivo(smartphone)
inventario.aggiungi_dispositivo(laptop)
inventario.aggiungi_dispositivo(tablet)

inventario.stampa_inventario()

dispositivi_economici = inventario.cerca_per_prezzo(1000)
print("Dispositivi con prezzo inferiore a 1000€:")
for dispositivo in dispositivi_economici:
    print(dispositivo.descrizione())

dispositivi_disponibili = inventario.cerca_disponibili()
print("Dispositivi disponibili:")
for dispositivo in dispositivi_disponibili:
    print(dispositivo.descrizione())
