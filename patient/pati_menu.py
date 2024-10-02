from patient.pati_entity import Patient
from patient.pati_repo import PatiRepo
from department.dept_entity import DeptEntity
from department.dept_menu import DeptMenu

class PatiMenu():
    def __init__(self):
        self.pati_repo=PatiRepo()

    def register_patient_info(self):
        pati_name=input('환자의 이름을 입력해주세요: ')
        while True:
            birth_num = input('환자의 주민번호를 입력해주세요: ')
            if len(birth_num)==13 and birth_num.isdigit():
                break
            else:
                print('올바른 주민번호를 입력해주세요: ')
        # birth_num=input('환자의 주민번호를 입력해주세요: ')
        pati_phone=input('환자의 전화번호를 입력해주세요: ')

        patient=Patient(pati_name,birth_num,pati_phone)
        # dept =
        # doct =
        # patient.select_dept_doct(dept,doct)
        patient.assign_reservation_num()
        self.pati_repo.update_patient_info(patient)
"""희애"""
"""""""""

""""혜영""""
"""""""""""