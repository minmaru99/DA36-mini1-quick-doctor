from patient.pati_menu import PatiMenu

class Menu:

    def __init__(self):
        self.pati_menu=PatiMenu()

    def main_menu(self):
        menu_str = """
        ------ 접수/수납 ------
        1. 접수하기 🩺
        2. 수납하기 💸
        ------------------------
        입력 : """

            while True:
                choice = input(menu_str)

                match choice:
                    case '1':
                        self.pati_menu.register_patient_info()
                    case '2':
                        pass
                    case _:
                        print('다시 선택해주세요.')

"""희애"""
"""""""""

""""혜영""""
"""""""""""