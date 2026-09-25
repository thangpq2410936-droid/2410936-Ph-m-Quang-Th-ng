students = []
courses = []
marks = {}

def input_students():
    n = int(input("Number of students: "))
    for i in range(n):
        id = input("ID: ")
        name = input("Name: ")
        dob = input("DoB: ")
        students.append([id, name, dob])

def input_courses():
    n = int(input("Number of courses: "))
    for i in range(n):
        id = input("Course ID: ")
        name = input("Course name: ")
        courses.append([id, name])

def input_marks():
    for course in courses:
        marks[course[0]] = {}
        for student in students:
            mark = float(input("Mark of " + student[1] + ": "))
            marks[course[0]][student[0]] = mark

def list_students():
    for s in students:
        print(s)

def list_courses():
    for c in courses:
        print(c)

def show_marks():
    course_id = input("Course ID: ")
    for s in students:
        print(s[1], ":", marks[course_id][s[0]])


input_students()
input_courses()
input_marks()

list_students()
list_courses()
show_marks()


