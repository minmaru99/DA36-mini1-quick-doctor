from department.dept_repo import DeptRepo

class DeptService():
    def __init__(self):
        self.dept_repo = DeptRepo()


    def load_dept_doct_list(self):
        return self.dept_repo.load_dept_doct_list()




