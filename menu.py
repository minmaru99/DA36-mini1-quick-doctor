class Menu:

    def __init__(self):
        self.dept_menu = DeptMenu()
        self.pati_menu = PatiMenu()

    def main_menu(self):
        menu_str = """
        ------ 접수/수납 키오스크 ------
        1. 접수
        2. 수납
        ------------------------
        입력 : """

            while True:
                choice = input(menu_str)

                match choice:
                    case '1':
                        pati_name, pati_ssn = self.pati_menu.register_patient_info()
                        dept_name, dept_doct_name = self.dept_menu.dept_menu()
                        print('진료를 시작합니다......')
                        print('수납해주세요....')
                    case '2':
                        pass
                    case _:
                        print('다시 선택해주세요.')

"""희애"""
"""""""""

""""혜영""""
"""""""""""