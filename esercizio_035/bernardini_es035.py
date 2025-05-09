import datetime
from enum import Enum

class Utente:
    def __init__(self, id_utente, nome_utente, email):
        self.id_utente = id_utente
        self.nome_utente = nome_utente
        self.email = email
        self.progetti = [ProgettoMusicale]

    def crea_progetto(self, titolo):
        id_progetto = len(self.progetti) + 1
        data_creazione = datetime.datetime.now()
        nuovo_progetto = ProgettoMusicale(id_progetto, titolo, data_creazione, "", "", self.id_utente)
        self.progetti.append(nuovo_progetto)
        return nuovo_progetto
    
    def progetti_per_genere(self):
        generi = {}
        for progetto in self.progetti:
            if progetto.genere_musicale in generi:
                generi[progetto.genere_musicale] += 1
            else:
                generi[progetto.genere_musicale] = 1
        return generi

    def conta_progetti_totali(self):
        return len(self.progetti)

    def strumento_piu_usato(self):
        strumenti = {}
        for progetto in self.progetti:
            for traccia in progetto.tracce:
                if traccia.strumento_utilizzato in strumenti:
                    strumenti[traccia.strumento_utilizzato] += 1
                else:
                    strumenti[traccia.strumento_utilizzato] = 1
        return max(strumenti, key=strumenti.get)


class ProgettoMusicale:
    def __init__(self, id_progetto, titolo_progetto, data_creazione, genere_musicale, descrizione, id_utente):
        self.id_progetto = id_progetto
        self.titolo_progetto = titolo_progetto
        self.data_creazione = data_creazione
        self.genere_musicale = genere_musicale
        self.tracce = [TracciaAudio]

    def aggiungi_traccia(self, nome_traccia):
        id_traccia = len(self.tracce) + 1
        durata_secondi = 0
        volume_db = 0
        sequenza_note_manuali = ""
        strumento_utilizzato = None
        nuova_traccia = TracciaAudio(id_traccia, nome_traccia, durata_secondi, volume_db, sequenza_note_manuali, strumento_utilizzato)
        self.tracce.append(nuova_traccia)
        return nuova_traccia 

    def percentuale_tracce_con_effetti(self):
        tracce_con_effetti = sum(1 for traccia in self.tracce if traccia.effetti_applicati)
        if len(self.tracce) == 0:
            return 0
        return (tracce_con_effetti / len(self.tracce)) * 100

    def effetto_piu_usato(self):
        effetti = {}
        for traccia in self.tracce:
            for effetto in traccia.effetti_applicati:
                if effetto.nome_effetto in effetti:
                    effetti[effetto.nome_effetto] += 1
                else:
                    effetti[effetto.nome_effetto] = 1
        return max(effetti, key=effetti.get)


class TracciaAudio:
    def __init__(self, id_traccia, nome_traccia, durata_secondi, volume_db, sequenza_note_manuali, strumento_utilizzato):
        self.id_traccia = id_traccia
        self.nome_traccia = nome_traccia
        self.durata_secondi = durata_secondi
        self.volume_db = volume_db
        self.sequenza_note_manuali = sequenza_note_manuali
        self.strumento_utilizzato = strumento_utilizzato
        self.effetti_applicati = [EffettoAudio]

    def aggiungi_strumento(self, strumento):
        self.strumento_utilizzato = strumento
        self.durata_secondi = 0
        self.volume_db = 0
        self.sequenza_note_manuali = ""
        self.effetti_applicati = []

    def applica_effetto(self, effetto):
        if effetto not in self.effetti_applicati:
            self.effetti_applicati.append(effetto)
        else:
            print(f"L'effetto {effetto.nome_effetto} è già applicato a questa traccia.")

    def rimuovi_effetto(self, effetto):
        if effetto in self.effetti_applicati:
            self.effetti_applicati.remove(effetto)
        else:
            print(f"L'effetto {effetto.nome_effetto} non è applicato a questa traccia.")

    def imposta_sequenza_note(self, sequenza_note):
        self.sequenza_note_manuali = str(sequenza_note)
        self.durata_secondi = len(sequenza_note.split()) * 0.5
    
    def modifica_volume(self, nuovo_volume_db):
        self.volume_db = float(nuovo_volume_db)

    def ha_effetti(self):
        return len(self.effetti_applicati) > 0

    def numero_note(self):
        return len(self.sequenza_note_manuali.split()) if self.sequenza_note_manuali else 0

