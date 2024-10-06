from admin_service_new import Admin

class Admin_menu:
    def __init__(self):
        self.admin_service_new = Admin()

    def main_menu(self):
        menu_str = """
    =========⚙️️️ 관리자 모드 ⚙️️️=========
    1. 누적 환자 수 조회
    2. 키오스크 사용자 연령대 통계 조회
    3. 환자 성별 통계 조회
    4. 모든 환자 정보 조회
    5. 처음으로 돌아가기
    =============================
    입력: """
        while True:
            choice = input(menu_str)

            if choice == '1':
                print("======== 누적 환자 수 ========")
                self.admin.count_dept_patients()

            elif choice == '2':
                print('====== 키오스크 사용자 연령대 ======')
                age_stats = self.admin.age_statistics()  # 연령 통계 조회
                print(f'평균 나이: {age_stats["avg_age"]}세')
                print(f'가장 많이 이용한 연령대: {age_stats["max_age_group"]}대')
                print(f'가장 적게 이용한 연령대: {age_stats["min_age_group"]}대')

            elif choice == '3':
                print('======= 환자 성별 통계 =======')
                sex_stats = self.admin.sex_ratio()  # 성별 비율 조회
                print(f'♂️ 남성 환자 비율: {sex_stats["male_ratio"]}')
                print(f'♀️ 여성 환자 비율: {sex_stats["female_ratio"]}')

            elif choice == '4':
                print("======== 모든 환자 정보 조회 🔍 ========")
                self.admin.display_all_patients()

            # elif choice == '5':
            #     print("처음 화면으로 이동합니다.🧸️️")
            #     self.return_menu.main_menu()
            #     return

            else:
                print('❌잘못 입력하셨습니다. 다시 입력해주세요!❌')
