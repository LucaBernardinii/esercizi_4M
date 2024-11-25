import math

class VeicoloSpaziale:
    numero_veicoli = 0

    def __init__(self, nome, velocita_massima, massa, posizione):
        self._nome = nome
        self._velocita_massima = velocita_massima
        self._massa = massa
        self._posizione = posizione
        VeicoloSpaziale.numero_veicoli += 1

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome
    
    def get_velocita_massima(self):
        return self._velocita_massima

    def set_velocita_massima(self, velocita_massima):
        self._velocita_massima = velocita_massima

    def get_massa(self):
        return self._massa

    def set_massa(self, massa):
        self._massa = massa

    def get_posizione(self):
        return self._posizione

    def set_posizione(self, posizione):
        self._posizione = posizione
    
    @staticmethod
    def veicoli_totali(cls):
        return cls.numero_veicoli
    
    def calcola_tempo_comunicazione(altro_veicolo):
        math.sqrt
    

class Sonda:
    def __init__(self, nome, velocita_massima, massa, posizione, tipo_missione, energia, consumo_energia):
        super().__init__(nome, velocita_massima, massa, posizione)
        self._tipo_missione = tipo_missione
        self._energia = energia
        self._consumo_energia = consumo_energia

    def get_tipo_missione(self):
        return self._tipo_missione

    def set_tipo_missione(self, tipo_missione):
        self._tipo_missione = tipo_missione

    def get_energia(self):
        return self._energia

    def set_energia(self, energia):
        self._energia = energia

    def get_consumo_energia(self):
        return self._consumo_energia

    def set_consumo_energia(self, consumo_energia):
        self._consumo_energia = consumo_energia

    def simula_missione(durata):
        consumo = consumo_energia * durata
        if consumo <= energia:
            energia - consumo
            return True
        else:
            return False
        

class Astronave:
    def __init__(self, nome, velocita_massima, massa, posizione, numero_equipaggio, carburante, consumo_carburante):
        super().__init__(nome, velocita_massima, massa, posizione)
        self._numero_equipaggio = numero_equipaggio
        self._carburante = carburante
        self._consumo_carburante = consumo_carburante

    def get_numero_equipaggio(self):
        return self._numero_equipaggio

    def set_numero_equipaggio(self, numero_equipaggio):
        self._numero_equipaggio = numero_equipaggio

    def get_carburante(self):
        return self._carburante

    def set_carburante(self, carburante):
        self._carburante = carburante

    def get_consumo_carburante(self):
        return self._consumo_carburante

    def set_consumo_carburante(self, consumo_carburante):
        self._consumo_carburante = consumo_carburante

    def puo_raggiungere(distanza):
        carburante_necessario = distanza * consumo_carburante
        if carburante_necessario <= carburante:
            return True
        else:
            return False
        

class StazioneOrbitante:
    def __init__(self, nome, velocita_massima, massa, posizione, moduli, capacita_aggancio, _veicoli_agganciati):
        super().__init__(nome, velocita_massima, massa, posizione)
        self._moduli = moduli
        self._capacita_aggancio = capacita_aggancio
        self._veicoli_agganciati = veicoli_agganciati

    def get_moduli(self):
        return self._moduli

    def set_moduli(self, moduli):
        self._moduli = moduli

    def get_capacita_aggancio(self):
        return self._capacita_aggancio

    def set_capacita_aggancio(self, capacita_aggancio):
        self._capacita_aggancio = capacita_aggancio

    def get_veicoli_agganciati(self):
        return self._veicoli_agganciati

    def set_veicoli_agganciati(self, veicoli_agganciati):
        self._veicoli_agganciati = veicoli_agganciati

    def aggancia_veicolo(veicolo):
        if capacita_aggancio > 0:
            veicolo.append(veicoli_agganciati)
            capacita_aggancio -= 1
            return True
        else:
            return False
    
    def sgancia_veicolo(veicolo):
        if veicolo in veicoli_agganciati:
            veicolo.remove(veicoli_agganciati)
            capacita_aggancio += 1
            return True
        else:
            return False
        
    def elenca_veicoli_agganciati():
        return veicoli_agganciati
            
            




sonda1 = Sonda(
    nome="Explorer I",
    velocita_massima=15,  # km/s
    massa=800,            # kg
    posizione=(1000, 2000, 3000),  # km
    tipo_missione="Ricerca",
    energia=5000,         # MJ
    consumo_energia=50    # MJ/h
)

astronave1 = Astronave(
    nome="Odyssey",
    velocita_massima=12,  # km/s
    massa=200000,         # kg
    posizione=(11500, 12500, 13500),  # km
    numero_equipaggio=100,
    carburante=600,       # tonnellate
    consumo_carburante=0.06  # tonnellate/km
)

stazione1 = StazioneOrbitante(
    nome="Alpha Station",
    velocita_massima=0,   # Stazionaria
    massa=500000,         # kg
    posizione=(0, 0, 0),  # km
    moduli=["Habitat", "Laboratorio", "Comunicazioni"],
    capacita_aggancio=2,
    veicoli_agganciati = []
)

# Informazioni sui veicoli
print(sonda1)
print(astronave1)
print(stazione1)
# Sonda: Explorer I - Velocità Massima: 15 km/s - Massa: 800 kg - Missione: Ricerca - Energia: 5000 MJ
# Astronave: Odyssey - Velocità Massima: 12 km/s - Massa: 200000 kg - Equipaggio: 100 - Carburante: 600 t
# Stazione Orbitante: Alpha Station - Moduli: ['Habitat', 'Laboratorio', 'Comunicazioni'] - Capacità di Aggancio: 5 - Veicoli Agganciati: 0

# Simulazione di una missione con la sonda
durata_missione = 80  # ore
if sonda1.simula_missione(durata_missione):
    print("Missione completata con successo.")
else:
    print("Energia insufficiente per completare la missione.")
print(f"Energia residua della sonda: {sonda1.energia()} MJ")
# Missione completata con successo.
# Energia residua della sonda: 1000 MJ

# Verifica se l'astronave può raggiungere una destinazione a 8000 km
distanza_destinazione = 8000  # km
if astronave1.puo_raggiungere(distanza_destinazione):
    print("L'astronave può raggiungere la destinazione.")
else:
    print("Carburante insufficiente per raggiungere la destinazione.")
# L'astronave può raggiungere la destinazione.


# Calcolo del tempo di comunicazione tra la sonda e l'astronave
tempo_comunicazione = sonda1.calcola_tempo_comunicazione(astronave1)
print(f"Tempo di comunicazione tra sonda e astronave: {tempo_comunicazione:.2f} s")
# Tempo di comunicazione tra sonda e astronave: 0.06 s


# Aggancio dell'astronave alla stazione
if stazione1.aggancia_veicolo(astronave1):
    print("Astronave agganciata con successo alla stazione.")
else:
    print("Capacità massima di aggancio raggiunta.")
# Astronave agganciata con successo alla stazione.


# Elenco dei veicoli agganciati
veicoli_agganciati = stazione1.elenca_veicoli_agganciati()
print(f"Veicoli agganciati alla stazione: {veicoli_agganciati}")
# Veicoli agganciati alla stazione: ['Odyssey']

# Calcolo del peso totale dei veicoli
veicoli = [sonda1, astronave1, stazione1]
peso_totale = calcola_peso_totale(veicoli)
print(f"Peso totale dei veicoli: {peso_totale} kg")
# Peso totale dei veicoli: 700800 kg

# Numero totale di veicoli creati
print(f"Numero totale di veicoli spaziali: {VeicoloSpaziale.veicoli_totali()}")
# Numero totale di veicoli spaziali: 3