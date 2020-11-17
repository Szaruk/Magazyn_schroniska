from magazyn import *

class Produkt:
    braki = 0
    def __init__(self,nazwa_produktu, ilosc_max, ilosc_aktualna, gatunek, rodzaj_produktu):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc_max = ilosc_max
        self.ilosc_aktualna = ilosc_aktualna
        self.gatunek = gatunek
        self.rodzaj_produktu = rodzaj_produktu


    def DodajProdukt(self):
        self.braki = self.ilosc_max - self.ilosc_aktualna
        nowy_produkt = "Nazwa produktu: " + self.nazwa_produktu + " Ilość maksymalna: " + str(self.ilosc_max) + \
                       " Ilość aktualna: " + str(self.ilosc_aktualna) + " Braki: " + str(self.braki) +  " Gatunek: " + self.gatunek + " Rodzaj_produktu: " + self.rodzaj_produktu

        cur.execute('INSERT INTO magazyn VALUES(Null,?,?,?,?,?,?);',(self.nazwa_produktu,self.ilosc_max,self.ilosc_aktualna,self.braki,self.gatunek,self.rodzaj_produktu))
        con.commit()
        return nowy_produkt

