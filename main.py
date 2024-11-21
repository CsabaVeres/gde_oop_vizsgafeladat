from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from Autokolcsonzo import Autokolcsonzo
from Berles import Berles
from datetime import date

if __name__ == "__main__":
    # Autók létrehozása
    auto1 = Szemelyauto("ABC-123", 10000, 5)
    auto2 = Szemelyauto("DEF-321", 12000, 4)
    auto3 = Teherauto("GHI-789", 15000, 1000)
    auto4 = Szemelyauto("JKL-012", 11000, 5)
    auto5 = Teherauto("MNO-345", 20000, 2000)
    auto6 = Szemelyauto("PQR-678", 13000, 4)
    auto7 = Teherauto("STU-910", 25000, 2500)

    # Autókölcsönző létrehozása
    kolcsonzo = Autokolcsonzo("BestCar Rentals")
    kolcsonzo.autok_feltoltese([auto1, auto2, auto3, auto4, auto5, auto6, auto7])

    # Előre definiált bérlések létrehozása
    auto1.foglalt = True
    auto2.foglalt = True
    auto3.foglalt = True
    auto4.foglalt = True
    kolcsonzo.berlesek.append(Berles(auto1, date(2024, 11, 20)))
    kolcsonzo.berlesek.append(Berles(auto2, date(2024, 11, 21)))
    kolcsonzo.berlesek.append(Berles(auto3, date(2024, 11, 22)))
    kolcsonzo.berlesek.append(Berles(auto4, date(2024, 11, 23)))

    # Felhasználói interfész
    while True:
        print("\nAutókölcsönző Rendszer")
        print("1. Autók listázása")
        print("2. Autó bérlése")
        print("3. Bérlés lemondása")
        print("4. Bérlések listázása")
        print("5. Kilépés")
        valasztas = input("Válassz egy opciót: ")

        if valasztas == "1":
            kolcsonzo.autok_listazasa()
        elif valasztas == "2":
            rendszam = input("Add meg a bérelni kívánt autó rendszámát: ")
            kolcsonzo.berles(rendszam)
        elif valasztas == "3":
            rendszam = input("Add meg a lemondani kívánt bérlés rendszámát: ")
            kolcsonzo.berles_lemondasa(rendszam)
        elif valasztas == "4":
            kolcsonzo.berlesek_listazasa()
        elif valasztas == "5":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen opció!")