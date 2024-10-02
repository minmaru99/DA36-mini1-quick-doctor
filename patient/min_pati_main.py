from patient.pati_repo import PatiRepo
from patient.min_pati_menu import PatiMenu

def display_kiosk():
    menu_str = """
    ====== 접수/수납 키오스크 ======
    1. 접수
    2. 수납
    3. 종료
    ======================
    입력: """
    return input(menu_str)

if __name__ == '__main__':
    # PatiRepo 객체 생성 (여러 환자 정보를 저장할 수 있도록)
    patient_repo = PatiRepo()

    while True:
        choice = display_kiosk()

        match choice:
            case '1':  # 접수 선택
                print()
                patient_register = PatiMenu()
                patient_register.register_patient_info()

                # 등록된 환자의 정보 출력
                print()
                print('아래 접수 내역이 올바릅니까?.')
                print('=' * 20)

                # PatiRepo에서 모든 환자 정보 출력
                for patient in patient_register.pati_repo.get_all_patient_info():
                    patient_info = patient.pati_info()
                    print(f"환자 이름: {patient_info['pati_name']}")
                    print(f"환자 주민번호: {patient_info['birth_num'][:6]}-{patient_info['birth_num'][6:]}")
                    print(
                        f"환자 전화번호: {patient_info['pati_phone'][:3]}-{patient_info['pati_phone'][3:7]}-{patient_info['pati_phone'][7:]}")
                    print(f"진료 과목: {patient_info['dept']}")
                    print(f"담당의: {patient_info['doct']}")
                print()
                check=input('y(예) / n(아니오): ')
                if check == 'y':
                    print()
                    print('-' * 30)
                    print(f"\'{patient_info['pati_name']}\'님의 예약번호는 \'{patient_info['reservation_num']}\' 입니다.")
                    print('-' * 30)

            case '2':  # 수납 선택
                pass

            case '3':
                print()
                print("이용해주셔서 감사합니다.")
                break

            case _:  # 잘못된 입력 처리
                print("다시 입력해주세요.")
