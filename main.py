from model.reservation_model import ReservationModel
from view.reservation_view import ReservationView
from controller.reservation_controller import ReservationController
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    model = ReservationModel()
    view = ReservationView(root)
    controller = ReservationController(model, view)
    root.mainloop()
