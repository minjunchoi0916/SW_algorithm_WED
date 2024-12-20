#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string

# 학생 정보 생성 함수
def generate_random_students(num_students=30):
    students = []
    for _ in range(num_students):
        name = ''.join(random.choices(string.ascii_uppercase, k=2))  # 2글자의 대문자 이름
        age = random.randint(18, 22)  # 18~22 사이의 나이
        score = random.randint(0, 100)  # 0~100 사이의 성적
        students.append({"이름": name, "나이": age, "성적": score})
    return students

# 선택 정렬 함수
def selection_sort(students, key, reverse=False):
    n = len(students)
    for i in range(n):
        selected_idx = i
        for j in range(i + 1, n):
            if (students[j][key] < students[selected_idx][key]) ^ reverse:
                selected_idx = j
        students[i], students[selected_idx] = students[selected_idx], students[i]
    return students

# 삽입 정렬 함수
def insertion_sort(students, key, reverse=False):
    n = len(students)
    for i in range(1, n):
        key_student = students[i]
        j = i - 1
        while j >= 0 and (students[j][key] > key_student[key]) ^ reverse:
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = key_student
    return students

# 퀵 정렬 함수
def quick_sort(students, key, left, right, reverse=False):
    if left < right:
        pivot = partition(students, key, left, right, reverse)
        quick_sort(students, key, left, pivot - 1, reverse)
        quick_sort(students, key, pivot + 1, right, reverse)
    return students

def partition(students, key, left, right, reverse):
    pivot = students[left][key]
    low = left + 1
    high = right
    while True:
        while low <= high and (students[low][key] <= pivot) ^ reverse:
            low += 1
        while low <= high and (students[high][key] > pivot) ^ reverse:
            high -= 1
        if low <= high:
            students[low], students[high] = students[high], students[low]
        else:
            break
    students[left], students[high] = students[high], students[left]
    return high

# 기수 정렬 함수 (성적 기준)
def radix_sort(students):
    max_score = max(students, key=lambda x: x["성적"])["성적"]
    exp = 1
    while max_score // exp > 0:
        counting_sort(students, exp)
        exp *= 10
    return students

def counting_sort(students, exp):
    output = [None] * len(students)
    count = [0] * 10
    for student in students:
        index = student["성적"] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(len(students) - 1, -1, -1):
        index = students[i]["성적"] // exp
        output[count[index % 10] - 1] = students[i]
        count[index % 10] -= 1
    for i in range(len(students)):
        students[i] = output[i]

# 학생 정보 출력 함수
def print_students(students):
    for student in students:
        print(f"이름: {student['이름']}, 나이: {student['나이']}, 성적: {student['성적']}")

# 사용자 인터페이스
def main():
    students = generate_random_students()
    
    while True:
        print("\n생성된 학생 정보:")
        print_students(students)
        
        print("\n메뉴:")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")
        
        choice = input("정렬 기준을 선택하세요 (1,2,3,4): ")
        
        if choice == '1':
            key = '이름'
        elif choice == '2':
            key = '나이'
        elif choice == '3':
            key = '성적'
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")
            continue
        
        order = input("오름차순(1) 또는 내림차순(2)을 선택하세요: ")
        reverse = True if order == '2' else False
        
        algorithm = input("사용할 정렬 알고리즘을 선택하세요 (1: 선택 정렬, 2: 삽입 정렬, 3: 퀵 정렬, 4: 기수 정렬): ")
        
        if algorithm == '1':
            selection_sort(students, key, reverse)
        elif algorithm == '2':
            insertion_sort(students, key, reverse)
        elif algorithm == '3':
            quick_sort(students, key, 0, len(students) - 1, reverse)
        elif algorithm == '4' and key == '성적':
            radix_sort(students)
        else:
            print("기수 정렬은 성적 기준으로만 사용할 수 있습니다.")
            continue
        
        print("\n정렬된 결과:")
        print_students(students)

if __name__ == "__main__":
    main()


# In[ ]:




