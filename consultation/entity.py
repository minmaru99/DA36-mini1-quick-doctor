class Patient:
    dept_fees = {
        "내과": 10000,
        "이비인후과": 20000,
        "소아과": 30000
    }
    def __init__(self, reservation_number, name,  phone_number, social_number, dept, doc):
        self.reservation_number = reservation_number
        self.name = name
        self.phone_number = phone_number
        self.social_number = social_number
        self.dept = dept
        self.doc = doc

#TODO 에외처리
"""
전화번호, 주민번호 int로 변환
진료과목, 의사 다른숫자 선택하해도 넘어감

진료내역 이름/나이/번호 불러오는 순서 이상함
결제 금액 보여줄 때, 진료내역 함께 보여주기
"""
