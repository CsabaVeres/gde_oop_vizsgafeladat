from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij
        self.foglalt = False

    def __str__(self):
        statusz = "Foglalt" if self.foglalt else "Elérhető"
        return f"{self.tipus} - {self.rendszam}, {self.berleti_dij} Ft/nap, Státusz: {statusz}"

    @abstractmethod
    def extra_informacio(self):
        pass