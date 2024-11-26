import tkinter as tk
from tkinter import messagebox

class ReservationView:
    def __init__(self, root):
        tk.Label(root, text="Nombre:").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(root, text="Fecha (YYYY-MM-DD):").grid(row=1, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=1, column=1)

        tk.Label(root, text="Hora (HH:MM):").grid(row=2, column=0)
        self.time_entry = tk.Entry(root)
        self.time_entry.grid(row=2, column=1)

        self.submit_button = tk.Button(root, text="Añadir Reserva")
        self.submit_button.grid(row=3, columnspan=2)

    def set_submit_callback(self, callback):
        self.submit_button.config(command=lambda: callback(
            self.name_entry.get(),
            self.date_entry.get(),
            self.time_entry.get()
        ))

    def display_message(self, message):
        messagebox.showinfo("Información", message)
