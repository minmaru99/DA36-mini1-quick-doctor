from patient.pati_entity import Pati

class PatiMenu():
    def __init__(self):
        pass

    def input_pati(self):
        print('> 환자 정보를 입력해주세요')
        pati_name = input('> 이름 입력:')
        pati_phone = input('> 전화번호 입력:')
        birth_num = input('> 주민번호 입력:')

        pati_info = Pati(pati_name, pati_phone, birth_num)
        return pati_info