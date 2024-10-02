from patient.pati_menu import *
from department.dept_menu import *



class Menu:

    def __init__(self):
        self.main_menu()
        self.patient_menu=PatiMenu() # patient_menu는 PatiMenu class안에 있는 모든 attr나 method에 접근 가능
        self.dept_menu=DeptMenu()

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
                    self.patient_menu.register_patient_info() #patient_menu가 class PatiMenu안에 있는 register함수를 부름
                case '2':
                    pass
                case _:
                    print('다시 선택해주세요.')

"""희애"""
"""""""""

""""혜영""""
"""""""""""

if __name__ == '__main__':
    m=Menu()
    m.main_menu()