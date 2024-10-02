# DeptMenu 클래스
class DeptMenu():
    def __init__(self):
        self.dept = None
        self.doct = None

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
                    self.dept = '내과'
                    self.inter_doct_menu()
                    break
                case '2':
                    self.dept = '이비인후과'
                    self.oto_doct_menu()
                    break
                case '3':
                    self.dept = '소아과'
                    self.ped_doct_menu()
                    break
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
                self.doct = '김내과'
            case '2':
                self.doct = '최내과'

    def oto_doct_menu(self):
        menu_str = """
    ====== 이비인후과 담당의 =====
    1. 김이비
    2. 박비인
    ======================= 
    입력 : """
        choice = input(menu_str)
        match choice:
            case '1':
                self.doct = '김이비'
            case '2':
                self.doct = '박비인'

    def ped_doct_menu(self):
        menu_str = """
    ====== 소아과 담당의 =====
    1. 박소아
    2. 이소아
    ======================= 
    입력 : """
        choice = input(menu_str)
        match choice:
            case '1':
                self.doct = '박소아'
            case '2':
                self.doct = '이소아'
