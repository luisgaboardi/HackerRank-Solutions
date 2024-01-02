if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    unique_grades = sorted(set(grade for name, grade in students))
    second_lowest_grade = unique_grades[1]

    second_lowest_students = sorted([name for name, grade in students if grade == second_lowest_grade])

    for student in second_lowest_students:
        print(student)