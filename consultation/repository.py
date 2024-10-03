class PatiRepo:
    def __init__(self):
        self.patients = {}

    def add_patient(self, patient):
        patient = self.patients[patient.reservation_number]

    def get_patient_by_reservation(self, reservation_number):
        return self.patients.get(reservation_number, None)
