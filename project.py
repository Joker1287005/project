import tkinter as tk
from tkinter import messagebox
import datetime

class Szoba:
    def __init__(self, szobaszam, szobatipus, ar):
        self.szobaszam = szobaszam
        self.szobatipus = szobatipus
        self.ar = ar
        self.foglalt_datumok = []

    def foglalas(self, datum):
        self.foglalt_datumok.append(datum)

    def lemondas(self, datum):
        if datum in self.foglalt_datumok:
            self.foglalt_datumok.remove(datum)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = {}

    def szoba_hozzaadasa(self, szobaszam, szobatipus, ar):
        if szobaszam not in self.szobak:
            self.szobak[szobaszam] = Szoba(szobaszam, szobatipus, ar)

    def foglalas(self, szobaszam, datum):
        if szobaszam in self.szobak:
            szoba = self.szobak[szobaszam]
            if datum in szoba.foglalt_datumok:
                messagebox.showerror("Hiba", "A szoba már foglalt ezen a dátumon.")
            else:
                szoba.foglalas(datum)
                messagebox.showinfo("Siker", f"Foglalás sikeres! Szoba: {szobaszam} ({szoba.szobatipus}), Ár: {szoba.ar} Ft")
        else:
            messagebox.showerror("Hiba", "Nincs ilyen szoba.")

    def lemondas(self, szobaszam, datum):
        if szobaszam in self.szobak:
            szoba = self.szobak[szobaszam]
            if datum in szoba.foglalt_datumok:
                szoba.lemondas(datum)
                messagebox.showinfo("Siker", "Lemondás sikeres!")
            else:
                messagebox.showerror("Hiba", "Nincs ilyen foglalás ezen a dátumon.")
        else:
            messagebox.showerror("Hiba", "Nincs ilyen szoba.")

    def listaz_foglalasok(self):
        foglalasok = ""
        for szobaszam, szoba in self.szobak.items():
            for datum in szoba.foglalt_datumok:
                foglalasok += f"Szoba: {szobaszam} ({szoba.szobatipus}), Ár: {szoba.ar} Ft, Dátum: {datum}\n"
        if not foglalasok:
            messagebox.showinfo("Információ", "Nincsenek foglalások.")
        else:
            messagebox.showinfo("Foglalások", foglalasok)

def make_reservation():
    szobaszam = int(szoba_entry.get())
    datum_str = datum_entry.get()
    try:
        datum = datetime.datetime.strptime(datum_str, "%Y-%m-%d")
        szalloda.foglalas(szobaszam, datum)
    except ValueError:
        messagebox.showerror("Hiba", "Hibás dátum formátum.")

def cancel_reservation():
    szobaszam = int(szoba_entry.get())
    datum_str = datum_entry.get()
    try:
        datum = datetime.datetime.strptime(datum_str, "%Y-%m-%d")
        szalloda.lemondas(szobaszam, datum)
    except ValueError:
        messagebox.showerror("Hiba", "Hibás dátum formátum.")

def list_reservations():
    szalloda.listaz_foglalasok()

def load_initial_data():
    szalloda.szoba_hozzaadasa(101, "Egyágyas", 10000)
    szalloda.szoba_hozzaadasa(102, "Egyágyas", 12000)
    szalloda.szoba_hozzaadasa(103, "Egyágyas", 13000)
    szalloda.szoba_hozzaadasa(201, "Kétágyas", 15000)
    szalloda.szoba_hozzaadasa(202, "Kétágyas", 18000)

    # Példa foglalások
    szalloda.foglalas(101, datetime.datetime(2024, 5, 1))
    szalloda.foglalas(101, datetime.datetime(2024, 5, 2))
    szalloda.foglalas(102, datetime.datetime(2024, 5, 3))
    szalloda.foglalas(103, datetime.datetime(2024, 5, 4))
    szalloda.foglalas(201, datetime.datetime(2024, 5, 5))

szalloda = Szalloda("Sam Szálloda")

root = tk.Tk()
root.title(f"{szalloda.nev} - Foglalás")
root.geometry("300x200")

tk.Label(root, text="Szobaszám:").pack()
szoba_entry = tk.Entry(root)
szoba_entry.pack()

tk.Label(root, text="Dátum (ÉÉÉÉ-HH-NN):").pack()
datum_entry = tk.Entry(root)
datum_entry.pack()

tk.Button(root, text="Foglalás", command=make_reservation).pack()
tk.Button(root, text="Lemondás", command=cancel_reservation).pack()
tk.Button(root, text="Foglalások listázása", command=list_reservations).pack()

load_initial_data()

root.mainloop()
