class ReservationModel:
    def __init__(self):
        self.reservations = []  # Lista para almacenar las reservas

    def add_reservation(self, name, date, time):
        new_reservation = {"name": name, "date": date, "time": time}
        self.reservations.append(new_reservation)
        return True
