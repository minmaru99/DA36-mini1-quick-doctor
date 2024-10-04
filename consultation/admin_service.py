from datetime import datetime
from matplotlib import pyplot as plt


class AdminService:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_patients_from_file(self):
        # 파일 내용을 읽고 줄별로 split하여 리스트로 저장
        with open(self.file_path, 'r', encoding='utf-8') as file:
            patients_list = [line.strip().split(',') for line in file.readlines()]
        return patients_list

    def display_patients_info(self, patients_list):
        if patients_list:
            return patients_list
        else:
            return "등록된 환자 정보가 없습니다."

    def calculate_age(self, social_num):
        current_year = datetime.now().year
        if int(social_num[6]) in (1, 2):
            birth_year = int(social_num[:2]) + 1900
        elif int(social_num[6]) in (3, 4):
            birth_year = int(social_num[:2]) + 2000
        user_age = current_year - birth_year + 1
        return user_age

    def classify_sex(self, social_num):
        if int(social_num[6]) in (1, 3):
            return '남성'
        elif int(social_num[6]) in (2, 4):
            return '여성'

    def age_statistics(self, ages):
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
        max_age=max(ages)
        min_age=min(ages)

        age_group_keys = sorted(age_group.keys())  # 연령대 (10대, 20대 등)
        age_group_values = [age_group[key] for key in age_group_keys]  # 각 연령대의 환자 수

        # 막대그래프 그리기
        plt.bar(age_group_keys, age_group_values, width=5,color='pink')  # width=8로 막대의 너비 설정
        plt.xlabel('age group')
        plt.ylabel('count')
        plt.title('Age Distribution')
        plt.xticks(age_group_keys)  # x축에 연령대를 표시
        plt.show()

        return {
            'avg_age': f'{avg_age:.1f}',
            'max_age': max_age,
            'min_age': min_age,
            'max_age_group': max_count_gens,
            'min_age_group': min_count_gens
        }

    def sex_ratio(self, sexes):
        if not sexes:
            return '등록된 환자 정보가 없습니다.'
        male_count = sexes.count('남성')
        female_count = sexes.count('여성')
        total = len(sexes)

        male_ratio = (male_count/total) * 100
        female_ratio = (female_count/total) * 100

        # 원형 차트 그리기
        plt.pie([male_count,female_count],labels=['male','female'], autopct='%1.1f%%', colors=['lightgreen','violet'])
        plt.title('Patient Sex Ratio')
        plt.show()

        return {
          'male_ratio': f'{male_ratio:.2f}%',
          'female_ratio': f'{female_ratio:.2f}%'
          }

    def count_dept_patients(self,depts):
        dept_counts = {}
        for dept in depts:
            if dept in dept_counts:
                dept_counts[dept] += 1
            else:
                dept_counts[dept] = 1
        sorted_dept_counts = sorted(dept_counts.items(), key=lambda x: x[1], reverse=True)
        # 전체 환자 수 계산
        total_patients = len(depts)
        # 부서별 환자 수와 전체 환자 수 반환
        return sorted_dept_counts, total_patients
