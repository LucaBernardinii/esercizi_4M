from datetime import date

class Utente:
    def __init__ (self, nome_utente, email, password):
        self._nome_utente = nome_utente
        self._email = email
        self._password = password
        self.profilo = Profilo
        self._album = [Album]
        self._seguiti = [Utente]

    @property
    def nome_utente(self):
        return self._nome_utente
    
    nome_utente.setter
    def nome_utente(self, nuovo_nome):
        self._nome_utente = nuovo_nome

    @property
    def email(self):
        return self._email
    
    email.setter
    def email(self, nuova_email):
        self._email = nuova_email

    @property
    def password(self):
        return self._password
    
    password.setter
    def password(self, nuova_password):
        self._password = nuova_password


class Foto:
    def __init__ (self, id, titolo, descrizione, data_caricamento):
        self._id = id
        self._titolo = titolo
        self._descrizione = descrizione
        self._data_caricamento = data_caricamento
        self._utente = Utente
        self._album = [Album]
        self._commenti = [Commento]

    @property
    def id(self):
        return self._id
    
    id.setter
    def id(self, nuovo_id):
        self._id = nuovo_id

    @property
    def titolo(self):
        return self._titolo
    
    titolo.setter
    def titolo(self, nuovo_titolo):
        self._titolo = nuovo_titolo

    @property
    def descrizione(self):
        return self._descrizione
    
    descrizione.setter
    def descrizione(self, nuova_descrizione):
        self._descrizione = nuova_descrizione

    @property
    def data_caricamento(self):
        return self._data_caricamento
    
    data_caricamento.setter
    def data_caricamento(self, nuova_data):
        self._data_caricamento = nuova_data

    
class Album:
    def __init__ (self, titolo, descrizione):
        self._titolo = titolo
        self._descrizione = descrizione
        self._utente = Utente
        self._foto = [Foto]

    @property
    def titolo(self):
        return self._titolo
    
    titolo.setter
    def titolo(self, nuovo_titolo):
        self._titolo = nuovo_titolo

    @property
    def descrizione(self):
        return self._descrizione
    
    descrizione.setter
    def descrizione(self, nuova_descrizione):
        self._descrizione = nuova_descrizione

    
class Commento:
    def __init__(self, descrizione):
        self._descrizione = descrizione
        self._utente = Utente
        self._foto = Foto

    @property
    def descrizione(self):
        return self._descrizione
    
    descrizione.setter
    def descrizione(self, nuova_descrizione):
        self._descrizione = nuova_descrizione

class Profilo:
    def __init__(self, immagine, biografia):
        self._immagine = immagine
        self._biografia = biografia
        self._utente = Utente

    @property
    def immagine(self):
        return self._immagine
    
    immagine.setter
    def immagine(self, nuova_immagine):
        self._immagine = nuova_immagine

    @property
    def biografia(self):
        return self._biografia
    
    biografia.setter
    def biografia(self, nuova_biografia):
        self._biografia = nuova_biografia

    