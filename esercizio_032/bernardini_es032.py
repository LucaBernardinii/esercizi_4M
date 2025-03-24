class Utente:
    def __init__(self, nome_utente, email, password):
        self._nome_utente = nome_utente
        self._email = email
        self._password = password
        self._video_visti = []
        self._playlist_create = []
        self._abbonamento = Abbonamento

    @property
    def nome_utente(self):
        return self._nome_utente
    
    nome_utente.setter
    def nome_utente(self, nome_utente):
        self._nome_utente = nome_utente

    @property
    def email(self):
        return self._email
    
    email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password
    
    password.setter
    def password(self, password):
        self._password = password

    def guarda_video(self, video):
        self._video_visti.append(video)

    def crea_playlist(self, playlist):
        self._playlist_create.append(playlist)

    def aggiungi_video_playlist(self, playlist, video):
        playlist._video.append(video)

    def rimuovi_video_playlist(self, playlist, video):
        playlist._video.remove(video)

    def cancella_playlist(self, playlist):
        self._playlist_create.remove(playlist)

    def commenta_video(self, video, commento):
        video._commenti.append(commento)


class Video:
    def __init__(self, titolo, descrizione, url, durata):
        self._titolo = titolo
        self._descrizione = descrizione
        self._url = url
        self._durata = durata
        self._commenti = []

    @property
    def titolo(self):
        return self._titolo
    
    titolo.setter
    def titolo(self, titolo):
        self._titolo = titolo

    @property
    def descrizione(self):
        return self._descrizione
    
    descrizione.setter
    def descrizione(self, descrizione):
        self._descrizione = descrizione

    @property
    def url(self):
        return self._url
    
    url.setter
    def url(self, url):
        self._url = url

    @property
    def durata(self):
        return self._durata
    
    durata.setter
    def durata(self, durata):
        self._durata = durata

    def aggiungi_commento(self, commento):
        self._commenti.append(commento)


class Playlist:
    def __init__(self, nome, creatore: Utente):
        self._nome = nome
        self._creatore = creatore
        self._video = []

    @property
    def nome(self):
        return self._nome
    
    nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def creatore(self):
        return self._creatore
    
    creatore.setter
    def creatore(self, creatore):
        self._creatore = creatore

    def aggiungi_video(self, video):
        self._video.append(video)

    def rimuovi_video(self, video):
        self._video.remove(video)


class Abbonamento:
    def __init__(self, tipo, prezzo, data_inizio, data_fine):
        self._tipo = tipo
        self._prezzo = prezzo
        self._data_inizio = data_inizio
        self._data_fine = data_fine

    @property
    def tipo(self):
        return self._tipo
    
    tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def prezzo(self):
        return self._prezzo
    
    prezzo.setter
    def prezzo(self, prezzo):
        self._prezzo = prezzo

    @property
    def data_inizio(self):
        return self._data_inizio
    
    data_inizio.setter
    def data_inizio(self, data_inizio):
        self._data_inizio = data_inizio

    @property
    def data_fine(self):
        return self._data_fine
    
    data_fine.setter
    def data_fine(self, data_fine):
        self._data_fine = data_fine


class Commento:
    def __init__(self, autore: Utente, testo, data_pubblicazione, video: Video):
        self._autore = autore
        self._testo = testo
        self._data_pubblicazione = data_pubblicazione
        self._video = video

    @property
    def autore(self):
        return self._autore
    
    autore.setter
    def autore(self, autore):
        self._autore = autore

    @property
    def testo(self):
        return self._testo
    
    testo.setter
    def testo(self, testo):
        self._testo = testo

    @property
    def data_pubblicazione(self):
        return self._data_pubblicazione
    
    data_pubblicazione.setter
    def data_pubblicazione(self, data_pubblicazione):
        self._data_pubblicazione = data_pubblicazione

    @property
    def video(self):
        return self._video
    
    video.setter
    def video(self, video):
        self._video = video


utente = Utente("Mario", "mario.boh@gmail.com", "password")
video = Video("Titolo", "Descrizione", "url", 10)
playlist = Playlist("Playlist", utente)
abbonamento = Abbonamento("Premium", 10, "01/01/2021", "01/01/2022")
commento = Commento(utente, "Testo", "01/01/2021", video)
utente.guarda_video(video)
utente.crea_playlist(playlist)
utente.aggiungi_video_playlist(playlist, video)
utente.rimuovi_video_playlist(playlist, video)
utente.cancella_playlist(playlist)
utente.commenta_video(video, commento)
video.aggiungi_commento(commento)
playlist.aggiungi_video(video)
playlist.rimuovi_video(video)