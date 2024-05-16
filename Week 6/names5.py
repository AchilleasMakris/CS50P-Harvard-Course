with open("names.txt") as file:
    for line in sorted(file): # Itterate every line and sort them
        print("Hello,", line.rstrip()) # Strip the \n of the file
