import tkinter as tk
from tkinter import messagebox
import datetime

class HotelBookingSystem:
    def __init__(self):
        self.rooms = {101: "szabad", 102: "szabad", 103: "szabad"}  # 3 szoba
        self.bookings = {}

    def make_reservation(self, room_number, date):
        if room_number not in self.rooms:
            messagebox.showerror("Hiba", "Hibás szobaszám.")
            return False
        if self.rooms[room_number] != "szabad":
            messagebox.showerror("Hiba", "A szoba foglalt.")
            return False
        if date <= datetime.datetime.now():
            messagebox.showerror("Hiba", "Csak jövőbeni foglalás lehetséges.")
            return False
        self.rooms[room_number] = "foglalt"
        self.bookings[(room_number, date)] = "foglalva"
        messagebox.showinfo("Siker", "Foglalás sikeres!")
        return True

    def cancel_reservation(self, room_number, date):
        if (room_number, date) not in self.bookings:
            messagebox.showerror("Hiba", "Nincs ilyen foglalás.")
            return False
        del self.bookings[(room_number, date)]
        self.rooms[room_number] = "szabad"
        messagebox.showinfo("Siker", "Lemondás sikeres!")
        return True

    def list_bookings(self):
        if not self.bookings:
            messagebox.showinfo("Információ", "Nincsenek foglalások.")
            return
        bookings_info = "Foglalások:\n"
        for (room_number, date) in self.bookings.keys():
            bookings_info += f"Szoba: {room_number}, Dátum: {date}\n"
        messagebox.showinfo("Foglalások", bookings_info)

def load_initial_data(system):
    # 1 szálloda, 3 szoba, 5 foglalás
    for room_num in range(101, 104):
        system.rooms[room_num] = "szabad"
    system.bookings = {
        (101, datetime.datetime(2024, 5, 1)): "foglalva",
        (101, datetime.datetime(2024, 5, 3)): "foglalva",
        (102, datetime.datetime(2024, 5, 2)): "foglalva",
        (102, datetime.datetime(2024, 5, 4)): "foglalva",
        (103, datetime.datetime(2024, 5, 5)): "foglalva",
    }

def make_reservation_window():
    reservation_window = tk.Toplevel()
    reservation_window.title("Foglalás")
    reservation_window.geometry("400x350")
    tk.Label(reservation_window, text="Szobaszám:").pack()
    room_number_entry = tk.Entry(reservation_window)
    room_number_entry.pack()
    tk.Label(reservation_window, text="Dátum (ÉÉÉÉ-HH-NN):").pack()
    date_entry = tk.Entry(reservation_window)
    date_entry.pack()

    def make_reservation():
        room_num = int(room_number_entry.get())
        date_str = date_entry.get()
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Hiba", "Hibás dátum formátum.")
            return
        hotel_system.make_reservation(room_num, date)
        reservation_window.destroy()

    tk.Button(reservation_window, text="Foglalás", command=make_reservation).pack()

def cancel_reservation_window():
    cancel_window = tk.Toplevel()
    cancel_window.title("Lemondás")
    cancel_window.geometry("400x350")
    tk.Label(cancel_window, text="Szobaszám:").pack()
    room_number_entry = tk.Entry(cancel_window)
    room_number_entry.pack()
    tk.Label(cancel_window, text="Dátum (ÉÉÉÉ-HH-NN):").pack()
    date_entry = tk.Entry(cancel_window)
    date_entry.pack()

    def cancel_reservation():
        room_num = int(room_number_entry.get())
        date_str = date_entry.get()
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Hiba", "Hibás dátum formátum.")
            return
        hotel_system.cancel_reservation(room_num, date)
        cancel_window.destroy()

    tk.Button(cancel_window, text="Lemondás", command=cancel_reservation).pack()

def main():
    global hotel_system
    hotel_system = HotelBookingSystem()
    load_initial_data(hotel_system)

    root = tk.Tk()
    root.title("Szállodai foglalás")
    root.geometry("400x350")

    tk.Button(root, text="Foglalás", command=make_reservation_window).pack()
    tk.Button(root, text="Lemondás", command=cancel_reservation_window).pack()
    tk.Button(root, text="Foglalások listázása", command=hotel_system.list_bookings).pack()
    tk.Button(root, text="Kilépés", command=root.quit).pack()

    root.mainloop()

if __name__ == "__main__":
    main()
