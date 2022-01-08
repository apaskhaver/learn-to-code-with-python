foods = "sushi", "steak", "chicken"
foods = ("sushi", "steak", "chicken")

print(type(foods))

empty = ()
print(type(empty))

mystery = (1)
print(type(mystery)) # parens do not create tuple

mystery = (1, )
print(type(mystery))

print(tuple(["sushi", "steak", "chicken"]))

print(tuple("ABC"))