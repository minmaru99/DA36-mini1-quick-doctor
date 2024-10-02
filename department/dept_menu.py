from conda.deprecations import deprecated

from department.dept_entity import Dept
from department.dept_repo import DeptRepo, dept_doct_dict
from department.dept_service import DeptService


class DeptMenu():
    def __init__(self):
        self.dept_service =DeptService()

    def dept_menu(self):
        menu_str = """
------ 진료과목 선택 ------
1. 내과
2. 이비인후과
3. 소아과
------------------------
입력 : """

        while True:
            dept_choice = input(menu_str)

            match dept_choice:
                case '1':
                    self.inter_doct_menu()
                    if dept_choice == '1' :
                        print(dept_doct_dict)
                case '2':
                    self.oto_doct_menu()
                case '3':
                    self.ped_doct_menu()
                case _:
                    print('다시 선택해주세요.')


    def inter_doct_menu(self):
        menu_str = """
    ====== 내과 담당의 =====
    1. 김내과
    2. 최내과
    =======================
    입력 : """
        choice = input(menu_str)
        match choice:
            case '1':
                pass
            case '2':
                pass
            case _:
                print('다시 선택해주세요.')

    def oto_doct_menu(self):
        menu_str = """
        ====== 내과 담당의 =====
        1. 김이비
        2. 박비인
        =======================
        입력 : """

        choice = input(menu_str)
        match choice:
            case '1':
                pass
            case '2':
                pass

    def ped_doct_menu(self):
        menu_str = """
        ====== 내과 담당의 =====
        1. 박소아
        2. 이소아
        =======================
        입력 : """

        choice = input(menu_str)
        match choice:
            case '1':
                pass
            case '2':
                pass







