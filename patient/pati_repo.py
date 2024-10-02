from patient.pati_entity import Patient

class PatiRepo:
    def __init__(self):
        self.patients_info=[]

    def update_patient_info(self,patient):
        self.patients_info.append(patient)

    def find_patient_info(self,reservation_num):
        for patient in self.patients_info:
            if patient.reservation_num == reservation_num:
                return patient.pati_info()

        print('조회된 환자의 정보가 없습니다. 예약번호를 다시 확인해주세요.')

    def get_all_patient_info(self):
        return self.patients_info

"""희애"""
"""""""""

""""혜영""""
"""""""""""