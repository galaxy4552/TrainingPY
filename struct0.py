import cs50

students = []

for i in range(3):
    name = cs50.get_string("Name: ")
    dorm = cs50.get_string("Dorm: ")

    student = {"name": name, "dorm": dorm}

    students.append(student)

for student in students:
    print(f"{student['name']} is in this {student['dorm']}")