from consultation.repository import *
from consultation.entity import *
from consultation.service import *


class Menu:
    def __init__(self):
        pass

    def main_menu(self):
        menu_str = """
    ====== 접수/수납 키오스크 ======
    1. 진료예약 조회
    2. 진료예약 등록
    3. 수납
    3. 종료
    =============================
    입력: """
        while True:
            choice = input(menu_str)

            if choice == '1':
                reservation_number = input("예약번호를 입력하세요: ")
                PatiService.find_patient_by_reservation(reservation_number)

            elif choice == '2':
                # 환자 정보 입력
                name = input("이름을 입력하세요: ")
                age = input("나이를 입력하세요: " "")
                while True:
                    phone_number = input("전화번호를 입력하세요(11자리): ")
                    if len(phone_number) == 11 and phone_number.isdigit():
                        break
                    else:
                        print('❌잘못된 전화번호입니다. 11자리 숫자를 다시 입력해주세요❌')

                while True:
                    social_number = input("주민번호를 입력하세요(13자리): ")
                    if len(social_number) == 13 and social_number.isdigit():
                        break
                    else:
                        print('❌잘못된 주민번호입니다. 13자리 숫자를 다시 입력해주세요')

                # 진료과목 선택
                depts = ["내과", "소아과","이빈후과"]
                depts_str = "\n".join([f'{i+1}.{dept}' for i, dept in enumerate(depts)])
                dept_choice = int(input(f'==진료과목을 선택하세요== \n{depts_str}\n선택: ')) -1
                dept = depts[dept_choice]

                # 담당의사 선택
                docs = {
                    "내과" : ["김내과","이내과"],
                    "이빈후과" : ["최이빈", "박후과"],
                    "소아과" : ["문소아", "한소아"]
                }
                docs_str = "\n".join([f'{i+1}.{doc}' for i, doc in enumerate(docs[dept])])
                doc_choice = int(input(f'담당의사를 선택해주세요: \n{docs_str}\n선택:')) -1
                doc = docs[dept][doc_choice]

                # 예약번호 생성 및 환자 등록
                PatiService.create_reservation_num(reservation_number)

            elif choice == '3':
                fee =(5000, 10000, 20000)

                reservation_number  = input("예약번호를 입력하세요: ")
                patient = PatiRepo.get_patient_by_reservation(reservation_number)
                if patient == reservation_number:
                    print(fee[dept_choice])
                    PatiService.payment_process(patient) # TODO 수납 추가+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                else:
                    print(f'예약번호 {reservation_number}로 등록된 정보를 찾을 수 없습니다')

            elif choice == '4':
                print("프로그램을 종료합니다.")
                return

            else:
                print('❌잘못 입력하셨습니다. 다시 입력해주세요!❌')