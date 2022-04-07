from Student import Student



def main():
    student_file = open('student.txt', 'r')
    student_file.readline()
    students =[]
    for line in student_file.readlines():
        s = convert_to_student(line)
        students.append(s)
    best_student = students[0]
    for student in students:
        if student.get_gpa() > best_student.get_gpa():
            best_student = student

if __name__ == '__main__':
    main()