```mermaid
classDiagram
    class ElementoMenu {
        + codice: str
        + nome: str
        + prezzo: float
        + tempo_di_preparazione: float
        + allergeni: str
        + disponibile: bool
        + is_disponibile()
        + set_disponibile(stato)
        + to_string()
    }

    class PrimoPiatto {
        + tipo_pasta: str
        + vegetariano: bool
        + is_vegetariano()
        + to_string()
    }

    class SecondoPiatto {
        cottura: str
        + to_string()
    }

    class Ordine {
        + numero_ordine: int
        + data_ora: Date
        + stato: str
        + elementi: list
        + calcola_totale()
        + aggiungi_elemento(elemento)
        + rimuovi_elemento(elemento)
        + to_string()
    }

    Class Tavolo {
        + numero: int
        + posti: int
        + stato: str
        + is_libero()
        + aggiungi_ordine()
        + get_ordini_attivi()
        + to_string()
    }

ElementoMenu  <|-- PrimoPiatto
ElementoMenu  <|-- SecondoPiatto
Ordine "1" -- "*" ElementoMenu : contiene
Ordine "*" -- "1" Tavolo : assegnato
```