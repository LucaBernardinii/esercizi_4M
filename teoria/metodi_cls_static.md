#### Metodi di classe

I metodi di classe operano sugli attributi di classe. Per definire un metodo di classe, si utilizza il decoratore `@classmethod`, e il primo argomento del metodo sarà `cls`, che si riferisce alla classe stessa.

```python
class Studente:
    scuola = "Liceo Classico"  # Attributo di classe

    def __init__(self, nome, eta, matricola):
        self.nome = nome
        self.eta = eta
        self.matricola = matricola

    @classmethod
    def cambia_scuola(cls, nuova_scuola):
        cls.scuola = nuova_scuola
```

> **Esempio**: Cambiare l’attributo di classe `scuola` utilizzando un metodo di classe.

```python
Studente.cambia_scuola("Liceo Scientifico")
print(Studente.scuola)  # Output: Liceo Scientifico
```

In questo esempio, il metodo `cambia_scuola()` modifica l’attributo di classe `scuola` per tutte le istanze.

#### Metodi statici

I metodi statici, definiti con il decoratore `@staticmethod`, non accedono né agli attributi di istanza né a quelli di classe. Sono funzioni che appartengono logicamente alla classe, ma non dipendono né dagli oggetti né dalla classe stessa.

```python
class Studente:
    @staticmethod
    def matricola_valida(matricola):
        return matricola.isdigit()
```

> **Esempio**: Verifica se la matricola è valida prima di creare uno studente.

```python
print(Studente.matricola_valida("123456"))  # Output: True
print(Studente.matricola_valida("123ABC"))  # Output: False
```

I metodi statici possono essere utilizzati quando una funzione ha una relazione logica con la classe, ma non necessita di accedere ai dati dell’istanza o della classe.