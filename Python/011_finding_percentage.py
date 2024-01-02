if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    mark_sum = 0.0
    for mark in student_marks[query_name]:
        mark_sum += mark

    print("{:.2f}".format(mark_sum/3))