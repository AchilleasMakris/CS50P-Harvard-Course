#if we dont call hello with a parameter on ()
# we print the word (world) as default
def hello(to="world"):
    print("hello,", to)


# We can add all those in this
name = input("What's your name? ")
hello(name)

