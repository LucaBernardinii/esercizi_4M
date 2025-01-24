class Film:
    def __init__(self, titolo, regista, anno_uscita, genere, valutazione):
        self._titolo = titolo
        self._regista = regista
        self._anno_uscita = anno_uscita
        self._genere = genere
        self._valutazione = valutazione

    @property
    def titolo(self):
        return self._titolo
    
    titolo.setter
    def titolo(self, titolo):
        self._titolo = titolo

    @property
    def regista(self):
        return self._regista
    
    regista.setter
    def regista(self, regista):
        self._regista = regista

    @property
    def anno_uscita(self):
        return self._anno_uscita
    
    anno_uscita.setter
    def anno_uscita(self, anno_uscita):
        self._anno_uscita = anno_uscita

    @property
    def genere(self):
        return self._genere
    
    genere.setter
    def genere(self, genere):
        self._genere = genere

    @property
    def valutazione(self):
        return self._valutazione
    
    valutazione.setter
    def valutazione(self, valutazione):
        self._valutazione = valutazione


class Libreria:
    def __init__(self):
        self._lista_film = []

    def aggiungi_film(self, film):
        self._lista_film.append(film)

    def cerca_film(self, titolo):
        for film in self._lista_film:
            if film.titolo == titolo:
                return film
        
    def visualizza_film(self):
        for film in self._lista_film:
            print(film.titolo, film.regista, film.anno_uscita, film.genere, film.valutazione)

    def valutazione_film(self, titolo, valutazione):
        film = self.cerca_film(titolo)
        print(film.titolo, film.valutazione)


film = Film("Titanic", "James Cameron", 1997, "Drammatico", 8)
film2 = Film("Il Padrino", "Francis Ford Coppola", 1972, "Drammatico", 9)
film3 = Film("Il Signore degli Anelli", "Peter Jackson", 2001, "Fantasy", 10)

libreria = Libreria()
libreria.aggiungi_film(film)
libreria.aggiungi_film(film2)
libreria.aggiungi_film(film3)

libreria.visualizza_film()
libreria.valutazione_film("Titanic", 9)
libreria.visualizza_film()


