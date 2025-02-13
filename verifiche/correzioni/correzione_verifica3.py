from datetime import date

class Libro:
    def __init__(self, titolo: str, data_pubblicazione: date, autore: 'Autore'):
        self.titolo = titolo
        self.data_pubblicazione = data_pubblicazione
        self.data_prestito = None
        self.data_restituzione = None
        self.utente_corrente = None
        self.autore = autore
        autore.aggiungi_libro(self)

    def disponibile(self) -> bool:
        return self.utente_corrente is None

    def __str__(self):
        return f"{self.titolo} di {self.autore.nome} {self.autore.cognome}"

class Autore:
    def __init__(self, nome: str, cognome: str):
        self.nome = nome
        self.cognome = cognome
        self.libri = []

    def aggiungi_libro(self, libro: Libro):
        self.libri.append(libro)

    def ottieni_libri(self):
        return self.libri

class Utente:
    def __init__(self, nome: str, cognome: str):
        self.nome = nome
        self.cognome = cognome
        self.libri_in_prestito = []

    def ottieni_libri_in_prestito(self):
        return self.libri_in_prestito

    def __str__(self):
        return f"{self.nome} {self.cognome}"

class Biblioteca:
    def __init__(self):
        self.libri = []
        self.utenti = []

    def aggiungi_libro(self, libro: Libro):
        self.libri.append(libro)

    def aggiungi_utente(self, utente: Utente):
        self.utenti.append(utente)

    def ottieni_libri(self):
        return self.libri

    def ottieni_utenti(self):
        return self.utenti

    def presta_libro(self, libro: Libro, utente: Utente, data_prestito: date) -> bool:
        if libro.disponibile():
            libro.data_prestito = data_prestito
            libro.utente_corrente = utente
            utente.libri_in_prestito.append(libro)
            return True
        return False

    def restituisci_libro(self, libro: Libro, data_restituzione: date) -> bool:
        if libro.utente_corrente is not None:
            libro.data_restituzione = data_restituzione
            libro.utente_corrente.libri_in_prestito.remove(libro)
            libro.utente_corrente = None
            return True
        return False

    def cerca_libro_per_titolo(self, titolo: str):
        return [libro for libro in self.libri if libro.titolo == titolo]

    def cerca_libri_per_autore(self, autore: Autore):
        return autore.ottieni_libri()

    def libri_disponibili(self):
        return [libro for libro in self.libri if libro.disponibile()]

def main():
    # Creazione biblioteca
    biblioteca = Biblioteca()

    # Creazione autori
    autore1 = Autore("Alessandro", "Manzoni")
    autore2 = Autore("Italo", "Calvino")

    # Creazione libri
    libro1 = Libro("I Promessi Sposi", date(1827, 1, 1), autore1)
    libro2 = Libro("Il barone rampante", date(1957, 1, 1), autore2)
    biblioteca.aggiungi_libro(libro1)
    biblioteca.aggiungi_libro(libro2)

    # Creazione utenti
    utente1 = Utente("Mario", "Rossi")
    utente2 = Utente("Laura", "Bianchi")
    biblioteca.aggiungi_utente(utente1)
    biblioteca.aggiungi_utente(utente2)

    # Test operazioni
    print("Libri disponibili:", [str(l) for l in biblioteca.libri_disponibili()])

    # Prestito libro
    biblioteca.presta_libro(libro1, utente1, date.today())
    print(f"\nLibro '{libro1}' prestato a {utente1}")

    # Verifica disponibilità
    print("Libri disponibili dopo il prestito:", [str(l) for l in biblioteca.libri_disponibili()])

    # Restituzione libro
    biblioteca.restituisci_libro(libro1, date.today())
    print(f"\nLibro '{libro1}' restituito da {utente1}")

    # Verifica disponibilità dopo restituzione
    print("Libri disponibili dopo la restituzione:", [str(l) for l in biblioteca.libri_disponibili()])

if __name__ == "__main__":
    main()