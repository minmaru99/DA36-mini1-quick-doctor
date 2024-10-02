from department.dept_repo import DeptRepo

class DeptService():
    """
    아는거: repo
    하는거: 진료내용 저장(save_reservation),
    """
    def __init__(self):
        self.dept_repo = DeptRepo()

    def save_reservation(self, reservation):
        return self.dept_repo.save_reservation()






