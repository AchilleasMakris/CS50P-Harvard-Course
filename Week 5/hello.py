def main():
    name = input("What's your name? ")
    print(hello(name)) # Print the output of the def hello from return


def hello(to="world"):
    return f"Hello, {to}"


if __name__ == "__main__":
    main()
