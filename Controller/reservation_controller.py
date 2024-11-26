class ReservationController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_submit_callback(self.add_reservation)

    def add_reservation(self, name, date, time):
        if not name or not date or not time:
            self.view.display_message("Todos los campos son obligatorios.")
            return

        success = self.model.add_reservation(name, date, time)
        if success:
            self.view.display_message("Reserva añadida con éxito.")
        else:
            self.view.display_message("Error al añadir la reserva.")

