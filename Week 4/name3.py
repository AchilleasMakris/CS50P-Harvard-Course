import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# Start from index 1 and end in blank(everything else)
# The [] can have negative to delete names from the end like
# sys.argv[1:-1] 1 to remove the name of the program
# and -1 to remove last name inputed
for name in sys.argv[1:]:
    print("Hello, my name is", name)
