```mermaid
classDiagram
    class Azienda {
        + progetti_attivi: list[Progetto]
        + teams: list[Team]
        + dipendenti: list[membro]
        + clienti: list[Cliente]
        + assegna_team(team: Team, progetto: Progetto) -> None
        + get_teams() -> teams
        + get_progetti_attivi() -> progetti_attivi
        + comunica_avanzamento(progetto: Progetto) -> None
        + paga_membro(membro: Membro) -> None
        + aggiorna_costi_progetto(progetto: Progetto) -> None
        + confronta_budget_costi(progetto: Progetto) -> None
    }

    class Progetto {
        + budget_iniziale: float
        + costi_effettivi: float
        + stato_avanzamento: int
        + documenti: list[Documento]
        + tasks: list[Task]
        + crea_task() -> None
        + rimuovi_task() -> None
        + get_documenti() -> documenti
        + aggiorna_avanzamento() -> stato_avanzamento
    }

    class Documento {
        + tipo_documento: str
        + contenuto: str
    }

    class Responsabile {
        + nome: str
        + cognome: str
        + membri_coordinati: list[Membro]
        + assegna_task(task: Task, membro: Membro) -> None
        + rimuovi_task(membro: Membro) -> None
    }

    class Task {
        + priorita: str
        + completamento: bool
    }

    class Cliente {
        + nome: str
        + progetti_attivi: list [Progetto]
        + commissiona_progetto() -> None
    }

    class Team {
        + lista_membri: list[Membro]
        + documenti_generati: list[Documento]
        + risorse_utilizzabili: list[Risorsa]
        + genera_documento() -> Documento
        + utilizza_risorsa() -> None
    }

    class Membro {
        + nome: str
        + cognome: str
        + competenza: str
        + disponibilita_oraria: str
        + stipendio: float
        + tasks_assegnate: list[Task]
        + completa_task(task: Task) -> None
    }

    class Risorsa {
        + tipologia: str
        + quantita: int
    }

Azienda "1" --> "*" Team: composta da
Progetto "1" --> "*" Task: formato da
Cliente "1" --> "*" Progetto: commissiona
Team "1" --> "*" Membro: formato da
Task "*" --> "1" Membro: assegnata a
Team "1" --> "*" Risorsa: utilizza
Progetto "1" --> "1" Responsabile: ha
Responsabile "1" --> "*" Membro: coordina
Azienda "1" --> "*" Progetto: tiene traccia
Azienda "1" --> "*" Risorsa: gestisce
Documento "*" --> "1" Progetto: relativi a
Team "1" --> "*" Documento: genera
Responsabile "1" --> "*" Task: gestisce
Azienda "1" --> "*" Cliente: collabora con
Azienda "1" --> "*" Membro: paga
```

Azienda è la classe principale, ha una gestione generale e può assegnare team a diversi progetti, gestire i costi dei progetti e comunicare con il cliente.

Un cliente può commissionare diversi progetti che vengono divisi in tasks e assegnati ai vari membri dal responsabile del progetto.

Ho creato una classe a parte per Documento per relazionarli più facilmente con i progetti e assegnargli degli attributi.
