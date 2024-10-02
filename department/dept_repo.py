import pickle
from department.dept_entity import Dept

class DeptRepo():
    def __init__(self):
        pass

    def load_dept_doct_list(self):
        dept_doct_dict = {}
        file_path="C:/Workspaces/DA36-mini1-quick-doctor/department/dept_doct_list.txt"
        with open(file_path, 'r', encoding='utf8') as f:
            for line in f :
                key, value = line.strip().split('=')
                dept_doct_dict[key] = value
        return dept_doct_dict

    def save_rev(self):
        reservation = []



# 클래스 인스턴스 생성
repo = DeptRepo()

file_path = 'dept_doct_list.txt'
dept_doct_dict = repo.load_dept_doct_list()

dd_dept = list(dept_doct_dict.keys())






# def load_dept_doct_list(file_path) :