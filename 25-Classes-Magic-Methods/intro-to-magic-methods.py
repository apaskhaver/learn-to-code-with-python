print(3.3 + 4.4)
print(3.3.__add__(4.4))

print()

print(len([1, 2, 3]))
print([1, 2, 3].__len__())

print()

print("h" in "hello")
print("hello".__contains__("h"))

print()

print(["A", "B", "C"][2])
print(["A", "B", "C"].__getitem__(2))