# print(dir([]))

print(dir("pasta")) # calls dir on a string
print(len("pasta")) # calls the built-in __len__ in strings.
print("pasta".__len__())

print("st" in "pasta")
print("pasta".__contains__("st"))

print("pasta" + " and meatballs")
print("pasta".__add__(" and meatballs"))