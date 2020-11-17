import sqlite3

con = sqlite3.connect(':memory:')

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


def CzytajDane():
    cur.execute("""
           SELECT * FROM magazyn
       """)
    produkty = cur.fetchall()
    if(produkty == []):
        print("Baza jest pusta")
    else:
        for dane in produkty:
            print(dane['id'], dane['nazwa_produktu'], dane['ilosc_max'], dane['ilosc_aktualna'], dane['braki'],
                    dane['gatunek'], dane['rodzaj_produktu'])

