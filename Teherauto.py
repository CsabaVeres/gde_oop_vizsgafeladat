from Auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, berleti_dij, teherkapacitas):
        super().__init__(rendszam, "Teherautó", berleti_dij)
        self.teherkapacitas = teherkapacitas

    def extra_informacio(self):
        return f"Teherkapacitás: {self.teherkapacitas} kg"