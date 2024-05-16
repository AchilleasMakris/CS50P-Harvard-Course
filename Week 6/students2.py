students = []

with open("students.csv") as file:
    for line in file:  # Read each line
        # Strip /n and split in 2 words
        name, house = line.rstrip().split(",")
        # Append to student = []
        students.append(f"{name} is in {house}")

for student in sorted(students):  # Sort students
    print(student)
