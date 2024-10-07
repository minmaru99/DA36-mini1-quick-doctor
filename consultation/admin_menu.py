from matplotlib import pyplot as plt

from consultation.admin_service import *

def admin_menu():
    admin = AdminService('C:\Workspaces\DA36-mini1-quick-doctor\consultation\patients.txt')
    patients = admin.load_patients_from_file()

    while True:
        print("""
    =========⚙️️️ 관리자 모드 ⚙️️️=========
    1. 누적 사용자 수 조회
    2. 사용자 연령대 통계 조회
    3. 사용자 성별 통계 조회
    4. 사용자 정보 조회
    5. 처음 화면으로 돌아가기
    ==================================
    입력: """)

        choice = input()

        if choice == '1':
            depts = [patient[4] for patient in patients]
            dept_counts, total_patients = admin.count_dept_patients(depts)
            print("\n====== 부서별 환자 수 ======")
            for dept, count in dept_counts:
                print(f'- {dept}: {count}명')
            print(f'😷 전체 환자 수 😷: {total_patients}명')

        elif choice == '2':
            ages = [admin.calculate_age(patient[3]) for patient in patients]
            age_stats = admin.age_statistics(ages)
            print("\n====== 📊 키오스크 사용자 연령대 통계 ======")
            print(f"- 평균 나이: {age_stats['avg_age']}세")
            print(f"- 👵🏻 최고령 이용자: {age_stats['max_age']}")
            print(f"- 👶🏻 최연소 이용자: {age_stats['min_age']}")
            print(f"- 가장 많이 이용한 연령대: {age_stats['max_age_group']}대")
            print(f"- 가장 적게 이용한 연령대: {age_stats['min_age_group']}대")

        elif choice == '3':
            sexes = [admin.classify_sex(patient[3]) for patient in patients]
            sex_ratio = admin.sex_ratio(sexes)
            print("\n====== 🍩 키오스크 사용자 성별 통계 ======")
            print(f'♂️ 남성 비율: {sex_ratio["male_ratio"]}')
            print(f'♀️ 여성 비율: {sex_ratio["female_ratio"]}')

        elif choice == '4':
            all_patients_info = admin.display_patients_info(patients)
            if isinstance(all_patients_info, str):
                print(all_patients_info)
            else:
                print('============ 모든 환자 정보 ============')
                for index, patient_info in enumerate(patients, start=1):
                    print(f'{index}. {patient_info}')

        elif choice == '5':
            print("처음 화면으로 돌아갑니다.🏃🏻‍°°°")
            break

        else:
            print("잘못된 선택입니다. 다시 선택해 주세요.")


if __name__ == "__main__":
    admin_menu()