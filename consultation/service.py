from datetime import datetime
from consultation.repository import *
from consultation.entity import *



class PatiService:
    def __init__(self):
        self.repository = PatiRepo()


    def find_patient_by_reservation(self, reservation_number):
        patient = self.repository.get_patient_by_reservation(reservation_number)
        if patient:
            self.display_patient_info(patient)
        else:
            print(f'예약번호 {reservation_number}로 등록된 정보를 찾을 수 없습니다.')


    def create_reservation_num(self):
        # today = datetime.now().strftime("%y%m%d")
        # if today in PatiService.reservation_date:
        #     PatiService.reservation_date[today] += 1
        # else:
        #     PatiService.reservation_date[today] = 1
        #     reservation_number = f'{today}0{PatiService.reservation_date[today]}'
        # return reservation_number

        today = datetime.today().strftime('%Y%m%d')
        unique_id = str(len(self.repository.patients)+1).zfill(2)
        return f'{today}0{unique_id}'

    def add_new_patient(self, name, age, phone_number, social_number, dept, doc):
        reservation_number = self.create_reservation_num()
        new_patient = Patient(reservation_number, name, age, phone_number, social_number, dept, doc)
        self.repository.add_patient(new_patient)
        print(f'예약이 완료되었습니다!   💡예약번호: {reservation_number}💡')

    def display_patient_info(self, patient):
       print("==== 예약 정보=====:")
       print(f'예약번호: {patient.reservation_number}')
       print(f'이름: {patient.name}')
       print(f'나이: {patient.age}')
       print(f'전화번호: {patient.phone_number}')
       print(f'주민번호: {patient.social_number}')
       print(f'진료과목: {patient.dept}')
       print(f'담당의: {patient.doc}')

    def payment_process(self,reservation_number):
        patient = self.repository.get_patient_by_reservation(reservation_number)
        if patient:
            dept_fee = self.repository.get_dept_fee(patient.dept)
            return dept_fee





