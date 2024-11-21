class Libro:
    def __init__(self, titolo, autore, pagine):
        self._titolo = titolo
        self._autore = autore
        self._pagine = pagine

    def get_titolo(self):
        if self._titolo != None:
            return self._titolo
        return False

    def set_titolo(self, titolo):
        if self._titolo != '':
            self._titolo = titolo
            return True
        return False

    def get_autore(self):
        if self._autore != None:
            return self._autore
        return False

    def set_autore(self, autore):
        if self._autore != '':
            self._autore = autore
            return True
        return False
    
    def get_pagine(self):
        if self._pagine != None:
            return self._pagine
        return False

    def set_pagine(self, pagine):
        if self._pagine != '':
            self._pagine = pagine
            return True
        return False

libro = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1200)
print(libro._titolo) 
libro._titolo = "Lo Hobbit" 
print(libro._titolo)        