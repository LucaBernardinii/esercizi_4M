class Persona:
    def __init__(self, nome, eta, citta):
        self.nome = nome
        self.eta = eta
        self.citta = citta
    
    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome}.")

    def descrizione(self):
        print(f"Ho {self.eta} anni e vivo a {self.citta}.")
    
persona = Persona("Ana", 169, "Bucarest")
persona.saluta()
persona.descrizione()