import pickle

from dept_entity import DeptEntity

class DeptRepo():
    """
    할 수 있는 것: 진료내용 저장(save_reservation), 진료내용 조회(find_reservation)
    """
    def __init__(self):
        self.reservation = {}

    def save_reservation(self,reservation):
        self.reservations.append(reservation)
        return 1



