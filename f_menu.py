from patient.min_pati_menu import PatiMenu
from patient.pati_entity import Patient
from patient.pati_repo import PatiRepo
from department.dept_entity import Dept
from department.dept_menu import DeptMenu

class Kiosk():
    def __init__(self):
        self.dept_menu = DeptMenu()
        self.pati_menu = PatiMenu()
        patient_register = PatiMenu()
        patient_register.register_patient_info()

    def display_kiosk(self):
        menu_str = """
        ====== 접수/수납 키오스크 ======
        1. 접수
        2. 수납
        3. 종료
        ======================
        입력: """

        while True:
            choice = input(menu_str)

            match choice:
                case '1':
                    pati = self.input_pati()
                    pati_re = self.pati_service.create_pati(pati)
                    self.print_pati_re(pati_re)
                    self.DeptMenu.print_menu1()
                case '2':
                    pass
                case '3':
                    return

    def input_pati(self):
        print('> 본인 정보를 입력하세요.')
        pati_name = input('> 이름 입력 : ')
        pati_birth_num = input('> 주민번호 입력 :')
        pati_phone = input('> 부서입력')

        pati = Patient(pati_name, pati_birth_num, pati_phone)
        return pati

    def print_pati_re(self,pati_name, pati_birth_num, pati_phone):
        print(pati_name)

        if len(pati_birth_num) == 13 and pati_birth_num.isdigit():
            return
        else:
            print('주민번호가 올바르지 않습니다.')
        print(pati_phone)