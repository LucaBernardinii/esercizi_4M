class Insegnante:
    def __init__(self, nome, cognome, strumento_insegnato):
        self._nome = nome
        self._cognome = cognome
        self._strumento_insegnato = strumento_insegnato

        self.studenti = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cognome(self):
        return self._cognome

    @cognome.setter
    def cognome(self, cognome):
        self._cognome = cognome

    @property
    def strumento_insegnato(self):
        return self._strumento_insegnato

    @strumento_insegnato.setter
    def strumento_insegnato(self, strumento_insegnato):
        self._strumento_insegnato = strumento_insegnato

    def aggiungi_studente(self, studente):
        if studente not in self.studenti:    
            self.studenti.append(studente)
            studente.set_insegnante(self)

class Studente:
    def __init__(self, nome, cognome):
        self._nome = nome
        self._cognome = cognome

        self.corsi = []
        self.insegnanti = []
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cognome(self):
        return self._cognome

    @cognome.setter
    def cognome(self, cognome):
        self._cognome = cognome

    @property
    def corsi(self):
        return self._corsi

    @corsi.setter
    def corsi(self, corsi):
        self._corsi = corsi

    def iscrivi_corso(self, corso):
        if corso not in self.corsi:
            self.corsi.append(corso)
            corso.aggiungi_studente(self)
    
    def set_insegnante(self, insegnante):
        if insegnante not in self.insegnanti:
            self.insegnanti.append(insegnante)
            insegnante.aggiungi_studente(self)

class Corso:
    def __init__(self, nome, durata):
        self._nome = nome
        self._durata = durata

        self.studenti = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def durata(self):
        return self._durata

    @durata.setter
    def durata(self, durata):
        self._durata = durata

    def aggiungi_studente(self, studente):
        if studente not in self.studenti:    
            self.studenti.append(studente)
            studente.iscrivi_corso(self)

    
def main():
    # Creazione degli insegnanti
    insegnante1 = Insegnante("Mario", "Rossi", "Pianoforte")
    insegnante2 = Insegnante("Luca", "Bianchi", "Chitarra")

    # Creazione degli studenti
    studente1 = Studente("Anna", "Verdi")
    studente2 = Studente("Marco", "Neri")

    # Assegnazione degli insegnanti agli studenti
    studente1.set_insegnante(insegnante1)
    studente2.set_insegnante(insegnante2)

    # Creazione dei corsi
    corso1 = Corso("Teoria Musicale", "3 mesi")
    corso2 = Corso("Tecnica Pianistica", "6 mesi")

    # Iscrizione degli studenti ai corsi
    studente1.iscrivi_corso(corso1)
    studente1.iscrivi_corso(corso2)
    studente2.iscrivi_corso(corso1)

    # Stampa delle informazioni
    print(studente1)
    print(studente2)

if __name__ == "__main__":
    main()