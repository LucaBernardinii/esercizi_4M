class Insegnante:
    def __init__(self, nome, cognome, strumento_insegnato):
        self.nome = nome
        self.cognome = cognome
        self.strumento_insegnato = strumento_insegnato

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cognome(self):
        return self.cognome

    @cognome.setter
    def cognome(self, cognome):
        self.cognome = cognome

    @property
    def strumento_insegnato(self):
        return self.strumento_insegnato

    @strumento_insegnato.setter
    def strumento_insegnato(self, strumento_insegnato):
        self.strumento_insegnato = strumento_insegnato









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