class Camera:
    def __init__(self, numero_camera, tipo_camera, disponibilita):
        self._numero_camera = numero_camera
        self._tipo_camera = tipo_camera
        self._disponibilita = disponibilita

    @property
    def numero_camera(self):
        return self._numero_camera
    
    @numero_camera.setter
    def numero_camera(self, numero_camera):
        self._numero_camera = numero_camera

    @property
    def tipo_camera(self):
        return self._tipo_camera
    
    @tipo_camera.setter
    def tipo_camera(self, tipo_camera):
        self._tipo_camera = tipo_camera

    @property
    def disponibilita(self):
        return self._disponibilita
    
    @disponibilita.setter
    def disponibilita(self, disponibilita):
        self._disponibilita = disponibilita


class Albergo:
    def __init__(self):
        self._camere = [Camera]

    def aggiungi_camera(self, camera):
        self._camere.append(camera)

    def prenota_camera(self, numero_camera):
        for camera in self._camere:
            if camera.numero_camera == numero_camera:
                camera.disponibilita = False
                return True
        return False
    
    def camere_disponibili(self):
        camere_disponibili = []
        for camera in self._camere:
            if camera.disponibilita:
                camere_disponibili.append(camera.numero_camera)
        return camere_disponibili
    
    def prenotazioni_effettuate(self):
        prenotazioni_effettuate = []
        for camera in self._camere:
            if not camera.disponibilita:
                prenotazioni_effettuate.append(camera.numero_camera)
        return prenotazioni_effettuate
    
camera1 = Camera(1, 'singola', True)
camera2 = Camera(2, 'doppia', True)

aggiungi_camera = Albergo()
aggiungi_camera.aggiungi_camera(camera1)
aggiungi_camera.aggiungi_camera(camera2)

prenota_camera = Albergo()
prenota_camera.prenota_camera(1)

camere_disponibili = Albergo()
print(camere_disponibili.camere_disponibili())

prenotazioni_effettuate = Albergo()
print(prenotazioni_effettuate.prenotazioni_effettuate())