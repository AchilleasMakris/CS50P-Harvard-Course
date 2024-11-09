def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}") #student[0] = name, student[1] = house


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) #Tuple

if __name__ == "__main__":
    main()
