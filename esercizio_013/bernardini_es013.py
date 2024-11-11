class Casa:
    def __init__(self, indirizzo, proprietario):
        self.indirizzo = indirizzo
        self.proprietario = proprietario
        self.stanze = []

    def get_indirizzo(self):
        return self.indirizzo
    
    def set_indirizzo(self, indirizzo):
        self.indirizzo = indirizzo

    def get_proprietario(self):
        return self.proprietario
    
    def set_proprietario(self, proprietario):
        self.proprietario = proprietario

    def stampa_stanze(self):
        for stanza in self.stanze:
            print(f'{stanza.nome} ({stanza.superficie} mq)')
        

    def aggiungi_stanza(self,stanza):      
        self.stanze.append(stanza)
        stanza.associa_casa(self)


class Stanza:
    def __init__(self, nome, superficie):
        self.nome = nome
        self.superficie = superficie
        self.casa = None


    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    def get_superficie(self):
        return self.superficie
    
    def set_superficie(self, superficie):
        self.superficie = superficie

    def associa_casa(self,casa):
        self.casa = casa

    


casa = Casa("Via delle Rose 15", "Maria Rossi")

soggiorno = Stanza("Soggiorno", 30)
cucina = Stanza("Cucina", 15)
camera = Stanza("Camera da Letto", 20)

casa.aggiungi_stanza(soggiorno)
casa.aggiungi_stanza(cucina)
casa.aggiungi_stanza(camera)

print(f"Casa di {casa.proprietario} situata in {casa.indirizzo} contiene le seguenti stanze:")
for stanza in casa.stanze:
    print(f"- {stanza.nome} ({stanza.superficie} mq)")