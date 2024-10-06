from consultation.service import *
from consultation.repository import *

class Menu:
    def __init__(self):
        self.service = PatiService()

    def main_menu(self):
        menu_str = """
    ====== 접수/수납 키오스크 ======
    1. 진료예약 등록
    2. 진료내역 조회
    3. 수납
    4. 종료
    =============================
    입력: """
        while True:
            choice = input(menu_str)

            if choice == '1':
                # 환자 정보 입력
                name = input("이름을 입력하세요: ")


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
                depts = ["내과", "소아과", "이빈후과"]
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
                reservation_number = self.service.create_reservation_num()
                patient_info=[reservation_number, name, phone_number, social_number,dept, doc]
                self.service.add_new_patient(patient_info)
                print(f'예약이 완료되었습니다! {name}님의 💡예약번호: {reservation_number}💡')


            elif choice == '2':
                reservation_number = input("예약번호를 입력하세요: ")
                self.service.find_patient_by_reservation(reservation_number)  # 클래스가 아닌 위에 선언한 인스턴스 self.service로 불러와야 함
            elif choice == '3':
                reservation_number  = input("예약번호를 입력하세요: ")
                dept_fee = self.service.payment_process(reservation_number)
                print(f'\n💰결제 금액은 {dept_fee}원 입니다.💰')

                while True:
                    payment_method = input('\n<결제 수단을 선택하세요.>\n 1.💳카드 2.💸현금: ')
                    if payment_method == '1':
                        print('💳 카드 결제가 완료되었습니다.')
                        break
                    elif payment_method == '2':
                        print('💸현금 결제가 완료되었습니다.')
                        break
                    else:
                        print('❌ 잘못 입력하셨습니다. 다시 선택해주세요. ❌')

                print('~~~~~~~~~~~~~~~~~\n🧾 결제가 완료되었습니다. 감사합니다!')

            elif choice == '4':
                print("프로그램을 종료합니다.")
                return









