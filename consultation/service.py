from datetime import datetime
from repository import *
from entity import *



class PatiService:
    reservation_date = {}
    def __init__(self, repository):
        self.repository = repository

    def create_reservation_num(self):
        today = datetime.datetime.now().strftime("%y%m%d")
        if today in PatiService.reservation_date:
            PatiService.reservation_date[today] += 1
        else:
            PatiService.reservation_date[today] = 1
        self.reservation_number = f'{today}0{PatiService.reservation_date[today]}'
        return self.reservation_number

    def add_new_patient(self,name, age, phone_number, social_number, dept, doc):
        reservation_number = self.create_reservation_num()
        new_patient = Patient(reservation_number, name, age, phone_number, social_number, dept, doc)
        self.repository.add_new_patient(new_patient)
        print(f'예약이 완료되었습니다! 예약번호: {reservation_number}')
        return reservation_number

    def find_patient_by_reservation(self, reservation_number):
        patient = self.repository.get_patient_by_reservation(reservation_number)
        if patient:
            self.display_patient_info(patient)
        else:
            print(f'예약번호 {reservation_number}로 등록된 정보를 찾을 수 없습니다.')

    def display_patient_info(self, patient):
       print("==== 예약 정보=====:")
       print(f'예약번호: {patient.reservation_number}')
       print(f'이름:{patient.name}')
       print(f'나이:{patient.age}')
       print(f'주민번호: {patient.social_num}')
       print(f'전화번호: {patient.phone}')
       print(f'진료과목" {patient.dept}')
       print(f'담당의" {patient.doc}')

    def payment_process(self,patient):
        pass
