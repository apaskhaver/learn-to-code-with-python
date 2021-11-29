import sys

# allows user input

# .argv stands for argument variable; it returns a list of all the arguments
# the user feeds into the program
# Much like string[] args in Java
print(sys.argv)

print(type(sys.argv))

word_lengths = 0

# skipping the file name and adding up the lengths of all the arguments in argv
for arg in sys.argv[1:]:
    word_lengths += len(arg)

print(f"The total length of all command line arguments is {word_lengths}")