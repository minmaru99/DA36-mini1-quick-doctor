from datetime import datetime
class Patient():
    reservation_date={}
    def __init__(self, pati_name, birth_num, pati_phone):
        self.name=pati_name
        self.birth_num = birth_num
        self.phone=pati_phone
        self.dept=None
        self.doct=None
        self.reservation_num=None

    def select_dept_doct(self,dept, doct):
        self.dept=dept
        self.doct=doct

    def assign_reservation_num(self):
        today = datetime.today().strftime('%y%m%d')
        if today in Patient.reservation_date:
            Patient.reservation_date[today]+=1
        else:
            Patient.reservation_date[today]=1
        self.reservation_num = f'{today}0{Patient.reservation_date[today]}'

    def pati_info(self):
        return {
            'pati_name':self.name,
            'birth_num':self.birth_num,
            'pati_phone':self.phone,
            'dept':self.dept,
            'doct':self.doct,
            'reservation_num':self.reservation_num
        }