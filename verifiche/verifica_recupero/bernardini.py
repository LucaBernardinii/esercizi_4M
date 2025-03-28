import datetime

class ElementoMenu:
    def __init__(self, codice, nome, prezzo, tempo_di_preparazione, allergeni, diponibile):
        self.codice = codice
        self.nome = nome
        self.prezzo = prezzo
        self.tempo_di_preparazione = tempo_di_preparazione
        self.allergeni = allergeni
        self.diponibile = diponibile

    def is_disponibile(self):
        return self.diponibile
    
    def set_disponibile(self, diponibile):
        self.diponibile = diponibile

    def to_string(self):
        return f"Codice: {self.codice}, Nome: {self.nome}, Prezzo: {self.prezzo}, Tempo di preparazione: {self.tempo_di_preparazione}, Allergeni: {self.allergeni}, Disponibile: {self.diponibile}"
    
class PrimoPiatto(ElementoMenu):
    def __init__(self, tipo_pasta, vegetariano, codice, nome, prezzo, tempo_di_preparazione, allergeni, diponibile):
        super().__init__(codice, nome, prezzo, tempo_di_preparazione, allergeni, diponibile)
        self.tipo_pasta = tipo_pasta
        self.vegetariano = vegetariano

    def is_vegetariano(self):
        return self.vegetariano

    def to_string(self):
        return f"Tipo di pasta: {self.tipo_pasta}, Vegetariano: {self.vegetariano}, {super().to_string()}"

class SecondoPiatto(ElementoMenu):
    def __init__(self, cottura, ordine, codice, nome, prezzo, tempo_di_preparazione, allergeni, diponibile):
        super().__init__(codice, nome, prezzo, tempo_di_preparazione, allergeni, diponibile)
        self.cottura = cottura
        self.ordine = ordine

    def to_string(self):
        return f"Cottura: {self.cottura}, Ordine: {self.ordine}, {super().to_string()}"
    
class Ordine:
    def __init__(self, numero_ordine, data_ora, stato, elementi):
        self.numero_ordine = numero_ordine
        self.data_ora = data_ora
        self.stato = stato
        self.elementi = elementi
        self.ordini_attivi = []

    def calcola_totale(self):
        totale = 0
        for elemento in self.elementi:
            totale += elemento.prezzo
        return totale
    
    def aggiungi_elemento(self, elemento):
        self.elementi.append(elemento)

    def rimuovi_elemento(self, elemento):
        self.elementi.remove(elemento)

    def to_string(self):
        return f"Numero ordine: {self.numero_ordine}, Data e ora: {self.data_ora}, Stato: {self.stato}, Elementi: {[elemento.to_string() for elemento in self.elementi]}"
    
class Tavolo:
    def __init__(self, numero, posti, stato):
        self.numero = numero
        self.posti = posti
        self.stato = stato
    
    def is_libero(self):
        return self.stato == "libero"
    
    def aggiungi_ordine(self, ordine):
        self.ordine = ordine
        self.stato = "occupato"

    def get_ordini_attivi(self):
        return self.ordine.ordini_attivi
    
    def to_string(self):
        return f"Numero tavolo: {self.numero}, Posti: {self.posti}, Stato: {self.stato}"
    
# Creazione elementi del menu
primo = PrimoPiatto("P1", "Spaghetti Carbonara", 12.0, 15, ["uova", "glutine"], True)
primo.set_tipo_pasta("spaghetti")
primo.set_vegetariano(False)

secondo = SecondoPiatto("S1", "Bistecca", 18.0, 20, [], True)
secondo.set_cottura_default("media")

# Creazione tavolo e ordine
tavolo = Tavolo(1, 4, "libero")
ordine = Ordine("ORD1", datetime.now(), "in_attesa", [])

# Aggiunta elementi all'ordine
ordine.aggiungi_elemento(primo)
ordine.aggiungi_elemento(secondo)

# Associazione ordine al tavolo
tavolo.aggiungi_ordine(ordine)
tavolo.set_stato("occupato")

# Calcoli
print(f"Totale ordine: {ordine.calcola_totale()}€")  # Output: Totale ordine: 30.0€

# Gestione stato ordine
ordine.set_stato("in_preparazione")
print(f"Stato ordine: {ordine.get_stato()}")  # Output: Stato ordine: in_preparazione

# Informazioni tavolo
print(f"Tavolo numero: {tavolo.get_numero()}")
print(f"Stato tavolo: {'libero' if tavolo.is_libero() else 'occupato'}")
print(f"Ordini attivi: {len(tavolo.get_ordini_attivi())}")