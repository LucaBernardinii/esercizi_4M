```mermaid
classDiagram
    class Albergo {
        - camere: list[Camera]

        + aggiungi_camera() -> None
        + prenota_camera() -> bool
        + camere_disponibili() -> list[Camera]
        + prenotazioni_effettuate() -> list
    }

    class Camera {
        - numero_camera: int
        - tipo_camera: str
        - disponibilita: str
    }

Camera "1..*" --> "1" Albergo: contenuta
```