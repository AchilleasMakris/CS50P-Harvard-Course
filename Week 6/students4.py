students = []

with open("students.csv") as file:
    for line in file:  # Read each line
        # Strip /n and split in 2 words
        name, house = line.rstrip().split(",")
        # Create dictionary that store assosiation of name and house
        student = {"name": name, "house": house}
        students.append(student)


# lambda is the same as creating a function like get_name
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
