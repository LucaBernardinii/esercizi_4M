class Animale:
    def __init__(self, codiceIdentificativo, nome, eta, peso):
        self._codiceIdentificativo = codiceIdentificativo
        self._nome = nome
        self._eta = eta
        self._peso = peso
        self._visite = []

    @property
    def codiceIdentificativo(self):
        return self._codiceIdentificativo
    
    codiceIdentificativo.setter
    def codiceIdentificativo(self, value):
        self._codiceIdentificativo = value

    @property
    def nome(self):
        return self._nome
    
    nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def eta(self):
        return self._eta
    
    eta.setter
    def eta(self, value):
        self._eta = value

    @property
    def peso(self):
        return self._peso
    
    peso.setter
    def peso(self, value):
        self._peso = value

    def aggiungi_visita(self, visita):
        self._visite.append(visita)


class Mammifero(Animale):
    def __init__(self, codiceIdentificativo, nome, eta, peso, tipoPelliccia, temperaturaCorpo, periodoGestazione):
        super().__init__(codiceIdentificativo, nome, eta, peso)
        self._tipoPelliccia = tipoPelliccia
        self._temperaturaCorpo = temperaturaCorpo
        self._periodoGestazione = periodoGestazione

    @property
    def tipoPelliccia(self):
        return self._tipoPelliccia
    
    tipoPelliccia.setter
    def tipoPelliccia(self, value):
        self._tipoPelliccia = value

    @property
    def temperaturaCorpo(self):
        return self._temperaturaCorpo
    
    temperaturaCorpo.setter
    def temperaturaCorpo(self, value):
        self._temperaturaCorpo = value

    @property
    def periodoGestazione(self):
        return self._periodoGestazione
    
    periodoGestazione.setter
    def periodoGestazione(self, value):
        self._periodoGestazione = value

class Rettile(Animale):
    def __init__(self, codiceIdentificativo, nome, eta, peso, velenoso):
        super().__init__(codiceIdentificativo, nome, eta, peso)
        self._velenoso = velenoso

    @property
    def velenoso(self):
        return self._velenoso
    
    velenoso.setter
    def velenoso(self, value):
        self._velenoso = value

class Habitat:
    def __init__(self, codiceArea, nome, dimensione):
        self._codiceArea = codiceArea
        self._nome = nome
        self._dimensione = dimensione
        self._animali = []

    @property
    def codiceArea(self):
        return self._codiceArea
    
    codiceArea.setter
    def codiceArea(self, value):
        self._codiceArea = value

    @property
    def nome(self):
        return self._nome
    
    nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def dimensione(self):
        return self._dimensione
    
    dimensione.setter
    def dimensione(self, value):
        self._dimensione = value

    def aggiungi_animale(self, animale: Animale) -> None:
        self._animali.append(animale)

    def rimuovi_animale(self, animale: Animale) -> None:
        self._animali.remoove(animale)
    
    def get_animali(self) -> list[Animale]:
        return self._animali
    
    def get_eta_media(self, animale: Animale) -> float:
        return sum(animale.eta for animale in self._animali) / len(self._animali)


class Veterinario:
    def __init__(self, matricola, nome, cognome, specializzazione, anniEsperienza):
        self._matricola = matricola
        self._nome = nome
        self._cognome = cognome
        self._specializzazione = specializzazione
        self._anniEsperienza = anniEsperienza

    @property
    def matricola(self):
        return self._matricola
    
    matricola.setter
    def matricola(self, value):
        self._matricola = value

    @property
    def nome(self):
        return self._nome
    
    nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def cognome(self):
        return self._cognome
    
    cognome.setter
    def cognome(self, value):
        self._cognome = value

    @property
    def specializzazione(self):
        return self._specializzazione
    
    specializzazione.setter
    def specializzazione(self, value):
        self._specializzazione = value

    @property
    def anniEsperienza(self):
        return self._anniEsperienza
    
    anniEsperienza.setter
    def anniEsperienza(self, value):
        self._anniEsperienza = value

    def effettua_visita(self, animale: Animale, diagnosi: str, trattamento: str):
        pass
        #diagnosi = VisitaVeterinaria.diagnosi
        #trattamento = VisitaVeterinaria.trattamentoProposto

class VisitaVeterinaria:
    def __init__(self, data, diagnosi, trattamentoProposto):
        self._data = data
        self._diagnosi = diagnosi
        self._trattamentoProposto = trattamentoProposto

    @property
    def data(self):
        return self._data
    
    data.setter
    def data(self, value):
        self._data = value

    @property
    def diagnosi(self):
        return self._diagnosi
    
    diagnosi.setter
    def diagnosi(self, value):
        self._diagnosi = value

    @property
    def trattamentoProposto(self):
        return self._trattamentoProposto
    
    trattamentoProposto.setter
    def trattamentoProposto(self, value):
        self._trattamentoProposto = value

