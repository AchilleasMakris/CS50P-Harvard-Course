names = []

with open("names.txt") as file:  # No need to specify "r", its default
    for line in file:  # Itterate in file
        names.append(line.rstrip())  # We strip the \n

for name in sorted(names):  # Sort the names
    print(f"Hello, {name}")
