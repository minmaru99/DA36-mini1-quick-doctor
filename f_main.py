# from patient.pati_entity import Patient
# from patient.pati_repo import PatiRepo
# from department.dept_entity import Dept
from department.dept_menu import DeptMenu
from patient.pati_menu import PatiMenu
from f_menu import Kiosk
if __name__ == '__main__':
    f_menu = Kiosk()
    Kiosk().display_kiosk()

    print('끝')