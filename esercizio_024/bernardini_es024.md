```mermaid
classDiagram
    class Film {
        - titolo: str
        - regista: str
        - anno_uscita: int
        - genere: str
        - valutazione: float
        }
    
    class Libreria {
        - lista_film: list[Film]
        + aggiungi_film()
        + cerca_film()
        + visualizza_film()
        + valutazione_film()
        }

Libreria "1" --> "1..*" Film: contiene    

```