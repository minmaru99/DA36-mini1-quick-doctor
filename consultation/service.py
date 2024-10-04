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
            print(f'(⊙_⊙)？ 예약번호 \'{reservation_number}\'로 등록된 정보를 찾을 수 없습니다.')
            print('다시 확인 후 이용해주세요 🙏🏻')

    count_date = {}
    def create_reservation_num(self):
        today = datetime.today().strftime('%y%m%d')  # 오늘 날짜 YYMMDD 형식
        max_num = 0  # 오늘 날짜의 최대 예약번호를 저장할 변수
        # 환자 목록에서 오늘 날짜에 해당하는 예약번호를 찾음
        for patient in self.repository.patients:
            if patient[0].startswith(today):  # 예약번호가 오늘 날짜로 시작하면
                current_num = int(patient[0][-3:])  # 예약번호의 마지막 3자리 숫자 추출
                if current_num > max_num:
                    max_num = current_num
        # 새로운 예약번호 생성
        new_reservation_num = f"{today}{str(max_num + 1).zfill(3)}"
        return new_reservation_num

        # if today in self.count_date:
        #     self.count_date[today] += 1
        # else:
        #     self.count_date[today] = 1
        # # 3자리로 고정된 번호를 만들어 반환 (001, 002, 003...)
        # return f'{today}{str(self.count_date[today]).zfill(3)}'
        # # unique_id = str(len(self.repository.patients)+1).zfill(2)
        # # return f'{today}0{unique_id}'


    def add_new_patient(self, patient_info):
        self.repository.add_new_patient(patient_info)


    def display_patient_info(self, patient_info):
       print("==== 접수 내역 =====:")
       print(f'이름: {patient_info[1]}')
       # print(f'예약번호: {patient_info[0]}')
       print(f'날짜: 20{patient_info[0][:2]}/{patient_info[0][2:4]}/{patient_info[0][4:6]}')
       print(f'전화번호: {patient_info[2][:3]}-{patient_info[2][3:7]}-{patient_info[2][7:]}')
       print(f'주민번호: {patient_info[3][:7]}-{patient_info[3][7:]}')
       print(f'진료과목: {patient_info[4]}')
       print(f'담당의사: {patient_info[5]}')


    def payment_process(self,reservation_number):
        patient = self.repository.get_patient_by_reservation(reservation_number)
        if patient:
            dept_fee = self.repository.get_dept_fee(patient[4])
            return dept_fee
        else:
            print(f'(⊙_⊙)？ 예약번호 \'{reservation_number}\'로 등록된 정보를 찾을 수 없습니다.')
            print('다시 확인 후 이용해주세요 🙏🏻')


if __name__ == '__main__':
    service = PatiService()