class Ricetta:
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta):
        self.nome = nome
        self.tempo_preparazione = tempo_preparazione
        self.ingredienti = ingredienti
        self.difficolta = difficolta

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_tempo_preparazione(self):
        return self.tempo_preparazione

    def set_tempo_preparazione(self, tempo_preparazione):
        self.tempo_preparazione = tempo_preparazione

    def get_ingredienti(self):
        return self.ingredienti

    def set_ingredienti(self, ingredienti):
        self.ingredienti = ingredienti

    def get_difficolta(self):
        return self.difficolta

    def set_difficolta(self, difficolta):
        self.difficolta = difficolta

    def __str__(self):
        return f"{self.nome} - {self.tempo_preparazione} min - Difficoltà: {self.difficolta}"
    
class Primo:
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, tipo_pasta, sugo):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.tipo_pasta = tipo_pasta
        self.sugo = sugo

    def get_tipo_pasta(self):
        return self.tipo_pasta

    def set_tipo_pasta(self, tipo_pasta):
        self.tipo_pasta = tipo_pasta

    def get_sugo(self):
        return self.sugo

    def set_sugo(self, sugo):
        self.sugo = sugo

class Secondo:
    def __init__(self, nome, tempo_preparazione, ingredienti, difficolta, tipo_carne, cottura):
        super().__init__(nome, tempo_preparazione, ingredienti, difficolta)
        self.tipo_pasta = tipo_carne
        self.sugo = cottura

    def get_tipo_carne(self):
        return self.tipo_carne

    def set_tipo_carne(self, tipo_carne):
        self.tipo_carne = tipo_carne

    def get_cottura(self):
        return self.cottura

    def set_cottura(self, cottura):
        self.cottura = cottura



primo = Primo("Spaghetti alla Carbonara", 20, ["Spaghetti", "Uova", "Pancetta"], "Media", "Spaghetti", "Carbonara")
secondo = Secondo("Bistecca alla Fiorentina", 30, ["Bistecca", "Sale", "Pepe"], "Alta", "Manzo", "Media")
dolce = Dolce("Tiramisù", 30, ["Mascarpone", "Caffè", "Savoiardi"], "Media", 200, "Dessert")

ricette = [primo, secondo, dolce]
ricette_possibili = verifica_ingredienti(ricette, ["Spaghetti", "Uova", "Pancetta", "Bistecca", "Sale", "Pepe", "Mascarpone", "Caffè", "Savoiardi", "Pane", "Pomodoro", "Basilico"])
print(f"Ricette che possono essere preparate: {len(ricette_possibili)}")

print("\nInformazioni sulle ricette:")
stampa_ricette(ricette)
