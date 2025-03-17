```mermaid
classDiagram
    class Corso {
        - titolo: str
        - descrizione: str
        - docente: str
        - studenti: list[Studente]
        + aggiungi_studente(Studente)
        + rimuovi_studente(Studente)
    }

    class Studente {
        - nome: str
        - cognome: str
        + tentativi: list[TentativoQuiz]
    }

    class Quiz {
        - titolo: str
        - punteggio_minimo: float
        + aggiungiDomanda(Domanda)
        + rimuoviDomanda(Domanda)
    }

    class Domanda {
        - testo: str
        - opzioni: list[str]
        - risposta_corretta: int
        + verifica_risposta(int)
    }

    class TentativoQuiz {
        - data: Date
        - risposte: list[str]
        - punteggio: float
        - quiz_superato: float
        + valuta_risposte()
        + verifica_superamento()
    }

    Corso "1" --> "*" Studente: seguito da
    Corso "1" --> "1" Quiz: include
    Quiz "1" --> "*" Domanda: include
    Studente "1" --> "*" TentativoQuiz: partecipa a
    Quiz "1" --> "*" TentativoQuiz: possibili