from klasy import *


if __name__ == '__main__':
    while(True):
        print("1.Dodaj produkt\n2.Wyświetl magazyn\n3.Aktualizuj ilosc")
        opcja = int(input("Wybierz opcje: "))
        if(opcja == 1):
            rodzaj_produktu = input("Podaj rodzaj produktu: ")
            nazwa_produktu = input("Podaj nazwe produktu: ")
            ilosc_max = int(input("Podaj wartośc maksymalną: "))
            ilosc_aktualna = int(input("Podaj wartość aktualną: "))
            gatunek = input("Podaj gatunek: ")
            nowyProdukt = Produkt(nazwa_produktu, ilosc_max, ilosc_aktualna, gatunek, rodzaj_produktu)
            print(nowyProdukt.DodajProdukt())
        elif(opcja == 2):
            CzytajMagazyn()
            print()
        elif(opcja == 3):
            WyswietlIlosciProduktow()
            print()