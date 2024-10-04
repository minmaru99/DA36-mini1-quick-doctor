from datetime import datetime
from matplotlib import pyplot as plt
from patient.pati_repo import PatiRepo

class AdminService:
    def __init__(self):
        self.repo = PatiRepo()

    def count_dept_patients(self):
        dept_counts = {}
        for patient in self.repo.patients_info:
            dept = patient.dept
            if dept in dept_counts:
                dept_counts[dept] += 1
            else:
                dept_counts[dept] = 1
        # 환자수를 기준으로 내림차순 정렬
        # print("진료과목별 누적 환자 수:")
        for dept, count in sorted(dept_counts.items(), key=lambda x: x[1], reverse=True):
            print(f'- {dept}: {count}명')

        total_patients = len(self.repo.patients_info)
        print(f'\n➡️ 전체 환자 수: {total_patients}명')

    def calculate_age(self, patient):
        birth_num = patient.birth_num
        current_year = datetime.now().year
        if int(birth_num[6]) in (1, 2):
            birth_year = int(birth_num[:2]) + 1900
        elif int(birth_num[6]) in (3, 4):
            birth_year = int(birth_num[:2]) + 2000
        user_age = current_year - birth_year + 1
        return user_age

    def age_statistics(self):
        ages = [self.calculate_age(patient) for patient in self.repo.patients_info]
        if not ages:
            return '등록된 환자 정보가 없습니다.'

        age_group = {}
        for age in ages:
            gens = (age // 10) * 10
            if gens in age_group:
                age_group[gens] += 1
            else:
                age_group[gens] = 1

        max_count = max(age_group.values())
        min_count = min(age_group.values())

        max_count_gens = [gens for gens, count in age_group.items() if count == max_count]
        min_count_gens = [gens for gens, count in age_group.items() if count == min_count]
        avg_age = sum(ages) / len(ages)

        # x축: 연령대, y축: 환자 수
        age_group_sort = sorted(age_group.keys())
        counts = [age_group[age] for age in age_group_sort]
        # 막대 그래프 그리기
        plt.bar(age_group_sort, counts)
        plt.xlabel('age_group')
        plt.ylabel('count')
        plt.title('age_distribution')
        plt.show()

        # 데이터를 반환하도록 수정
        return {
            'avg_age': avg_age,
            'max_age_group': max_count_gens,
            'min_age_group': min_count_gens
        }

    def classify_sex(self, patient):
        birth_num = patient.birth_num
        if int(birth_num[6]) in (1, 3):
            return '남성'
        elif int(birth_num[6]) in (2, 4):
            return '여성'

    def sex_ratio(self):
        sexes = [self.classify_sex(patient) for patient in self.repo.patients_info]

        if not sexes:
            return '등록된 환자 정보가 없습니다.'

        male_count = sexes.count('남성')
        female_count = sexes.count('여성')
        total = len(sexes)

        male_ratio = (male_count/total) * 100
        female_ratio = (female_count/total) * 100

        # 원형 그래프 그리기
        plt.pie([male_count, female_count], labels=['Male', 'Female'])
        plt.title('Sex Ratio')
        plt.show()

        return {
            'male_ratio': f'{male_ratio:.2f}%',
            'female_ratio': f'{female_ratio:.2f}%'
        }

    def display_all_patients(self):
        if not self.repo.patients_info:
            print("등록된 환자 정보가 없습니다.")
            return
        for patient in self.repo.patients_info:
            print(f'이름: {patient.name}, 주민번호: {patient.social_num}, 전화번호: {patient.phone}')
            print(f'진료과목: {patient.dept}, 담당의" {patient.doc}, 예약번호: {patient.reservation_number}')