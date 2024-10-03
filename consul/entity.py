class Patient:
    def __init__(self, reservation_num, name, phone, social_num, dept, doc, fee=0):
        self.reservation_num = reservation_num
        self.name = name
        self.phone = phone
        self.social_num = social_num
        self.dept = dept
        self.doc = doc
        self.fee = fee # fee는 추가되지만 표시되지 않음
