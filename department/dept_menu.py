from dept_service import DeptService

class DeptMenu():
    """
    아는거: service
    하는거: 메뉴 제공(메인, 서비메뉴), 입력폼 제공, 결과출력
    """
    def __init__(self):
        self.dept_service = DeptService()

    def dept_menu(self):
        print('진료 과목을 선택해주세요')
        dept_menu_str = """
        ------ 진료과목 ------
        1. 내과(IM)
        2. 이빈후과(ENT)
        3. 소아과(PD)
        0. 메인메뉴로 돌아가기
        ------------------------
        입력 : """

        while True:
            dept_choice = input(dept_menu_str)

            match dept_choice:
                case '1':
                    im_doc_str = """
                    =======내과 담당의=======
                    1. 김내과
                    2. 이내과
                    =======================
                    """
                    doc_choice=input('내과 담당의를 선택하세요: ')
                    if  doc_choice == '1':
                        # self.dept_service.save_reservation()
                        pass
                        print(dept_choice,doc_choice)

                    elif doc_choice == 2:
                        self.dept_service.save_reservation()

                    else:
                        print('다시 입력하세요')

                case '2':
                    ent_doc_str = """
                    ======이빈후과 담당의====
                    1. 정이비
                    2. 최후과
                    ======================
                    """
                    input('이빈후과 담당의를 선택하세요: ')

if __name__ == '__main__':
    d=DeptMenu()
    d.dept_menu()