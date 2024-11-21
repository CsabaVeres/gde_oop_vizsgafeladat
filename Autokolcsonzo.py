from Berles import Berles
from datetime import date

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def autok_feltoltese(self, autok):
        self.autok.extend(autok)

    def autok_listazasa(self):
        print("Elérhető autók:")
        for auto in self.autok:
            print(auto)

    def berles(self, rendszam):
        for auto in self.autok:
            if auto.rendszam == rendszam and not auto.foglalt:
                auto.foglalt = True
                uj_berles = Berles(auto, date.today())
                self.berlesek.append(uj_berles)
                print(f"Sikeres bérlés: {auto.rendszam}")
                return
        print("Nem elérhető az autó vagy nem létezik.")

    def berles_lemondasa(self, rendszam):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam:
                berles.auto.foglalt = False
                self.berlesek.remove(berles)
                print(f"Sikeresen lemondva: {rendszam}")
                return
        print("Nincs ilyen bérlés.")

    def berlesek_listazasa(self):
        print("Aktuális bérlések:")
        for berles in self.berlesek:
            print(berles)