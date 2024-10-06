from datetime import datetime
# from fontTools.misc.xmlWriter import escape


class Admin:
    def __init__(self, file_path):
        self.file_path = file_path
        self.patients = self.load_patients_from_file()

    def load_patients_from_file(self):
        patients = []  # 데이터를 저장할 리스트
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                content = f.readlines()
                for line in content:
                    # 파일에 저장된 문자열 리스트를 실제 리스트로 변환
                    data = eval(line.strip())  # 각 줄을 파싱하여 리스트로 변환
                    patients.append(data)  # 변환된 리스트를 patients에 추가
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")
        return patients


# 파일 불러오기 예시
if __name__ == "__main__":
    admin = Admin('consultation/patients.txt')  # txt 파일 경로 지정

    # 불러온 환자 리스트 출력
    print("불러온 환자 리스트:")
    print(admin.patients)

    # 주민번호로 나이 계산하가ㅣ
    def calculate_age(social_num):
        current_year = datetime.now().year
        if int(social_num[6]) in (1, 2):
            birth_year = int(social_num[:2]) + 1900
        elif int(social_num[6]) in (3, 4):
            birth_year = int(social_num[:2]) + 2000
        user_age = current_year - birth_year + 1
        return user_age

    # 주민번호로 성별 구분하기
    def classify_sex(social_num):
        if int(social_num[6]) in (1, 3):
            return '남성'
        elif int(social_num[6]) in (2, 4):
            return '여성'

    social_nums=[]
    depts=[]
    ages = []
    sexes=[]

    for p in admin.patients:
        social_nums.append(p[3])
        depts.append(p[4])
    # print(social_nums)
    # print(depts)

    for social_num in social_nums:
        ages.append(calculate_age(social_num))
        sexes.append(classify_sex(social_num))
    # print(ages)
    # print(sexes)

    def age_statistics(ages):
        # if not ages:
        #     return '등록된 환자 정보가 없습니다.'
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
