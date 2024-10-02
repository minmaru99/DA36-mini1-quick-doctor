class Pati():
    next_id = 1  # 클래스 변수 id(공용)

    def __init__(self, pati_name, pati_phone, birth_num):
        self.__id = Pati.next_id  # 클래스변수 id로부터 채번
        self.__pati_name = pati_name
        self.__pati_phone = pati_phone
        self.__birth_num = birth_num

        Pati.next_id += 1
