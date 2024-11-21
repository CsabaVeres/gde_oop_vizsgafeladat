from Auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, berleti_dij, ulesek_szama):
        super().__init__(rendszam, "Személyautó", berleti_dij)
        self.ulesek_szama = ulesek_szama

    def extra_informacio(self):
        return f"Ülések száma: {self.ulesek_szama}"