class Veicolo:
    numero_veicoli = 0

    def __init__(self, tipo: str, marca: str) -> None:
        self.tipo = tipo
        self.marca = marca
        Veicolo.numero_veicoli +=1

    @classmethod
    def get_numero_veicoli(cls) -> int:
        return cls.numero_veicoli
    
print(Veicolo.numero_veicoli)
auto1 = Veicolo("Auto", "Toyota")
auto2 = Veicolo("Moto", "Honda")
print(Veicolo.numero_veicoli)
