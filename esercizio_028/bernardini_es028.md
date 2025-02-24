```mermaid
classDiagram
    class Serra {
        +str nome
        +float superficie
        +list[Sensore] sensori
        +list[Sezione] sezioni
        +list[Dispositivo] dispositivi
        +list[Coltivazione] coltivazioni
        +monitoraParametri() dict
        +attivaIrrigazione(str nome_sezione) bool
    }

    class Sensore {
        +str tipo
        +str posizione
        +float valore
        +str unitaMisura
        +bool attivo
        +Sezione sezione
        +Serra serra
    }

    class Sezione {
        +str nome
        +float superficie
        +Coltivazione coltivazione
        +list[Sensore] sensori
        +list[Dispositivo] dispositivi
        +Serra serra
    }

    class Dispositivo {
        +str nome
        +str tipo
        +str stato
        +Serra serra
        +Sezione sezione
        +attiva() None
        +disattiva() None
        +verificaStato() bool
    }

    class Coltivazione {
        +str specie
        +datetime dataInizio
        +datetime dataRaccoltoPrevista
        +float quantitaPrevista
        +str stato
        +Serra serra
        +Sezione sezione
    }


    Serra "1" .. "*" Sensore : monitora con
    Serra "1" .. "*" Sezione : suddivisa in
    Serra "1" .. "*" Dispositivo : controlla
    Serra "1" .. "*" Coltivazione : gestisce
    Sezione "1" -- "*" Sensore : contiene
    Sezione "1" -- "*" Dispositivo : utilizza
    Sezione "1" -- "1" Coltivazione : ospita
```

### Serra automatizzata

Un'azienda agricola moderna vuole automatizzare la gestione della propria serra. Ogni serra viene utilizzata per diverse coltivazioni e deve essere monitorata costantemente. Per garantire la crescita ottimale delle _piante_, vengono utilizzati vari dispositivi e sensori che controllano le condizioni ambientali.

Le serre sono divise in sezioni separate per ospitare colture diverse che richiedono condizioni specifiche. _Il sistema deve tenere traccia di cosa viene coltivato, quando è stato piantato e quando si prevede il raccolto. Per ogni coltivazione, si deve poter calcolare lo stadio di crescita e stimare la quantità prevista al raccolto._

I vari dispositivi presenti nella serra (come irrigatori, ventilatori, luci) possono essere attivati o disattivati. I sensori forniscono continuamente letture delle condizioni ambientali attraverso un metodo di rilevazione.

_Il sistema deve essere in grado di intervenire automaticamente su una determinata sezione quando necessario, monitorando i parametri ambientali di tutta la serra (attraverso il metodo monitoraParametri che restituisce un dizionario con i valori rilevati) e attivando l'irrigazione (tramite il metodo attivaIrrigazione che attiva tutti i dispositivi di tipo irrigatore presenti nella sezione specificata)_.