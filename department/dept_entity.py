
class DeptEntity():

    class Doctor:
        def __init__(self, doctor_name, dept):
            self.doctor_name = doctor_name
            self.dept = dept

    class Reservation:
        def __init__(self, dept, doctor_name, reservation_date):
            self.dept = dept
            self.doctor_name = doctor_name
            self.reservation_date = reservation_date

