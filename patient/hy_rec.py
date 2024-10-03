from datetime import datetime

from pati_repo import PatiRepo
from pati_menu import PatiMenu
from pati_entity import Patient

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
                print('예약번호를 입력하세요')
                reservation_num = input('예약번호 8자리 입력:')
                if reservation_num == patient_info['reservation_num']:
                    for patient in patient_register.pati_repo.get_all_patient_info():
                        patient_info = patient.pati_info()
                        print("======예약정보 확인======")
                        today = datetime.today().strftime('%Y/%m/%d/%a')
                        print(f"진료 일자: {today}")
                        print(f"환자 이름: {patient_info['pati_name']}")
                        print(f"환자 주민번호: {patient_info['birth_num'][:6]}-{patient_info['birth_num'][6:]}")
                        print(
                            f"환자 전화번호: {patient_info['pati_phone'][:3]}-{patient_info['pati_phone'][3:7]}-{patient_info['pati_phone'][7:]}")
                        print(f"진료 과목: {patient_info['dept']}")
                        print(f"담당의: {patient_info['doct']}")
                        print("=====최종 결제 금액======")
                    print()

                else:
                    print()
                    print('❌잘못 입력하셨습니다. 8자리의 예약번호를 다시 입력해주세요❌.')

            case '3':
                print()
                print("이용해주셔서 감사합니다.")
                break

            case _:  # 잘못된 입력 처리
                print("다시 입력해주세요.")