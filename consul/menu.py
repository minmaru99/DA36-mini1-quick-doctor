from consul.service import Service
from consultation.repository import *
from consultation.entity import *
from consultation.service import *

class Menu:
    def __init__(self):
        self.service = Service()

    def main_menu(self):
        menu_str = """
        ====== 접수/수납 키오스크 ======
        1. 진료예약 
        2. 수납
        3. 종료
        =============================
        입력: """

        while True:
            choice = input(menu_str)

            match choice:
                case '1':
                    # 환자정보입력
                    name = input("이름을 입력하세요 : ")
                    age = input("나이를 입력하세요 : ")
                    while True:
                        social_num = input("주민번호 13자리를 입력하세요.")
                        if len(social_num) == 13 and social_num.isdigit():
                            break
                        else:
                            print("❌잘못된 주민번호입니다. 13자리 숫자를 다시 입력해주세요❌")
                    while True:
                        phone = input("전화번호 11자리를 입력하세요 :")
                        if len(phone) == 11 and phone.isdigit():
                            break
                        else:
                            print("❌잘못된 전화번호입니다. 11자리 숫자를 다시 입력해주세요❌")

                    # 진료과목 선택
                    depts = ["내과", "소아과", "이빈후과"]
                    depts_str = "\n".join([f'{i + 1}.{dept}' for i, dept in enumerate(depts)])
                    dept_choice = int(input(f'==진료과목을 선택하세요== \n{depts_str}\n선택: ')) - 1
                    dept = depts[dept_choice]

                    #담당의사 선택
                    docs = {
                        "내과": ["김내과", "이내과"],
                        "이비인후과": ["최이빈", "박후과"],
                        "소아과": ["문소아", "한소아"]
                    }
                    docs_str = "\n".join([f'{i + 1}.{doc}' for i, doc in enumerate(docs[dept])])
                    doc_choice = int(input(f'담당의사를 선택해주세요: \n{docs_str}\n선택:')) - 1
                    doc = docs[dept][doc_choice]

                    print(name, social_num, phone, dept, doc)
                    f_consul_info = self.service.consul_info(name, social_num, phone, dept, doc)
                    f_reservation_num = (self.service.reservation_num())

                    print(f_consul_info, f_reservation_num)




