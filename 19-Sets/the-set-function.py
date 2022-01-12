print(set([1, 2, 3]))
print(set([1, 2, 3, 2, 1]))

print(set((1, 2)))
print(set((1, 2, 1, 2, 1)))

print(set("abc"))
print(set("abcba"))

print(set({"key": "value"}))

philosophers = ["Plato", "Socrates", "Aristotle", "Pythagoras", "Socrates", "Aristotle"]
philosophers_set = set(philosophers)
philosophers = list(philosophers_set)
print(philosophers_set)