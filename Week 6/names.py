names = []

for _ in range(3):
    name = input("What's your name?")
    names.append(name)

for name in sorted(names):
    print(f"Hello, {name}")
