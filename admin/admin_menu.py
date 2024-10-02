from patient.pati_menu import PatiMenu
from patient.pati_repo import PatiRepo

#관리자 페이지에서 확인할 수 있는 것들: 사용자 정보/ 병원,의사 정보/ 누적 사용자 수(plot)/ 날짜별 사용자 수/
# 사용자 연령, 성별 통계
# 진료과목별 통계

class Admin:
    def __init__(self):
        self.repo=PatiRepo()

    def count_patients(self):
        print(f'전체 이용 환자: {len(self.repo.patients_info)}명')
        print(f'날짜별 이용 환자:')

    def calculate_age(self,patient):  # 환자 나이 계산
        birth_num=patient.birth_num
        if int(birth_num[6]) in (1,2):
            birth_year=int(birth_num[:2])+1900
        elif int(birth_num[6]) in (3,4):
            birth_year=int(birth_num[:2])+2000

        user_age=abs(2024-birth_year)+1
        return user_age

    def classify_sex(self,patient):
        birth_num=patient.birth_num
        if int(birth_num[6]) in (1,3):
            user_sex='남성'
        elif int(birth_num[6]) in (2,4):
            user_sex='여성'
        return user_sex

    def age_statics(self):
        ages=[]
        for patient in self.repo.patients_info:
            ages.append(self.calculate_age(patient))
        if ages:
            avg_ages=sum(ages)/len(ages)
            max_ages=max(ages)
            min_ages=min(ages)
        else:
            return '등록된 환자 정보가 없습니다.'

        return {
        'avg_age':avg_ages,
        'max_age':max_ages,
        'min_age':min_ages
        }

    def sex_ratio(self):
        sexes=[]
        male,female=(0,0)
        for patient in self.repo.patients_info:
            sexes.append(self.classify_sex(patient))

        if sexes:
            for sex in sexes:
                if sex=='남성':
                    male+=1
                else:
                    female+=1
            male_ratio=f'{(male/len(sexes))*100}%'
            female_ratio=f'{(female/len(sexes))*100}%'
            return male_ratio,female_ratio
        else:
            return '등록된 환자 정보가 없습니다.'