class EffettoAudio:
    def __init__(self, id_effetto, nome_effetto, tipo_effetto_audio):
        self.id_effetto = id_effetto
        self.nome_effetto = nome_effetto
        self.tipo_effetto_audio = tipo_effetto_audio


class StrumentoVirtuale:
    def __init__(self, id_strumento, nome_strumento, tipo_strumento_virtuale):
        self.id_strumento = id_strumento
        self.nome_strumento = nome_strumento
        self.tipo_strumento_virtuale = tipo_strumento_virtuale

    def suona_nuota(self, nota, durata):
        print(f"Suonando {nota} per {durata} secondi con lo strumento {self.nome_strumento}")


class TipoEffetto(Enum):
    RIVERBERO = "Riverbero"
    DELAY = "Delay"
    DISTORSIONE = "Distorsione"

class TipoStrumento(Enum):
    BATTERIA = "Batteria"
    CHITARRA = "Chitarra"
    BASSO = "Basso"


# Esempio di utilizzo
if __name__ == "__main__":
    # Creazione utente
    utente = Utente("u1", "Mario Rossi", "mario@example.com")  # type: ignore # noqa: F821

    # Creazione progetti
    progetto_rock = utente.crea_progetto("La Mia Canzone Rock")
    progetto_rock.genere_musicale = "Rock"
    
    progetto_jazz = utente.crea_progetto("Jazz Session")
    progetto_jazz.genere_musicale = "Jazz"

    # Aggiunta tracce al progetto rock
    traccia_basso = progetto_rock.aggiungi_traccia("Linea di basso")
    traccia_chitarra = progetto_rock.aggiungi_traccia("Chitarra ritmica")

    # Creazione e aggiunta strumenti
    basso = StrumentoVirtuale("s1", "Basso elettrico", TipoStrumento.BASSO)  # type: ignore # noqa: F821
    chitarra = StrumentoVirtuale("s2", "Chitarra elettrica", TipoStrumento.CHITARRA)  # type: ignore # noqa: F821
    
    traccia_basso.aggiungi_strumento(basso)
    traccia_chitarra.aggiungi_strumento(chitarra)

    # Aggiunta effetti
    distorsione = EffettoAudio("e1", "Distorsione Heavy", TipoEffetto.DISTORSIONE)  # type: ignore # noqa: F821
    delay = EffettoAudio("e2", "Delay Echo", TipoEffetto.DELAY)  # type: ignore # noqa: F821
    
    traccia_basso.applica_effetto(distorsione)
    traccia_chitarra.applica_effetto(distorsione)
    traccia_chitarra.applica_effetto(delay)

    # Impostazione volume e note
    traccia_basso.modifica_volume(-6)
    traccia_basso.imposta_sequenza_note("C2 G2 C3 E3")
    traccia_chitarra.modifica_volume(-3)
    traccia_chitarra.imposta_sequenza_note("C4 G4 C5 E5 G5")

    # Test dei metodi statistici
    print("\nStatistiche a livello utente:")
    print(f"Progetti per genere: {utente.progetti_per_genere()}")
    print(f"Numero totali progetti: {utente.conta_progetti_totali()}")
    print(f"Strumento più usato: {utente.strumento_piu_usato().nome_strumento}")

    print("\nStatistiche progetto rock:")
    print(f"Percentuale tracce con effetti: {progetto_rock.percentuale_tracce_con_effetti()}%")
    print(f"Effetto più usato: {progetto_rock.effetto_piu_usato().nome_effetto}")

    print("\nStatistiche traccia basso:")
    print(f"Ha effetti: {traccia_basso.ha_effetti()}")
    print(f"Numero di note: {traccia_basso.numero_note()}")