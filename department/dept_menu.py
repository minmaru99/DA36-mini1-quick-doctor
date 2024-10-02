from conda.deprecations import deprecated

from department.dept_entity import Dept
from department.dept_repo import DeptRepo
from department.dept_service import DeptService


class DeptMenu:
    def __init__(self):
        self.dept_service = DeptService()
        self.selected_dept_name = None
        self.selected_dept_doct_name = None
        self.selected_price = None

    def print_menu1(self):
        print("------ 진료과목 선택 ------")
        for i, key in enumerate(DeptRepo.department_dict.keys()):
            print(f'{i + 1}. {key}')
        print(f'{0}. 뒤로가기')
        print("------------------------")
        print("입력 : ")

        while True:
            # self.print_menu1()
            choice = input()
            match choice:
                case '1':
                    self.selected_dept_name = '내과'
                    self.selected_price = '5000'
                    self.in_doct()
                case '2':
                    self.selected_dept_name = '이비인후과'
                    self.selected_price = '10000'
                    self.ot_doct()
                case '3':
                    self.selected_dept_name = '소아과'
                    self.selected_price = '20000'
                    self.pd_doct()
                case '0':
                    return
                case _:
                    print('다시 선택해주세요.')

            print(self.selected_dept_name)
            print(self.selected_dept_doct_name)
            print(int(self.selected_price))


    def print_sub_menu(self, key):
        print(f"------ {key} 담당의 선택 ------")
        dept = DeptRepo.department_dict[key]
        for i, doc_name in enumerate(dept.doct_names):
            print(f'{i + 1}. {doc_name}')
        print(f'{0}. 뒤로가기')
        print("------------------------")
        print("입력 : ")

    def in_doct(self):
        self.print_sub_menu('내과')
        choice = input()
        match choice:
            case '1':
                # print(choice)
                self.selected_dept_doct_name = DeptRepo.department_dict['내과'].doct_names[0]
            case '2':
                self.selected_dept_doct_name = DeptRepo.department_dict['내과'].doct_names[1]
            case _:
                print('다시 선택해주세요.')

    def ot_doct(self):
        self.print_sub_menu('이비인후과')
        choice = input()
        match choice:
            case '1':
                self.selected_dept_doct_name = DeptRepo.department_dict['이비인후과'].doct_names[0]
            case '2':
                self.selected_dept_doct_name = DeptRepo.department_dict['이비인후과'].doct_names[1]

    def pd_doct(self):
        self.print_sub_menu('소아과')
        choice = input()
        match choice:
            case '1':
                self.selected_dept_doct_name = DeptRepo.department_dict['소아과'].doct_names[0]
            case '2':
                self.selected_dept_doct_name = DeptRepo.department_dict['소아과'].doct_names[1]