class SistemaGestioneZoo:
    def __init__(self):
        self._animali_presenti = [Animale]
        self._habitat = [Habitat]
        self._veterinari = [Veterinario]
        self._registro_visite_veterinarie = [VisitaVeterinaria]

    def aggiungi_animale(self, animale: Animale) -> None:
        self._animali_presenti.append(animale)

    def rimuovi_animale(self, animale: Animale) -> None:
        self._animali_presenti.remove(animale)

    def assegna_habitat(self, animale: Animale, habitat: Habitat) -> bool:
        if len(habitat._animali) == 0:
            habitat._animali.append(animale)
            return True
        elif len(habitat._animali) > 0:
            x = Mammifero(1,1,1,1,1,1,1)
            if type(habitat._animali[0]) == type(x):
                habitat._animali.append(animale)
                return True
            else:
                return False
            
    def registra_visita(self, visita : VisitaVeterinaria) -> None:
        self._registro_visite_veterinarie.append(visita)

    def get_animali_habitat(self, habitat: Habitat) -> list[Animale]:
        return habitat._animali
    
    def get_storico_visite(self, animale: Animale) -> list[VisitaVeterinaria]:
        return animale._visite
    
    def get_habitat_compatibili(self, animale : Animale) -> list[Habitat]:
        habitat_compatibili = []
        x = Mammifero()
        for habitat in self._habitat:
            pass
    
    def calcola_eta_media_per_habitat(self) -> dict[str, float]:
        pass
        #eta_media_per_habitat = {}
        #for habitat in self._habitat:
        #    eta_media_per_habitat.append(Habitat.get_eta_media())






def main():
    # Creazione del sistema
    zoo = SistemaGestioneZoo()

    # Creazione degli habitat
    savana = Habitat("H001", "Savana Africana", 1000.0)
    rettilario = Habitat("H002", "Rettilario", 500.0)
    zoo._habitat.extend([savana, rettilario])

    # Creazione dei veterinari
    vet1 = Veterinario("V001", "Mario", "Rossi", "Mammiferi", 10)
    vet2 = Veterinario("V002", "Laura", "Bianchi", "Rettili", 8)
    zoo._veterinari.extend([vet1, vet2])

    # Creazione degli animali
    leone = Mammifero("M001", "Simba", 5, 180.0, "Folta", 38.5, 110)
    serpente = Rettile("R001", "Kaa", 3, 5.0, True)
    giraffa = Mammifero("M002", "Melman", 7, 800.0, "Maculata", 38.0, 450)

    # Aggiunta degli animali al sistema
    for animale in [leone, serpente, giraffa]:
        zoo.aggiungi_animale(animale)

    # Assegnazione degli habitat
    zoo.assegna_habitat(leone, savana)
    zoo.assegna_habitat(giraffa, savana)
    success = zoo.assegna_habitat(serpente, savana)
    print("\nTentativo di mettere serpente in savana:", "Riuscito" if success else "Fallito")
    zoo.assegna_habitat(serpente, rettilario)

    # Effettuazione delle visite veterinarie
    visita1 = vet1.effettua_visita(leone, "Controllo di routine", "Somministrazione vaccino annuale")
    zoo.registra_visita(visita1)

    visita2 = vet2.effettua_visita(serpente, "Infezione batterica", "Antibiotico per 7 giorni")
    zoo.registra_visita(visita2)

    # Stampa delle informazioni
    print("\n=== Stato dello Zoo ===")

    print("\nAnimali nella Savana:")
    for animale in zoo.get_animali_habitat(savana):
        print(f"- {animale.nome} ({animale.codiceIdentificativo})")

    print("\nAnimali nel Rettilario:")
    for animale in zoo.get_animali_habitat(rettilario):
        print(f"- {animale.nome} ({animale.codiceIdentificativo})")

    #print("\nEtà media per habitat:")
    #for habitat, eta_media in zoo.calcola_eta_media_per_habitat().items():
    #    print(f"- {habitat}: {eta_media:.1f} anni")

    print("\nStorico visite di Simba:")
    for visita in zoo.get_storico_visite(leone):
        print(f"- Data: {visita.data}")
        print(f"  Veterinario: {visita.veterinario.nome} {visita.veterinario.cognome}")
        print(f"  Diagnosi: {visita.diagnosi}")
        print(f"  Trattamento: {visita.trattamentoProposto}")


if __name__ == "__main__":
    main()

# Tentativo di mettere serpente in savana: Fallito

# === Stato dello Zoo ===

# Animali nella Savana:
# - Simba (M001)
# - Melman (M002)

# Animali nel Rettilario:
# - Kaa (R001)

# Età media per habitat:
# - Savana Africana: 6.0 anni
# - Rettilario: 3.0 anni

# Storico visite di Simba:
# - Data: 2025-02-11 15:27:06.489484
#   Veterinario: Mario Rossi
#   Diagnosi: Controllo di routine
#   Trattamento: Somministrazione vaccino annuale