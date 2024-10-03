from department.dept_repo import DeptRepo

class DeptService():
    def __init__(self):
        self.dept_repo = DeptRepo()




    def save_rev(self):
        return self.dept_repo.save_rev()




