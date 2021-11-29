errands = ["Declare independence", "write Constitution", "Run the government", "Retire to Mount Vernon"]

print(enumerate(errands))

for index, errand in enumerate(errands):
    print(f"{index + 1}. {errand}")

for index, errand in enumerate(errands, 1):
    print(f"{index}. {errand}")