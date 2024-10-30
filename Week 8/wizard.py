class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name) #Access super parent class (wizard) and get the assignment
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name) #Access super parent class (wizard) and get the assignment
        self.subject = subject

    ...




wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
