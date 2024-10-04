from consultation.service import *
from consultation.admin_menu import admin_menu


class Menu:
    def __init__(self):
        self.service = PatiService()

    def main_menu(self):
        menu_str = """
    ====== 접수/수납 키오스크 ======
    1. 신규 접수
    2. 접수 내역 조회
    3. 수납
    4. 종료

    ⚙️ 관리자 모드 ⚙️
    =============================
    입력: """
        while True:
            choice = input(menu_str)

            if choice == '1':
                # 환자 정보 입력
                name = input("(1) 이름을 입력하세요: ")

                while True:
                    phone_number = input("(2) 전화번호를 입력하세요(숫자만): ")
                    if len(phone_number) == 11 and phone_number.isdigit():
                        break
                    else:
                        print('❌잘못된 전화번호입니다. 11자리 숫자를 다시 입력해주세요❌')

                while True:
                    social_number = input("(3) 주민번호를 입력하세요(숫자만): ")
                    if len(social_number) == 13 and social_number.isdigit():
                        break
                    else:
                        print('❌잘못된 주민번호입니다. 13자리 숫자를 다시 입력해주세요')

                # 진료과목 선택
                depts = ["내과", "소아과", "이비인후과"]
                depts_str = "\n".join([f'{i + 1}.{dept}' for i, dept in enumerate(depts)])
                dept_choice = int(input(f'(4) 진료과목을 선택하세요 \n{depts_str}\n- 선택: ')) - 1
                dept = depts[dept_choice]

                # 담당의사 선택
                docs = {
                    "내과": ["이마크", "이해찬"],
                    "이비인후과": ["정재현", "황런쥔"],
                    "소아과": ["김정우", "나재민"]
                }
                docs_str = "\n".join([f'{i + 1}.{doc}' for i, doc in enumerate(docs[dept])])
                doc_choice = int(input(f'(5) 담당의사를 선택해주세요: \n{docs_str}\n- 선택:')) - 1
                doc = docs[dept][doc_choice]

                # 예약번호 생성 및 환자 등록
                reservation_number = self.service.create_reservation_num()
                patient_info = [reservation_number, name, phone_number, social_number, dept, doc]
                self.service.add_new_patient(patient_info)
                print(f'\n예약이 완료되었습니다! \'{name}\'님의 예약번호: 💡{reservation_number}💡')
                print('예상 대기 시간은 10분입니다. 감사합니당 💙')

            elif choice == '2':
                reservation_number = input("\n예약번호를 입력하세요: ")
                self.service.find_patient_by_reservation(reservation_number)  # 클래스가 아닌 위에 선언한 인스턴스 self.service로 불러와야 함

            elif choice == '3':
                reservation_number = input("예약번호를 입력하세요: ")
                dept_fee = self.service.payment_process(reservation_number)
                if dept_fee:
                    print(f'\n💰 결제 금액은 \'{dept_fee}원\' 입니다 💰')

                    while True:
                        print('< 결제 수단을 선택하세요 >')
                        payment_method = input('1.💳 카드 \n2.💸 현금 \n- 선택: ')
                        if payment_method == '1':
                            print('💳 카드 결제가 완료되었습니다. $_$')
                            break
                        elif payment_method == '2':
                            print('💸 현금 결제가 완료되었습니다. $_$')
                            break
                        else:
                            print('❌ 잘못 입력하셨습니다. 다시 선택해주세요. ❌')

                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n수납을 모두 마쳤습니다.')
                    print('처방전은 안내데스크에서 받아가실 수 있습니다.🧾')

            elif choice == '*':
                chance = 0  # 시도할 수 있는 기회는 3번
                while chance < 3:
                    password = int(input('🔒 관리자 모드를 이용하시려면 비밀번호를 입력해주세요: '))
                    if password == 247:
                        print('🔓 관리자 모드로 전환합니다.')
                        admin_menu()
                        break
                    else:
                        chance += 1
                        if chance < 3:
                            print(f'💦 비밀번호가 틀렸습니다. 다시 시도해주세요. 남은 기회: {3 - chance}번!')
                        else:
                            print('비밀번호를 3번 틀리셨습니다.💢 처음 화면으로 돌아갑니다 ╰（‵□′）╯')
                            break


            elif choice == '4':
                print("\n키오스크를 종료합니다.\n이용해주셔서 감사합니다. (●'◡'●)")
                return








