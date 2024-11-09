def main():
    yell("This", "is", "CS50")


def yell(*words):
    #give me the uppercase of the word in the words list
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
