students = []

with open("students.csv") as file:
    for line in file:  # Read each line
        # Strip /n and split in 2 words
        name, house = line.rstrip().split(",")
        # Create dictionary that store assosiation of name and house
        student = {"name": name, "house": house}
        students.append(student)

# Return the name of the student
def get_name(student):
    return student["name"]

# Add a function (get_name) inside sorted function to sort it by name
for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
