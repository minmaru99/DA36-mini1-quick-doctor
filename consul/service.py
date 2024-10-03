import consul
from consul.repository import Repository
from datetime import datetime

class Service:

    reservation_date = {}

    def __init__(self):
        self.repository = Repository()

    def reservation_num(self):
        today = datetime.now().strftime("%y%m%d")
        if today in Service.reservation_date:
            Service.reservation_date[today] += 1
        else:
            Service.reservation_date[today] = 1
        reservation_num = f'{today}0{Service.reservation_date[today]}'
        return reservation_num

    def consul_info(self, name, social_num, phone, dept, doc):
        return self.repository.consul_info(name, social_num, phone, dept, doc)