# from patient.pati_menu import PatiMenu
from department.dept_menu import DeptMenu


class Menu:

    def __init__(self):
        self.pati_menu = PatiMenu()
        self.dept_menu = DeptMenu()

    def main_menu(self):
        menu_str = """
        ------ 접수/수납 키오스크 ------
        1. 접수
        2. 수납
        3. 진료내역 확인하기
        -----------------------------
        입력 : """

        while True:
            choice = input(menu_str)

            match choice:
                case '1':
                    pass # 환자정보 메뉴 나오기(진료 예약하기)

                case '2':
                    pass # 수납하기

                case '3':
                    pass

                case _:
                    print('다시 선택해주세요.')

