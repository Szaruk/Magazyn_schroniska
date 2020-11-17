import sqlite3

con = sqlite3.connect('zwierzaki.db')

con.row_factory = sqlite3.Row

cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS magazyn (
        id INTEGER PRIMARY KEY ASC,
        nazwa_produktu varchar(250) NOT NULL,
        ilosc_max int NOT NULL,
        ilosc_aktualna int NOT NULL,
        braki INT NOT NULL,
        gatunek varchar(45) NOT NULL,
        rodzaj_produktu varchar(45) NOT NULL
)""")

cur.execute('INSERT INTO magazyn VALUES(NULL, ?, ?, ?, ?, ?, ?);', ('Royal Canin Maxi Adult', '100', '50', '50', 'pies', 'Karma'))
cur.execute('INSERT INTO magazyn VALUES(NULL, ?, ?, ?, ?, ?, ?);', ('Smycze psy', '100', '50', '50', 'pies', 'Smycz'))
cur.execute('INSERT INTO magazyn VALUES(NULL, ?, ?, ?, ?, ?, ?);', ('Koce', '100', '50', '50', 'wszystkie', 'Koc'))


def CzytajMagazyn():
    cur.execute("""
           SELECT * FROM magazyn
       """)
    produkty = cur.fetchall()
    if(produkty == []):
        print("Baza jest pusta")
    else:
        for dane in produkty:
            print(dane['id'], dane['nazwa_produktu'], dane['ilosc_max'], dane['ilosc_aktualna'], dane['braki'],dane['gatunek'], dane['rodzaj_produktu'])

def WyswietlIlosciProduktow():
    cur.execute("SELECT id, rodzaj_produktu FROM magazyn")
    produkt_rodzaj = cur.fetchall()
    for rodzaj in produkt_rodzaj:
        print(str(rodzaj['id']) + "." + str(rodzaj['rodzaj_produktu']))



"""
def AktualizujProdukt():
    cur.execute("SELECT nazwa_produktu FROM magazyn")
    nazwy_produktow = cur.fetchall()
    if (nazwy_produktow == []):
        print("Baza jest pusta")
    else:
        for nazwy in nazwy_produktow:
            print(nazwy['nazwa_produktu'])
          
    cur.execute('SELECT ilosc_aktualna FROM magazyn WHERE nazwa_produktu = ?', (nazwa,))
    ilosc_aktualna = cur.fetchone()[0]
    return (ilosc_aktualna)
    """