# Ask user for their name
name = input("What's your name? ")

# Remove whitespace from str
# name = name.strip()

# Capitalize User's name
# (.capitalize only capitalize first letter, so we use title capitalization)
# name = name.title()

# We can embed 2 methods
name = name.strip().title()


# say hello to user
print(f"Hello, {name}")
