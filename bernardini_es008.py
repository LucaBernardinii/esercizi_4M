class Piatto:
    def __init__(self, nome, prezzo, disponibile):
        self.nome = nome
        self.prezzo = prezzo
        self.disponibile = disponibile

    def __str__(self):
        return f"{self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'}"

    def ordina(self):
        self.disponibile = False

    def disponi(self):
        self.disponibile = True

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_prezzo(self):
        return self.prezzo

    def set_prezzo(self, prezzo):
        self.prezzo = prezzo

    def get_disponibile(self):
        return self.disponibile

    def set_disponibile(self, disponibile):
        self.disponibile = disponibile

class Antipasto(Piatto):
    def __init__(self, nome, prezzo, disponibile, ingredienti, porzione):
        super().__init__(nome, prezzo, disponibile)
        self.ingredienti = ingredienti
        self.porzione = porzione

    def __str__(self):
        return f"Antipasto: {self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'} - Ingredienti: {', '.join(self.ingredienti)} - Porzione: {self.porzione}"

    def get_ingredienti(self):
        return self.ingredienti

    def set_ingredienti(self, ingredienti):
        self.ingredienti = ingredienti

    def get_porzione(self):
        return self.porzione

    def set_porzione(self, porzione):
        self.porzione = porzione

class Primo(Piatto):
    def __init__(self, nome, prezzo, disponibile, tipo_pasta, sugo):
        super().__init__(nome, prezzo, disponibile)
        self.tipo_pasta = tipo_pasta
        self.sugo = sugo

    def __str__(self):
        return f"Primo: {self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'} - Tipo Pasta: {self.tipo_pasta} - Sugo: {self.sugo}"

    def get_tipo_pasta(self):
        return self.tipo_pasta

    def set_tipo_pasta(self, tipo_pasta):
        self.tipo_pasta = tipo_pasta

    def get_sugo(self):
        return self.sugo

    def set_sugo(self, sugo):
        self.sugo = sugo

class Secondo(Piatto):
    def __init__(self, nome, prezzo, disponibile, tipo_carne, cottura):
        super().__init__(nome, prezzo, disponibile)
        self.tipo_carne = tipo_carne
        self.cottura = cottura

    def __str__(self):
        return f"Secondo: {self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'} - Tipo Carne: {self.tipo_carne} - Cottura: {self.cottura}"

    def get_tipo_carne(self):
        return self.tipo_carne

    def set_tipo_carne(self, tipo_carne):
        self.tipo_carne = tipo_carne

    def get_cottura(self):
        return self.cottura

    def set_cottura(self, cottura):
        self.cottura = cottura

class Dolce(Piatto):
    def __init__(self, nome, prezzo, disponibile, tipo_dolce, calorie):
        super().__init__(nome, prezzo, disponibile)
        self.tipo_dolce = tipo_dolce
        self.calorie = calorie

    def __str__(self):
        return f"Dolce: {self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'} - Tipo Dolce: {self.tipo_dolce} - Calorie: {self.calorie}"

    def get_tipo_dolce(self):
        return self.tipo_dolce

    def set_tipo_dolce(self, tipo_dolce):
        self.tipo_dolce = tipo_dolce

    def get_calorie(self):
        return self.calorie

    def set_calorie(self, calorie):
        self.calorie = calorie

def calcola_conto(piatti_ordinati):
    return sum(piatto.prezzo for piatto in piatti_ordinati)