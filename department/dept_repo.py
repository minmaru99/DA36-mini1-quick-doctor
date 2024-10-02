import pickle
from department.dept_entity import Dept

class DeptRepo():
    department_dict = {
        "내과": Dept('내과', ['김내과', '최내과'], '5000'),
        "이비인후과": Dept('이비인후과', ['김이빈', '박비인'], '10000'),
        "소아과": Dept('소아과',['박소아','이소아'], '20000')
    }










# def load_dept_doct_list(file_path) :