if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    if query_name in student_marks.keys():
        value = student_marks[query_name]
        avg = sum(value)/len(value)
print(format(avg,'.2f'))
