class Libro:
    def __init__(self, _titolo, _autore, _pagine):
        self._titolo = _titolo
        self._autore = _autore
        self._pagine = _pagine

    def get_titolo(self):
        if len(titolo) > 0:
            return self._titolo
        else:
            print("Il titolo è vuoto.")

    def set_titolo(self, _titolo):
        self._titolo = _titolo

    def get_autore(self):
        if len(_autore) > 0:
            return self._autore
        else:
            print("L'autore è vuoto.")

    def set_autore(self, _autore):
        self._autore = _autore

    def get_pagine(self):
        if len(_pagine) > 0:
            return self._pagine
        else:
            print("Il libro non ha pagine.")

    def set_pagine(self, _pagine):
        self._pagine = _pagine

libro = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1200)
print(libro._titolo) 
libro._titolo = "Lo Hobbit" 
print(libro._titolo)

        