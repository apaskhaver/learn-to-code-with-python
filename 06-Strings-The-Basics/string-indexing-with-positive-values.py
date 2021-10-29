best_language_ever = "Python"

print(best_language_ever[0])
print(type(best_language_ever[0]))

print(best_language_ever[1])
print(best_language_ever[3])
print(best_language_ever[2 * 2])

# easier to index with a negative value, see string-indexing-with-negative-values.py
print(best_language_ever[len(best_language_ever) - 1])

# best_language_ever[2] = "B" # can't do this b/c Strings are immutable

print("cat"[0])