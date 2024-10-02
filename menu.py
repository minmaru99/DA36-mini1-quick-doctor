class Menu:

    def __init__(self):
        pass

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
                        pass
                    case '2':
                        pass
                    case _:
                        print('다시 선택해주세요.')