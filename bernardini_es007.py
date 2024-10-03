class MaterialeBiblioteca:
    def __init__(self, titolo: str, anno_pubblicazione: int, disponibile: True):
        self.titolo = titolo
        self.anno_pubblicazione = anno_pubblicazione
        self.disponibile = disponibile

    def prestito(disponibile):
        disponibile = False
    
    def restituzione(disponibile):
        disponibile = True

    def get_titolo(self):
        return self.titolo
    
    def set_titolo(self, titolo):
        self.titolo = titolo

    def get_anno_pubblicazione(self):
        return self.anno_pubblicazione
    
    def set_anno_pubblicazione(self, anno_pubblicazione):
        self.anno_pubblicazione = anno_pubblicazione
    
    def is_disponibile(self):
        return self.disponibile
    
    






libro = Libro("Il Signore degli Anelli", 1954, "J.R.R. Tolkien", 1178)
print(libro.get_titolo())
print(libro.get_autore()) 
libro.prestito()
print(libro.is_disponibile())
libro.restituzione()
print(libro.is_disponibile())

rivista = Rivista("National Geographic", 2023, 5, "Maggio")
print(rivista.get_titolo())
print(rivista.get_numero_edizione())

dvd = DVD("Inception", 2010, "Christopher Nolan", 148)
print(dvd.get_titolo())
print(dvd.get_regista())

materiali = [libro, rivista, dvd]
risultato = MaterialeBiblioteca.ricerca(materiali, titolo="Inception")
print(risultato.get_titolo())