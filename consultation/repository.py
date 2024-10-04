from consultation.entity import Patient

class PatiRepo:
    dept_fees = {
        "내과": 10000,
        "이비인후과": 20000,
        "소아과": 30000
    }

    def __init__(self):
        self.patients = []
        try:
            with open(r'C:\Workspace\DA36-mini1-quick-doctor\consultation\patients.txt', 'r', encoding='utf-8') as f:
                content = f.readlines()
                for line in content:
                    line=line.strip().split(",")
                    self.patients.append(line)
        except FileNotFoundError:
            self.patients = []

    def add_new_patient(self, patient):
        self.patients.append(patient)
        with open('patients.txt', 'a', encoding='utf-8') as f:
            f.write(",".join(patient)+"\n")

    def get_patient_by_reservation(self, reservation_number):
        # print(self.patients)
        for patient in self.patients:
            if patient[0] == reservation_number:
                return patient

        return None

    def get_dept_fee(self, dept):
        return self.dept_fees.get(dept, 0)



if __name__ == '__main__':
    repo = PatiRepo()
