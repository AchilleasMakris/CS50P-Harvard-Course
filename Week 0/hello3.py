# We can add all those in this
name = input("What's your name? ").strip().title()

# Split user's name into firrst name and last name
first , last = name.split(" ")

# say hello to user
print(f"Hello, {first}")
