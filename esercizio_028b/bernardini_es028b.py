class ParcoNaturale:
    def __init__(self, nome):
        self._nome = nome
        self.ecosistemi = []
        self.dispositivi = []
        self.sensori = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def monitora_parametri(self, tipo, temperatura, umidita, qualita_aria):
        ecosistema = Ecosistema(tipo, temperatura, umidita, qualita_aria)
        self.ecosistemi.append(ecosistema)

    def gestione_dispositivi(self, tipo, stato):
        if tipo.lower() == "sensore":
            sensore = Sensore(tipo, stato)
            self.sensori.append(sensore)
        else:
            dispositivo = Dispositivo(tipo, stato)
            self.dispositivi.append(dispositivo)

    def regola_ecosistema(self, dispositivo):
        for ecosistema in self.ecosistemi:
            if ecosistema._temperatura > 30:
                dispositivo._tipo = "Ventilatore"
                dispositivo._stato = True
            if ecosistema._umidita < 60:
                dispositivo._tipo = "Irrigatore"
                dispositivo._stato = True
            if ecosistema._qualita_aria < 40:
                dispositivo._tipo = "Ventilatore"
                dispositivo._stato = True

class Ecosistema:
    def __init__(self, tipo, temperatura, umidita, qualita_aria):
        self._tipo = tipo
        self._temperatura = temperatura
        self._umidita = umidita
        self._qualita_aria = qualita_aria
        self._dispositivi = []
        self._sensori = []

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, temperatura):
        self._temperatura = temperatura

    @property
    def umidita(self):
        return self._umidita

    @umidita.setter
    def umidita(self, umidita):
        self._umidita = umidita

    @property
    def qualita_aria(self):
        return self._qualita_aria

    @qualita_aria.setter
    def qualita_aria(self, qualita_aria):
        self._qualita_aria = qualita_aria

    
class Dispositivo:
    def __init__(self, tipo, stato):
        self._tipo = tipo
        self._stato = stato

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def stato(self):
        return self._stato

    @stato.setter
    def stato(self, stato):
        self._stato = stato

    def attiva(self):
        self._stato = True

    def disattiva(self):
        self._stato = False


class Sensore:
    def __init__(self, tipo, valore):
        self._tipo = tipo
        self._valore = valore

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def valore(self):
        return self._valore

    @valore.setter
    def valore(self, valore):
        self._valore = valore

parco = ParcoNaturale("Parco Naturale")
parco.monitora_parametri("Foresta", 25, 50, 40)
parco.gestione_dispositivi("Irrigatore", False)
parco.gestione_dispositivi("Purificatore", True)
parco.gestione_dispositivi("Ventilatore", False)
parco.regola_ecosistema(parco.dispositivi[0])
parco.regola_ecosistema(parco.dispositivi[1])
parco.regola_ecosistema(parco.dispositivi[2])