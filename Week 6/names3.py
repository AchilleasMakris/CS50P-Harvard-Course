with open("names.txt", "r") as file:
    lines = file.readlines()

for name in lines:
    print(f"Hello, {name}", end="")
