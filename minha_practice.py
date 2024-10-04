# #ㅇㅕㄴㅅㅡㅂㅈㅜㅇ~
# def save_patient_info():
#     # 환자 정보 입력 받기
#     name = input("환자 이름을 입력하세요: ")
#     birth_date = input("환자 생년월일을 입력하세요 (YYYYMMDD): ")
#     phone_number = input("환자 전화번호를 입력하세요: ")
#     # 진료과목 선택
#     depts = ["내과", "소아과", "이빈후과"]
#     depts_str = "\n".join([f'{i + 1}.{dept}' for i, dept in enumerate(depts)])
#     dept_choice = int(input(f'==진료과목을 선택하세요== \n{depts_str}\n선택: ')) - 1
#     dept = depts[dept_choice]
#
#     # 담당의사 선택
#     docs = {
#         "내과": ["김내과", "이내과"],
#         "이빈후과": ["최이빈", "박후과"],
#         "소아과": ["문소아", "한소아"]
#     }
#     docs_str = "\n".join([f'{i + 1}.{doc}' for i, doc in enumerate(docs[dept])])
#     doc_choice = int(input(f'담당의사를 선택해주세요: \n{docs_str}\n선택:')) - 1
#     doc = docs[dept][doc_choice]
#
#     # 예약번호 생성 및 환자 등록
#     # reservation_number = self.service.create_reservation_num()
#     # self.service.add_new_patient(reservation_number, name, age, social_number, dept, doc)
#     # 텍스트 파일에 정보 저장하기
#     with open('patient_info.txt', 'a',encoding='utf-8') as file:  # 'a' 모드: 기존 파일에 덧붙이기
#         file.write(f"성명: {name}, 생년월일: {birth_date}, 전화번호: {phone_number}. 진료과목: {dept}, 담당의사: {doc}\n")
#
#     print("환자 정보가 저장되었습니다.")
#
# # 함수 실행
# save_patient_info()
#
# def view_patient_info():
#     try:
#         with open('patient_info.txt', 'r' ,encoding='utf-8') as file:
#             data = file.read()
#             if data:
#                 print("저장된 환자 정보:")
#                 print(data)
#             else:
#                 print("저장된 환자 정보가 없습니다.")
#     except FileNotFoundError:
#         print("파일이 존재하지 않습니다. 먼저 환자 정보를 저장하세요.")
#
# # 함수 실행
# view_patient_info()
#
# 환자 정보를 저장할 리스트
patients = []


def save_patient_info():
    # 환자 정보 입력 받기
    name = input("환자 이름을 입력하세요: ")
    id_number = input("환자 주민번호를 입력하세요: ")
    phone_number = input("환자 전화번호를 입력하세요: ")
    depts = ["내과", "소아과", "이빈후과"]
    depts_str = "\n".join([f'{i + 1}.{dept}' for i, dept in enumerate(depts)])
    dept_choice = int(input(f'==진료과목을 선택하세요== \n{depts_str}\n선택: ')) - 1
    dept = depts[dept_choice]

        # 담당의사 선택
    docs = {
        "내과": ["김내과", "이내과"],
        "이빈후과": ["최이빈", "박후과"],
         "소아과": ["문소아", "한소아"]
     }
    docs_str = "\n".join([f'{i + 1}.{doc}' for i, doc in enumerate(docs[dept])])
    doc_choice = int(input(f'담당의사를 선택해주세요: \n{docs_str}\n선택:')) - 1
    doc = docs[dept][doc_choice]

    patient = {
        '이름': name,
        '주민번호': id_number,
        '전화번호': phone_number,
        '진료과목': dept,
        '담당의사': doc
    }

    # 리스트에 추가
    patients.append(patient)

    # 텍스트 파일에 추가로 저장
    with open('patients_info.txt', 'a', encoding='utf-8') as file:
        # file.write(f"{patient['이름']}, {patient['주민번호']}, {patient['전화번호']}, {patient['진료과목']}, {patient['담당의사']}\n")
        file.write(f"{patients}\n")

    print("환자 정보가 저장되었습니다.")


# 함수 실행
save_patient_info()
print(patients)