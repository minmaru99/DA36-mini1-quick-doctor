from consultation.entity import Patient

class PatiRepo:
    dept_fees = {
        "내과": 10000,
        "이빈후과": 20000,
        "소아과": 30000
    }

    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_patient_by_reservation(self, reservation_number):
        for patient in self.patients:
            if patient.reservation_number == reservation_number:
                return patient
        return None

    def get_dept_fee(self, dept):
        return self.dept_fees.get(dept, 0)
